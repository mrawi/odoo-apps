# ******************************************************************************
#  Mustafa Rawi © 2025, all rights reserved.
# See LICENSE file for full copyright and licensing details.
# ******************************************************************************

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    allowed_journal_ids = fields.Many2many(string='Allowed Journals',
                                           comodel_name='account.journal',
                                           relation='account_journal_res_users_rel',
                                           column1='user_id',
                                           column2='journal_id',
                                           check_company=True)

    # @property
    # def SELF_READABLE_FIELDS(self):
    #     return super().SELF_READABLE_FIELDS + ['allowed_journal_ids']
