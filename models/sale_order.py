# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
import logging


_logger = logging.getLogger(__name__) #instancia del logg

class Saleorder(models.Model):  # clase para confirmar que pertenecen a un grupo para confirmar la orden de venta y desactivar documento de origen
	_inherit = 'sale.order'

	flag = fields.Boolean(compute='check_group', store=False) #Variable para el permiso de ver margenes

	def check_group(self):  #funcion para validar que el usuario no este dentro del grupo y si es asi el valor cambia a true 
	        for record in self:
			record.flag = not self.user_has_groups('Kingstrong_extended.group_margen')

	def action_confirm(self):
		if not self.env.user.has_group('Kingstrong_extended.group_confirmar'):
			raise ValidationError("No tienes permiso para confirmar este pedido")
		return super(Saleorder, self).action_confirm()
		


class PurchaseOrder(models.Model): #clase para desactivar campo de documento de origen.
	_inherit = 'sale.order.line'
