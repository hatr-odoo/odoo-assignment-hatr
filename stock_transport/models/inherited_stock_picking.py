from odoo import api, fields, models

class inheritedStockPicking(models.Model):
    _inherit = "stock.picking"
    
    weight = fields.Float(compute = "_compute_weight")
    
    volume = fields.Float(compute = "_compute_volume")
            
    # method for computing weight
    @api.depends('move_line_ids')
    def _compute_weight(self):
        for record in self:
            record.weight=0
            for move in record.move_line_ids:
                record.weight+=move.quantity * move.product_id.weight
      
    # method for computing volume  
    @api.depends('move_line_ids')
    def _compute_volume(self):
        for record in self:
            record.volume=0
            for move in record.move_line_ids:
                record.volume+=move.quantity * move.product_id.volume
