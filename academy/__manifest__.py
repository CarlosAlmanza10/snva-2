{

    'name': "Odoo Academy",
    'sumary': """Module to handle COurse and sessions""",
    'description': """Module yo handle
       - Courses
       - Sesions
       - attendes
    """,
    'licencse': 'OPL-1',
    'author': 'carlos',
    'website': 'www.odoo.com',
    'category': 'Custom Modules/tech Training',
    'depends': ['base'],
    'data': [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
        'data/session_data.xml',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml'
    ],  
    'demo': [],
    'version': '0.2',
    'aplication': True
    
}