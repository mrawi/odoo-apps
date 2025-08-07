# See LICENSE file for full copyright and licensing details.
{
    'name': "Detailed Access Rights",

    'summary': "Fine-tuned access rights",

    'description': """
        This module adds new security groups to create and update multiple core objects, e.g., products, contacts, 
        price lists and others.\n
        Since users need access to certain features that are allowed for higher-permission groups, 
        this module is designed to provide a workaround for access rights in Odoo that comes naturally with these 
        higher groups.
    """,

    'author': "Mustafa Rawi",
    'website': "https://mrawi.com",
    'license': 'OPL-1',
    'category': 'Sales/Sales',
    'version': '17.0.1.0.3',

    'depends': ['sale', 'stock', 'account', 'purchase'],
    'data': [
        'security/ir_groups.xml',
        'views/views_product_template.xml',
        'views/views_res_partner.xml',
    ]
}
