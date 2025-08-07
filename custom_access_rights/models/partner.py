# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import AccessError


class ResPartnerTag(models.Model):
    _inherit = 'res.partner.category'

    def write(self, vals):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_contact_tag'):
            raise AccessError(_('You are not allowed to modify contact tags.'))
        return super(ResPartnerTag, self).write(vals)

    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_contact_tag'):
            raise AccessError(_('You are not allowed to create contact tags.'))
        return super(ResPartnerTag, self).create(vals_list)


class ResPartnerTitle(models.Model):
    _inherit = 'res.partner.title'

    def write(self, vals):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_contact_tag'):
            raise AccessError(_('You are not allowed to modify contact titles.'))
        return super(ResPartnerTitle, self).write(vals)

    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_contact_tag'):
            raise AccessError(_('You are not allowed to create contact titles.'))
        return super(ResPartnerTitle, self).create(vals_list)
