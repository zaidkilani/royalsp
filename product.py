# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.template"   
    
    is_discount = fields.Boolean('Is Discount')
    is_inv_charges = fields.Boolean('Is Invoice Charges')

    
class ProductProduct(models.Model):
    _inherit = "product.product"
    
    temperature = fields.Float('Temperature')
    warehouse_condition = fields.Char('Warehouse condition')
    warehouse_condition_att = fields.Binary(attachment=True,string="Attachment")
    transport_condition = fields.Char('Transport condition')
    transport_condition_att = fields.Binary(attachment=True,string="Attachment")
    port_condition = fields.Char('Port condition')
    port_condition_att = fields.Binary(attachment=True,string="Attachment")
    other_condition = fields.Char('Other condition')
    other_condition_att = fields.Binary(attachment=True,string="Attachment")
    
    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        if self._context.get('com_customer_id' ):
            partner_id = self.env['res.partner'].browse(self._context.get('com_customer_id' ))
            args = expression.AND([args] + [[('id','in',partner_id.product_ids.ids)]])
        return super(ProductProduct, self)._search(args, offset, limit, order, count, access_rights_uid)
    