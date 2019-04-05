# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class TransportlinsuPrice(models.Model):
    _name = 'transport.price.line'
    _rec_name = 'container_size_id'
    
    container_size_id = fields.Many2one('container.size', required=True)
    weight_type_id = fields.Many2one('weight.type')
    truck_type_id = fields.Many2one('truck.type')
    price = fields.Float(required=True)
    cost_id = fields.Many2one('transport.cost')
    
    @api.multi
    def name_get(self):
        lines = []
        for rec in self:
            name = ' | '.join([i for i in [rec.cost_id.partner_id.name, rec.weight_type_id.name, rec.truck_type_id.name] if i])
            lines.append((rec.id,name))
        return lines
    
class TransportlinsuCost(models.Model):
    _name = 'transport.cost.line'
    _rec_name = 'container_size_id'
    
    product_id = fields.Many2one('product.product', string='Transport Name', required=True )
    container_size_id = fields.Many2one('container.size', required=True)
    cost = fields.Float(required=True)
    per_quantity = fields.Boolean()
    cost_id = fields.Many2one('transport.cost')
    


class TransportCost(models.Model):
    _name = 'transport.cost'
    _rec_name = 'qut_number'
   
    qut_number =fields.Char('Quotation Number')
    is_next = fields.Boolean('Is Next Price')
    is_expired = fields.Boolean('Is Expired Price')
    partner_id = fields.Many2one('res.partner',string="Transporter",domain=[('is_transporter_company', '=', True)])
    free_days = fields.Integer('Free Days')    
    country_loading_id = fields.Many2one('res.country', string="Country Of Loading", required=True)
    state_loading_id = fields.Many2one('res.country.state', string="State Of Loading")
    city_loading_id = fields.Many2one('res.city', string="City Of Loading")
    place_loading_id = fields.Many2one('loading.place', string="Place Of Loading")
    country_dest_id = fields.Many2one('res.country', string="Country Of Destination")
    state_dest_id = fields.Many2one('res.country.state', string="State Of Destination")
    city_dest_id = fields.Many2one('res.city', string="City Of Destination")
    place_dest_id = fields.Many2one('res.place', string="Place Of Destination")
    is_port = fields.Boolean(related="place_dest_id.is_port",store=True)
    date = fields.Date('Date')
    price = fields.Float()
    cost_line_ids = fields.One2many('transport.cost.line','cost_id',string="Additional Cost")
    price_line_ids = fields.One2many('transport.price.line','cost_id',string="Price")
    total = fields.Float('Total', compute='_compute_total',store=True)
    note = fields.Text()
    
    
    @api.constrains('is_port','place_dest_id')
    def is_port_check(self):
        for rec in self:
            if not rec.is_port and rec.place_dest_id:
                raise UserError('You cannot create transport cost with a not place port')
                
                
        
        
    @api.depends('price','cost_line_ids','cost_line_ids.cost')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.price + sum(rec.cost_line_ids.mapped('cost')+[0])
            
    
    
    
        
        
    