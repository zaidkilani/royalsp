# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ClearancelinsuCost(models.Model):
    _name = 'clearance.cost.line'
    
    from_truck = fields.Integer('From')
    to_truck = fields.Integer('To')
    cost = fields.Float()
    cost_id = fields.Many2one('clearance.cost',ondelete='cascade')


class ClearanceCost(models.Model):
    _name = 'clearance.cost'
    _rec_name = 'qut_number'
    
   
    qut_number =fields.Char('Quotation Number',required=True)
    is_next = fields.Boolean('Is Next Price')
    is_expired = fields.Boolean('Is Expired Price')
    shipment_method = fields.Selection([('all_in', 'All In'), ('sea_freight', 'Sea freight'), ('land_freight', 'Land Freight'), ('air_freight', 'Air Freight'), ('clearance', 'Clearance')])
    shipment_type = fields.Selection([ ('import', 'Import'), ('export', 'Export')])
    partner_id = fields.Many2one('res.partner',string="Clearance",domain=[('is_clearance_company', '=', True)])
    customs_id = fields.Many2one('res.partner',string="Customs point",domain=[('is_customs_point', '=', True)])
    partner_point_ids = fields.Many2many('res.partner',string="Point Contact",compute="_compute_partner_point_ids")
    customs_declaration_id = fields.Many2one('customs.declaration',string="Customs Declaration")
    date = fields.Date('Date')
    price = fields.Float()
    cost_line_ids = fields.One2many('clearance.cost.line','cost_id',string="Additional Cost")
    total = fields.Float('Total', compute='_compute_total',store=True)
    note = fields.Text()
    
    @api.depends('customs_id')
    def _compute_partner_point_ids(self):
        for rec in self:
            if rec.customs_id:
                rec.partner_point_ids = self.env['res.partner'].with_context(from_customs_filter=False).search([('customs_id','=',rec.customs_id.id)])
            else:
                rec.partner_point_ids = [(5,0,0)]
    @api.depends('price','cost_line_ids','cost_line_ids.cost')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.price + sum(rec.cost_line_ids.mapped('cost')+[0])
            
    
    
    
        
        
    