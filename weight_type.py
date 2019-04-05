# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WeightType(models.Model):
    _name = 'weight.type'
    
    name = fields.Char('Size',required=True)
    note = fields.Char('Note')
    
