# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TransportType(models.Model):
    _name = 'transport.type'
    
    name = fields.Char('Name',required=True)
    note = fields.Char('Note')
    
