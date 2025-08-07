# -*- coding: utf-8 -*-
{
    'name': "Calculate Quantity Sheets",

    'summary': """
        Calculate Quantity Sheets""",

    'description': """
        Calculate Quantity from number of Sheets
    """,

    'author': "It Power consulting",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase', 'stock', 'account', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/purchase_order.xml',
        'views/stock_picking.xml',
        'views/account.move.xml',
        'views/sale_order.xml',
        'views/inherit_stock_move_report.xml',
        'views/inherit_sale_order_report.xml',
        'views/inherit_report_deliveryslip.xml',
        'views/inherit_report_picking_operations.xml',

    ],

}
