{
    'name': 'Kingstrong_extended',
    'version': '1.1.0',
    'depends': ['base', 'contacts', 'sale', 'crm', 'web', 'purchase', 'branch'],
    'author': 'Angel Barrera',
    'category': 'Customization',
    'description': '''Actualizacion 1.1.0:
    - Se corrigue error qu emuestra margen a todos los usuarios.
    - Nuevo grupo de seguridad para ver margen.
    - Se elimina codigos obsoletos
    - Se agrego terminos y condiciones en el documento de presupuesto o factura. 
    - El campo de terminos y condiciones es solo lectura.
    - Ajuste de archivo de presupuesto, se agrego boton de Whatsapp que redirijira al asesor de venta.
    - Se corrigue error para agregar numero de telefono en CRM''',
    'data': ['security/security_groups.xml','views/sale_order.xml', 'views/contact_mobile.xml' ],
    'license': 'LGPL-3',
}
