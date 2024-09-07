# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
import logging

_logger = logging.getLogger(__name__) #instancia del logg

class Contactoname(models.Model):
    _inherit = 'res.partner'

    @api.onchange('name')
    def _onchange_name(self):  #funcion para que al registrar las letras sean mayusculas
        if self.name:
            self.name = self.name.upper()


    @api.constrains('name')
    def _check_name(self): #funcion para  comparar que no exista ya un nombre
        for record in self:
            if not self.env.user.has_group('Kingstrong_extended.group_duplicar'):
                existing_partners = self.env['res.partner'].search([('name', '=', record.name), ('id', '!=', record.id )], limit = 1) #busca el nombre
                if existing_partners:
                    raise ValidationError("Este usuario ya esta registrado, si crees que es un usuario nuevo porfavor contacta a tu gerente.")

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.onchange('name')
    def _onchange_name(self):  #funcion para que al registrar las letras sean mayusculas
        if self.name:
            self.name = self.name.upper()

    @api.constrains('name')
    def _check_name(self): #funcion para  comparar que no exista ya un nombre
        for record in self:
            if not self.env.user.has_group('Kingstrong_extended.group_duplicar'):
                existing_partners = self.env['res.partner'].search([('name', '=', record.name), ('id', '!=', record.id )], limit = 1) #busca el nombre
                if existing_partners:
                    raise ValidationError("Este usuario ya esta registrado, si crees que es un usuario nuevo porfavor contacta a tu gerente.")
    
