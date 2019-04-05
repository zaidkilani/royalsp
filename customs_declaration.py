# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CustomsDeclaration(models.Model):
    _name = 'customs.declaration'
    
    name = fields.Char('Name',required=True)
    code = fields.Char('Code',required=True)
    note = fields.Char('Note')
    
    @api.multi
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, '%s | %s'%(record.name,record.code)))

        return result
    
