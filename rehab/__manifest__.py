{
    'name': "Rehab",

    'summary': "Rehabilitation program for our customers",

    'description': """
    The Exoskeleton Rehabilitation Tracker is a specialized clinical management tool.
    It bridges the gap between advanced robotic therapy and patient data management.
    Designed for all type of clients, this module allows therapists to monitor patient progress,
    log device-assisted sessions, and visualize recovery data directly within their ERP environment.    """,

    'author': "Cereb.ri",
    'website': "https://www.cereb.ri",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Medic',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/rehab_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}

