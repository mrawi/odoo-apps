# ******************************************************************************
#  Mustafa Rawi © 2025, all rights reserved.
# See LICENSE file for full copyright and licensing details.
# ******************************************************************************

from odoo import models, fields


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    allowed_user_ids = fields.Many2many(string='Allowed Users',
                                        comodel_name='res.users',
                                        relation='account_journal_res_users_rel',
                                        column1='journal_id',
                                        column2='user_id',
                                        check_company=True,)