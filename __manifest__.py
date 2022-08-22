# -*- coding: utf-8 -*-
{
    'name': "Gym Center",

    'summary': """
        Alquiler de equipos de Gimnasio""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Joselyn Quispe",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/user_view.xml',
        'views/machine_view.xml',
        'views/rent_view.xml',
        'views/top_customer_view.xml',
        'views/top_selling_view.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
