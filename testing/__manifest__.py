{
    'name': "Product Beta Rater",

    'summary': "Space for Clients to test the Products and Rate it",

    'description': """
You know when you buy something that looks really cool and tech and futuristic but its just lame?
Like buying some techwear water-proof iridiscent thermal cargo pants in wish and getting a mini-skirt.
Yeah that happened to me once I swear. I look amazing with it, always wear it the first day of summer.
    """,

    'author': "Cereb.ri",
    'website': "https://www.cereb.ri",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Marketing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'website', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/product_rating_views.xml',
        'views/product_template_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': False, # Makes it a main App on the dashboard, but moved to Inventory Menu
    'installable': True,
    'license': 'LGPL-3',
}

