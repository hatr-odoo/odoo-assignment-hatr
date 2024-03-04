from odoo import api, fields, models
from dateutil.relativedelta import relativedelta

class inheritedStockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"
    
    vehicle_id = fields.Many2one('fleet.vehicle', required=False)
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category')
    weight = fields.Float(compute = '_compute_weight', store=True)
    volume = fields.Float(compute = '_compute_volume', store=True)
    number_of_transfer = fields.Integer(compute = "_compute_number_of_transfer", store=True)
    number_of_lines = fields.Integer(compute = "_compute_number_of_lines", store=True)
    dock_id = fields.Many2one('stock.transport.dock')
    date_start = fields.Date(default = fields.Date.today())
    date_deadline = fields.Date(default = fields.Date.today()+relativedelta(days=30))
    
    # method for computing weight
    @api.depends('picking_ids', 'vehicle_category_id')
    def _compute_weight(self):
        for record in self:
            record.weight=0
            for picking in record.picking_ids:
                record.weight+=picking.weight
            if record.vehicle_category_id.max_weight > 0:
                record.weight = (record.weight / record.vehicle_category_id.max_weight) * 100
      
    # method for computing volume  
    @api.depends('picking_ids', 'vehicle_category_id')
    def _compute_volume(self):
        for record in self:
            record.volume=0
            for picking in record.picking_ids:
                record.volume+=picking.volume
            if record.vehicle_category_id.max_volume > 0:
                record.volume = (record.volume / record.vehicle_category_id.max_volume) * 100
    
    # method for computing number of transfers
    @api.depends('picking_ids')
    def _compute_number_of_transfer(self):
        for record in self:
            record.number_of_transfer = len(record.picking_ids)
    
    # method for computing number of lines
    @api.depends('move_ids')
    def _compute_number_of_lines(self):
        for record in self:
            record.number_of_lines = len(record.move_ids)
