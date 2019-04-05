# -*- coding: utf-8 -*-

from odoo import models, fields, api


class truckType(models.Model):
    _name = 'truck.type'
    
    name = fields.Char('Size',required=True)
    note = fields.Char('Note')
    
