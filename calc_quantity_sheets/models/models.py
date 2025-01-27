# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    sheet_num = fields.Float(string='Sheets')
    product_qty = fields.Float(string='Quantity', digits='Product Unit of Measure', required=True,
                               compute='_compute_product_qty', store=True, readonly=True)

    @api.depends('sheet_num')
    def _compute_product_qty(self):
        for line in self:
            if line.product_uom.uom_type == 'bigger':
                line.product_qty = line.sheet_num * line.product_uom.ratio
            elif line.product_uom.uom_type == 'smaller':
                line.product_qty = line.sheet_num / line.product_uom.ratio
            else:
                line.product_qty = line.sheet_num

    def _prepare_stock_moves(self, picking):
        res = super(PurchaseOrderLine, self)._prepare_stock_moves(picking)
        for re in res:
            re['sheet_num'] = self.sheet_num
        return res

    def _prepare_account_move_line(self, move=False):
        res = super()._prepare_account_move_line(move)
        res.update({'sheet_num': self.sheet_num})
        return res


class StockMove(models.Model):
    _inherit = 'stock.move'

    sheet_num = fields.Float(string='Sheets')
    product_uom_qty = fields.Float(
        'Demand',
        digits='Product Unit of Measure',
        default=1.0, required=True, states={'done': [('readonly', True)]},
        help="This is the quantity of products from an inventory "
             "point of view. For moves in the state 'done', this is the "
             "quantity of products that were actually moved. For other "
             "moves, this is the quantity of product that is planned to "
             "be moved. Lowering this quantity does not generate a "
             "backorder. Changing this quantity on assigned moves affects "
             "the product reservation, and should be done with care.")

    quantity_done = fields.Float(
        'Quantity Done', compute='_quantity_done_compute', digits='Product Unit of Measure',
        inverse='_quantity_done_set', store=True)

    @api.onchange('sheet_num','product_uom')
    def compute_product_uom_qty(self):
        for line in self:
            if line.product_uom.uom_type == 'bigger':
                line.product_uom_qty = line.sheet_num * line.product_uom.ratio
            elif line.product_uom.uom_type == 'smaller':
                line.product_uom_qty = line.sheet_num / line.product_uom.ratio
            else:
                line.product_uom_qty = line.sheet_num

    @api.onchange('sheet_num','product_uom')
    def compute_quantity_done(self):
        for line in self:
            if line.product_uom.uom_type == 'bigger':
                line.quantity_done = line.sheet_num * line.product_uom.ratio
            elif line.product_uom.uom_type == 'smaller':
                line.quantity_done = line.sheet_num / line.product_uom.ratio
            else:
                line.quantity_done = line.sheet_num


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    sheet_num = fields.Float(string='Sheets')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    sheet_num = fields.Float(string='Sheets')


    @api.depends('sheet_num')
    def _compute_product_uom_qty(self):
        for line in self:
            if line.product_uom.uom_type == 'bigger':
                line.product_uom_qty = line.sheet_num * line.product_uom.ratio
            elif line.product_uom.uom_type == 'smaller':
                line.product_uom_qty = line.sheet_num / line.product_uom.ratio
            else:
                line.product_uom_qty = line.sheet_num

    def _prepare_procurement_values(self, group_id=False):
        res = super()._prepare_procurement_values(group_id)
        res['sheet_num'] = self.sheet_num
        return res

    def _prepare_invoice_line(self, **optional_values):
        res = super()._prepare_invoice_line(**optional_values)

        res['sheet_num'] = self.sheet_num
        return res


class StockRuleInherit(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id,
                               values):
        move_values = super()._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin,
                                                     company_id, values)
        if values.get('sheet_num') and values.get('group_id'):
            move_values['sheet_num'] = values['sheet_num']

        return move_values


class ProductProduct(models.Model):
    _inherit = 'product.product'

    sheet_num = fields.Float(string='Sheets', compute='_compute_product_sheets')

    @api.depends('qty_available')
    def _compute_product_sheets(self):
        for line in self:
            if line.uom_id.uom_type == 'bigger':
                line.sheet_num = line.qty_available / line.uom_id.ratio
            elif line.uom_id.uom_type == 'smaller':
                line.sheet_num = line.qty_available * line.uom_id.ratio
            else:
                line.qty_available = line.sheet_num
