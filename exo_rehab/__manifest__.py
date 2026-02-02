{
    'name': 'Rehabilitación con Exoesqueleto',
    'version': '1.0',
    'category': 'Health',
    'summary': 'Gestión de sesiones de rehabilitación con exoesqueletos',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/paciente_views.xml',
        'views/dispositivo_views.xml',
        'views/sesion_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}