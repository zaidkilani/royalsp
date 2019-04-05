# -*- coding: utf-8 -*-

from odoo import models, fields, api



class AdditionalCost(models.Model):
    _name = 'additional.cost'
    
    
    product_id = fields.Many2one('product.product', string='Additional Name', required=True ,domain=[('is_discount', '=', True)])
    cost = fields.Float()
    line_cost_id = fields.Many2one('line.cost' ,required=True)
    
    
class LineCostLine(models.Model):
    _name = 'line.cost.line'
    _rec_name = "sea_lines_id"
    
    sea_lines_id = fields.Many2one('sea.lines', 'Container', required=True)
    partner_id = fields.Many2one('res.partner',related="line_cost_id.line_id")
    min_qty = fields.Integer('Minimum Quantity', required=True)
    agency = fields.Float('Agency', related="sea_lines_id.agency",store=True)
    transport_loading_price = fields.Float()
    transport_discharge_price = fields.Float()
    is_loading = fields.Boolean()
    is_discharge = fields.Boolean()
    type = fields.Selection([('loading','Loading'),('discharg','Discharg')])
    product_id = fields.Many2one('product.product', string='Name Of Discount', domain=[('is_discount', '=', True)])
    value = fields.Float('Discount Value')
    rate = fields.Float('Rate')
    line_cost_id = fields.Many2one('line.cost', required=True)
    total = fields.Float('Total',compute='_compute_total')
    
    @api.depends('agency','transport_loading_price','value','rate','transport_discharge_price')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.agency + rec.rate+ rec.transport_discharge_price + rec.transport_loading_price - rec.value
            
    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        print(self._context)
        print(args)
        return super(LineCostLine, self)._search( args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)


class LineCost(models.Model):
    _name = 'line.cost'
    _rec_name = 'line_id'
    
    line_id = fields.Many2one('res.partner', string="Shipping Line", required=True,domain=[('company_type', '=', 'company'),('is_sea_line', '=', True)])
    quot_number = fields.Char(string="Quotation Number", required=True)
    date = fields.Date('Date', required=True)
    country_loading_id = fields.Many2one('res.country', string="Country Of Loading", required=True)
    state_loading_id = fields.Many2one('res.country.state', string="State Of Loading")
    city_loading_id = fields.Many2one('res.city', string="City Of Loading")
    place_loading_id = fields.Many2one('loading.place', string="Place Of Loading")
    transport_loading_id = fields.Many2one('transport.type', string="Transport Type Of Loading")
    port_loading_id = fields.Many2one('port', string="POL")
    country_dest_id = fields.Many2one('res.country', string="Country Of Destination")
    state_dest_id = fields.Many2one('res.country.state', string="State Of Destination")
    city_dest_id = fields.Many2one('res.city', string="City Of Destination")
    place_dest_id = fields.Many2one('res.place', string="Place Of Destination")
    port_dest_id = fields.Many2one('port', string="POD")
    transport_dest_id = fields.Many2one('transport.type', string="Transport Type Of Destination")
    delivery_place_id = fields.Many2one('delivery.place', 'Place Of Delivery')
    bill_fees = fields.Float('Bill fees',compute='_compute_bill_fees',store=True)
    free_demurrage_and_detention = fields.Integer()
    transt_time = fields.Integer()
    customer_id = fields.Many2one('res.partner',stirng='Named Account')
    fak = fields.Boolean('FAK',default=True)
    product_id = fields.Many2one('product.product')
    start_date = fields.Date('Start Date')
    expiry_date = fields.Date('Expiry Date')
    note = fields.Text('Notes')
    expired_price = fields.Boolean()
    next_price = fields.Boolean()
    line_cost_ids = fields.One2many('line.cost.line','line_cost_id',string="Price")
    additional_cost_ids = fields.One2many('additional.cost','line_cost_id',string="Additional Cost")
    product_discount_id = fields.Many2one('product.product', string='Additional Discount' ,domain=[('is_discount', '=', True)])
    discount = fields.Float(default=0.0)
    
    
    @api.model_create_multi
    @api.returns('self', lambda value:value.id)
    def create(self, vals_list):
        res = super(LineCost, self).create( vals_list)
        for rec in res:
            if not rec.place_dest_id:
                rec.line_cost_ids.write({'is_discharge':False,'transport_discharge_price':0.0})
            if not rec.place_loading_id:
                rec.line_cost_ids.write({'is_loading':False,'transport_loading_price':0.0})
        return res
    
    @api.multi
    def write(self, vals):
        res = super(LineCost, self).write(vals)
        for rec in self:
            if not rec.place_dest_id:
                rec.line_cost_ids.write({'is_discharge':False,'transport_discharge_price':0.0})
            if not rec.place_loading_id:
                rec.line_cost_ids.write({'is_loading':False,'transport_loading_price':0.0})
        return res
    @api.depends('line_id')
    def _compute_bill_fees(self):
        for rec in self:
            if rec.line_id:
                rec.bill_fees = rec.line_id.bill_fees
            else:
                rec.bill_fees = 0.0
                
                
            
    @api.onchange('line_id')     
    def onchange_line_id(self):
        self.line_cost_ids = [(6,0,[])]
    
    
    
    
    
    
