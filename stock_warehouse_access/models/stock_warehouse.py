# ******************************************************************************
#  Mustafa Rawi © 2025, all rights reserved.
# See LICENSE file for full copyright and licensing details.
# ******************************************************************************

from odoo import models, fields


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    allowed_user_ids = fields.Many2many(string='Allowed Users',
                                        comodel_name='stock.warehouse',
                                        relation='stock_warehouse_res_users_rel',
                                        column1='warehouse_id',
                                        column2='user_id',
                                        check_company=True)