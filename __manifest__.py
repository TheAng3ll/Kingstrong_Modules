{
    'name': 'Kingstrong_extended',
    'version': '1.2.0',
    'depends': ['base', 'contacts', 'sale', 'crm', 'web', 'purchase', 'branch'],
    'author': 'Angel Barrera',
    'category': 'Customization',
    'description': '''Actualizacion 1.2.0:
    - Se corrigue error que no permitia registrar dos leads o mas con el mismo numero.
    - se añade en el leas el campo para el seguimiento.
    - Ahora los contactos creados desde el lead se crean en mayusculas.''',
    'data': ['security/security_groups.xml','views/sale_order.xml', 'views/contact_mobile.xml', 'views/contacto_nombre.xml' ],
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend':[
             
            ],
        },
}
