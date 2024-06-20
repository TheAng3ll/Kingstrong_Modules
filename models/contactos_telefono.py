# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
import logging

_logger = logging.getLogger(__name__)  # declaración del _logger para imprimir mensajes en logs

class Contactos(models.Model):
    _inherit = 'res.partner'  # llamado del modelo del cual vamos a usar sus atributos

    def format_phone(self, phone_number):
        clean_number = re.sub(r'\D', '', phone_number)  # Eliminar todos los caracteres no numéricos
        if len(clean_number) == 10:  # Si es un número de 10 dígitos
            return '+52 1 ' + clean_number[:2] + ' ' + clean_number[2:6] + ' ' + clean_number[6:]
        else:
            return phone_number  # Retorna el número sin cambios si no tiene 10 dígitos

    @api.onchange('phone') #esta funcion no esta funcionando correctamente.
    def _onchange_phone(self):
        if self.phone:
            clean_number = re.sub(r'\D', '', self.phone)
            if len(clean_number) == 10:
                self.phone = self.format_phone(self.phone)
                _logger.info("Número de teléfono formateado: %s", self.phone)
            else:
                _logger.info("Número de teléfono sin formatear debido a longitud incorrecta: %s", self.phone)

    @api.onchange('mobile')
    def _onchange_mobile(self):
        if self.mobile:
            clean_number = re.sub(r'\D', '', self.mobile)
            if len(clean_number) == 10:
                self.mobile = self.format_phone(self.mobile)
                _logger.info("Número de móvil formateado: %s", self.mobile)
            else:
                _logger.info("Número de móvil sin formatear debido a longitud incorrecta: %s", self.mobile)

    @api.constrains('phone', 'mobile')  # llamado de los campos que vamos a necesitar
    def _check_phone(self):  # Función para comparar los campos de teléfono y celular
        phone_pattern = re.compile(r'^\+52\s1\s\d{2}\s\d{4}\s\d{4}$')  # Formato esperado
        for record in self:  # Iterar sobre todos los registros
            if record.phone:  # Validar formato
                formatted_phone = self.format_phone(record.phone)
                if record.phone != formatted_phone:
                    raise ValidationError("Campo teléfono inválido: solo se permiten números en el formato '+52 1 XX XXXX XXXX'.")

            if record.mobile:  # Validar formato
                formatted_mobile = self.format_phone(record.mobile)
                if record.mobile != formatted_mobile:
                    raise ValidationError("Campo móvil inválido: solo se permiten números en el formato '+52 1 XX XXXX XXXX'.")

            existing_mobile = self.env['res.partner'].search([('mobile', '=', record.mobile), ('id', '!=', record.id)])  # Buscar duplicados
            existing_phone = self.env['res.partner'].search([('phone', '=', record.phone), ('id', '!=', record.id)])

            if existing_phone:  # Verificar duplicados
                raise ValidationError("El número de teléfono ya está registrado.")

            if existing_mobile:
                raise ValidationError("El número de celular ya está registrado.")
