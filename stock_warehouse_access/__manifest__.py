# ******************************************************************************
#  Mustafa Rawi © 2025, all rights reserved.
# See LICENSE file for full copyright and licensing details.
# ******************************************************************************

{
    'name': 'Warehouse Access Rules',
    'version': '18.0.1.0.0',
    'license': 'OPL-1',
    'summary': 'Limit access to warehouses',
    'sequence': 50,
    'description': """
Allow access to warehouses on user level.
    """,
    'category': 'Inventory/Inventory',
    'author': 'Mustafa Rawi',
    'website': 'https://mrawi.com',
    'price': 15,
    'currency': 'EUR',
    'images': [],
    'depends': ['stock'],
    'data': [
        'security/ir_rules.xml',
        'views/res_users_views.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    # 'post_init_hook': '_auto_install_l10n',
}
