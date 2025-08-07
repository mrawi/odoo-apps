# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import AccessError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    margin = fields.Monetary(groups='custom_access_rights.detailed_access_group_cost')
    margin_percent = fields.Float(groups='custom_access_rights.detailed_access_group_cost')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    original_price_unit = fields.Float(
        string='Original Price Unit',
        compute='_compute_original_price_unit',
        store=True,
    )

    @api.depends('product_id', 'product_uom', 'product_uom_qty', 'price_unit')
    def _compute_original_price_unit(self):
        """
        Compute and store the original price unit to be compared with price_unit field, then apply access rules.

        Since price_unit may be written by price lists, promotions, etc.
        we need a field to compare with to store the unit price after all other modifiers have been applied.
        """
        for line in self:
            # check if there is already invoiced amount. if so, the price shouldn't change as it might have been
            # manually edited
            if line.qty_invoiced > 0 or (line.product_id.expense_policy == 'cost' and line.is_expense):
                continue
            if not line.product_uom or not line.product_id:
                line.original_price_unit = 0.0
            else:
                line = line.with_company(line.company_id)
                price = line._get_display_price()
                line.original_price_unit = line.product_id._get_tax_included_unit_price_from_price(
                    price,
                    line.currency_id or line.order_id.currency_id,
                    product_taxes=line.product_id.taxes_id.filtered(
                        lambda tax: tax.company_id == line.env.company
                    ),
                    fiscal_position=line.order_id.fiscal_position_id,
                )

    def write(self, vals):
        """
        Override to prevent price_unit being updated unless the user has proper access right.
        If the user does have it, allow and log the change in chatter.
        """

        for line in self:
            unit_price = vals.get('price_unit')
            computed_price = vals.get('original_price_unit') or line.original_price_unit

            if unit_price != computed_price and not self.env.user.has_group(
                    'custom_access_rights.detailed_access_group_sale_price'):
                # if the price unit is being changed and the user does not have the right group,
                raise AccessError(_("You do not have the access right to update unit prices.\n"
                                    "Please contact your administrator."))

            line.order_id.message_post(
                body=f"Product '{line.product_id.display_name}' price has been updated: {unit_price} > {computed_price}.")

        return super(SaleOrderLine, self).write(vals)

    margin = fields.Float(groups='custom_access_rights.detailed_access_group_cost')
    margin_percent = fields.Float(groups='custom_access_rights.detailed_access_group_cost')
    purchase_price = fields.Float(groups='custom_access_rights.detailed_access_group_cost')


class SaleReport(models.Model):
    _inherit = 'sale.report'

    margin = fields.Float(groups='custom_access_rights.detailed_access_group_cost')