# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.osv import expression


class ContainerSize(models.Model):
    _name = 'container.size'
    _rec_name = "size"
    
    size = fields.Char('Size',required=True)
    note = fields.Char('Note')
    
