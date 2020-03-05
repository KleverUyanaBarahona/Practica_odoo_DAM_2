# -*- coding: utf-8 -*-

{
    'name': "Citas",

    'summary': """
    Generador de Citas en Odoo con los campos: 
    Cita, Autor de la cita,  
    Fecha de visualización 
    y Orden de visualización
    """,

    "description": """
    DAM 2 Vespertino: 
    Creación de módulos para Odoo
    """,

    'author': "Klever Uyana y Anthony Moscoso",
    'website': "_",

    
    'category': 'Uncategorized',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views_citasjfsp.xml',
    ],
	
	'images': [
        'static/description/icono.png',
    ],
	
	'installable': True,
    'aplication' : True,
    'auto_install': False,  
}
