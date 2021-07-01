# -*- coding: utf-8 -*-

{
    'name': 'acceso',
    
    'sumary': """ Recuperar Cuenta desde Portalfarma""",
    
    'description': """ Si usuario existe en Portalfarma y contraseña coincide, asignamos dicha contraseña al usuario en Odoo y ponemos dicho usuario como 'USER : PORTAL' """,
    
    'author': 'AMP Software',
    
    'Website': 'https://www.ampsoftware.com',
    
    'category': 'Training',
    
    'version': '1.0',
    
    'depends': [
        'website',
        'web',
    ],
    
    'data': [
        'views/acceso_templates.xml'
    ],
    
    'demo': [
    ],
}