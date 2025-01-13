# ******************************************************************************
#  Mustafa Rawi © 2025, all rights reserved.
# See LICENSE file for full copyright and licensing details.
# ******************************************************************************

{
    'name': 'Account Journal Rules',
    'version': '18.0.1.0.0',
    'license': 'OPL-1',
    'summary': 'Limit access to journals',
    'sequence': 50,
    'description': """
Allow access to journals on user level.
    """,
    'category': 'Accounting/Accounting',
    'author': 'Mustafa Rawi',
    'website': 'https://mrawi.com',
    'price': 15,
    'currency': 'EUR',
    'images': [],
    'depends': ['account'],
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
