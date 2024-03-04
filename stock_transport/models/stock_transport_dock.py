from odoo import models, fields

class stockTransportDocker(models.Model):
    _name = "stock.transport.dock"
    
    name = fields.Char(required=True)   
