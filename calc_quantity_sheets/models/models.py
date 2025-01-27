# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    sheet_num = fields.Float(string='Sheets')

    @api.depends('sheet_num')
    def _compute_product_qty(self):
        super()._compute_product_qty()
        for line in self:
            if line.product_uom.uom_type == 'bigger':
                qty = line.sheet_num * line.product_uom.ratio
            elif line.product_uom.uom_type == 'smaller':
                qty = line.sheet_num / line.product_uom.ratio
            else:
                qty = line.sheet_num
            line.product_qty = qty

    def _prepare_stock_moves(self, picking):
        moves = super(PurchaseOrderLine, self)._prepare_stock_moves(picking)
        for move in moves:
            move['sheet_num'] = self.sheet_num
        return moves

    def _prepare_account_move_line(self, move=False):
        aml = super()._prepare_account_move_line(move)
        aml.update({'sheet_num': self.sheet_num})
        return aml


class StockMove(models.Model):
    _inherit = 'stock.move'

    sheet_num = fields.Float(string='Sheets')

    @api.onchange('sheet_num','product_uom')
    def _onchange_sheets_uoms(self):
        for line in self:
            if line.product_uom.uom_type == 'bigger':
                qty = line.sheet_num * line.product_uom.ratio
            elif line.product_uom.uom_type == 'smaller':
                qty = line.sheet_num / line.product_uom.ratio
            else:
                qty = line.sheet_num
            line.update({
                'product_uom_qty': qty,
                'quantity_done': qty,
            })


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
                qty = line.sheet_num * line.product_uom.ratio
            elif line.product_uom.uom_type == 'smaller':
                qty = line.sheet_num / line.product_uom.ratio
            else:
                qty = line.sheet_num
            line.product_uom_qty = qty

    def _prepare_procurement_values(self, group_id=False):
        res = super()._prepare_procurement_values(group_id)
        res['sheet_num'] = self.sheet_num
        return res

    def _prepare_invoice_line(self, **optional_values):
        res = super()._prepare_invoice_line(**optional_values)

        res['sheet_num'] = self.sheet_num
        return res


class StockRule(models.Model):
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
        for product in self:
            if product.uom_id.uom_type == 'bigger':
                qty = product.qty_available / product.uom_id.ratio
            elif product.uom_id.uom_type == 'smaller':
                qty = product.qty_available * product.uom_id.ratio
            else:
                qty = product.qty_available

            product.sheet_num = qty
