{
    'name': 'Event Proposals',
    'version': '1.0',
    'category': 'Operations/Events',
    'summary': 'Gestión de propuestas para workshops de integración y pruebas de exoesqueletos.',
    'depends': ['event', 'event_sale', 'event_sms', 'website_event'],
    'data': [
        'security/ir.model.access.csv',
        'views/event_event_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}