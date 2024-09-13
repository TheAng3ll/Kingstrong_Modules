# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
import logging

_logger = logging.getLogger(__name__)  # declaración del _logger para imprimir mensajes en logs

class Contactos(models.Model):
    _inherit = 'res.partner'  # llamado del modelo del cual vamos a usar sus atributos

    mobile = fields.Char(readonly=True) # campo mobil solo lectura

    def format_phone_number(self, number): # Formatear el número en el formato +52 1 XX XXXX XXXX
        return '+52 1 {} {} {}'.format(number[:2], number[2:6], number[6:])
        

    @api.onchange('phone') #funcion para verificar el formato del numero de telefono, digitos, cantidad y solo acepta numeros
    def _onchange_phone(self):
        if self.phone:
            clean_number = re.sub(r'\D', '', self.phone) #Eliminar los caracteres no numericos
            if clean_number.startswith('521'): # Este if se encarga de eliminar la Lada y dejando solo los numeros, esto es un desarrollo especial para chatroom.
                clean_number =clean_number[3:]
            if len(clean_number) == 10: # solo acepta 10 digitos una vez limpio
                formatted_number = self.format_phone_number(clean_number) #la variable adquiere el valor de el numero con el formato
                self.phone = formatted_number # Imprime el numero en el campo front
            else:
                raise ValidationError("Numero invalido: solo se permiten numeros de 10 digitos sin incluir lada.")
        else: #si el campo esta vacio imprime este defecto
            self.phone = '+52 1 00 0000 0000'


    @api.constrains('phone')  
    def _check_phone(self):  # Función para comparar los campos de teléfono 
        for record in self:  # Iterar sobre todos los registros
            existing_phone = False # Declaracion de variable a comparar
            if record.phone and record.phone != '+52 1 00 0000 0000':  # Validar formato y que sea diferen al de defecto
                existing_phone = self.env['res.partner'].search([('phone', '=', record.phone), ('id', '!=', record.id)]) #al ecnontrar le da valor

                if existing_phone:  # Verificar duplicados al encontrar que si tenga valor
                    raise ValidationError("El número de teléfono ya está registrado.")



class crmLead(models.Model):
    _inherit = 'crm.lead'

    def format_phone_number(self, number): # Formatear el número en el formato +52 1 XX XXXX XXXX
        return '+52 1 {} {} {}'.format(number[:2], number[2:6], number[6:])


    @api.onchange('phone') #funcion para verificar el formato del numero de telefono, digitos, cantidad y solo acepta numeros
    def _onchange_phone(self):
        if self.phone:
            clean_number = re.sub(r'\D', '', self.phone) #Eliminar los caracteres no numericos
            existing_phone = False # Declaracion de variable a comparar
            if len(clean_number) == 10: # solo acepta 10 digitos una vez limpio
                formatted_number = self.format_phone_number(clean_number) #la variable adquiere el valor de el numero con el formato
                self.phone = formatted_number # Imprime el numero en el campo front
            else:
                raise ValidationError("Numero invalido: solo se permiten numeros de 10 digitos sin incluir lada.")
        else: #si el campo esta vacio imprime este defecto
            self.phone = '+52 1 00 0000 0000'


