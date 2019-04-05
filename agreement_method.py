# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AgreementMethod(models.Model):
    _name = 'agreement.method'
    
    name = fields.Char('Name',required=True)
    note = fields.Char('Note')
    
