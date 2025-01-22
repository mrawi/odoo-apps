# ******************************************************************************
#  Mustafa Rawi © 2025, all rights reserved.
# See LICENSE file for full copyright and licensing details.
# ******************************************************************************

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    allowed_warehouse_ids = fields.Many2many(string='Allowed Warehouses',
                                             comodel_name='stock.warehouse',
                                             relation='stock_warehouse_res_users_rel',
                                             column1='user_id',
                                             column2='warehouse_id')

    def _get_default_warehouse_id(self):
        if self.allowed_warehouse_ids:
            return self.allowed_warehouse_ids.filtered(lambda wh: wh.company_id == self.company_id)[0]
        return super()._get_default_warehouse_id()

    @property
    def SELF_READABLE_FIELDS(self):
        return super().SELF_READABLE_FIELDS + ['allowed_warehouse_ids']
