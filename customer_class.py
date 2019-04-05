# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CustomerClass(models.Model):
    _name = 'customer.class'
    
    name = fields.Char('Name',required=True)
    note = fields.Char('Note')
    
