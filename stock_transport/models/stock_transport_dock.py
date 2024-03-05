from odoo import models, fields

class stockTransportDock(models.Model):
    _name = "stock.transport.dock"
    _description = "Model for Dock"
    
    name = fields.Char(required=True)   
