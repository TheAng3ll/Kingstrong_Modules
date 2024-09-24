# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
import logging

_logger = logging.getLogger(__name__) #instancia del logg

class Inventario(models.Model):
	_inherit = 'stock.quant'


