# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InsuranceType(models.Model):
    _name = 'insurance.type'
    
    name = fields.Char('Name',required=True)
    note = fields.Char('Note')
    
