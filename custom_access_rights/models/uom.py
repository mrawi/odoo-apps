# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import AccessError


class UnitOfMeasure(models.Model):
    _inherit = 'uom.uom'

    def write(self, vals):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_uom'):
            raise AccessError(_('You are not allowed to modify units of measure.'))
        return super(UnitOfMeasure, self).write(vals)

    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_uom'):
            raise AccessError(_('You are not allowed to create units of measure.'))
        return super(UnitOfMeasure, self).create(vals_list)


class UomCategory(models.Model):
    _inherit = 'uom.category'

    def write(self, vals):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_uom'):
            raise AccessError(_('You are not allowed to modify unit of measure categories.'))
        return super(UomCategory, self).write(vals)

    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_uom'):
            raise AccessError(_('You are not allowed to create unit of measure categories.'))
        return super(UomCategory, self).create(vals_list)