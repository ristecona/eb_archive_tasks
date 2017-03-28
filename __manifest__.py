# -*- coding: utf-8 -*-
{
    'name': "eb_archive_tasks",

    'summary': """
        Archive tasks using list view in odoo""",

    'description': """
        Archive tasks using list view in odoo
    """,

    'author': "Euroblaze, Cona Cons",
    'website': "http://www.simplify-erp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
