# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import AccessError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def write(self, vals):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_product'):
            raise AccessError(_('You are not allowed to modify products.'))
        return super(ProductTemplate, self).write(vals)

    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_product'):
            raise AccessError(_('You are not allowed to create products.'))
        return super(ProductTemplate, self).create(vals_list)

    standard_price = fields.Float(groups='custom_access_rights.detailed_access_group_cost,purchase.group_purchase_user')
    seller_ids = fields.One2many(groups='custom_access_rights.detailed_access_group_cost,purchase.group_purchase_user')
    variant_seller_ids = fields.One2many(groups='custom_access_rights.detailed_access_group_cost,purchase.group_purchase_user')


class ProductVariant(models.Model):
    _inherit = 'product.product'

    def write(self, vals):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_product'):
            raise AccessError(_('You are not allowed to modify product variants.'))
        return super(ProductVariant, self).write(vals)

    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_product'):
            raise AccessError(_('You are not allowed to create product variants.'))
        return super(ProductVariant, self).create(vals_list)

    standard_price = fields.Float(groups='custom_access_rights.detailed_access_group_cost,purchase.group_purchase_user')


class ProductCategory(models.Model):
    _inherit = 'product.category'

    def write(self, vals):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_product_categ'):
            raise AccessError(_('You are not allowed to modify products categories.'))
        return super(ProductCategory, self).write(vals)

    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_product_categ'):
            raise AccessError(_('You are not allowed to create product categories.'))
        return super(ProductCategory, self).create(vals_list)


class ProductAttribute(models.Model):
    _inherit = 'product.attribute'

    def write(self, vals):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_product_attribute'):
            raise AccessError(_('You are not allowed to modify product attributes.'))
        return super(ProductAttribute, self).write(vals)

    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_product_attribute'):
            raise AccessError(_('You are not allowed to create product attributes.'))
        return super(ProductAttribute, self).create(vals_list)


class ProductPackaging(models.Model):
    _inherit = 'product.packaging'

    def write(self, vals):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_product_packaging'):
            raise AccessError(_('You are not allowed to modify product packaging.'))
        return super(ProductPackaging, self).write(vals)

    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_product_packaging'):
            raise AccessError(_('You are not allowed to create product packaging.'))
        return super(ProductPackaging, self).create(vals_list)


class PriceList(models.Model):
    _inherit = 'product.pricelist'

    def write(self, vals):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_pricelist'):
            raise AccessError(_('You are not allowed to modify price lists.'))
        return super(PriceList, self).write(vals)

    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.user.has_group('custom_access_rights.detailed_access_group_pricelist'):
            raise AccessError(_('You are not allowed to create price lists.'))
        return super(PriceList, self).create(vals_list)
