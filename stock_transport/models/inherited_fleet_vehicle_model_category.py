from odoo import api, fields, models

class inheritedFleetVehicleModelCategory(models.Model):
    _inherit = "fleet.vehicle.model.category"
    
    max_weight = fields.Float()
    max_volume = fields.Float()
    
    # SQL constraints
    _sql_constraints = [('check_max_weight', 'CHECK(max_weight>0)', 'Maximum weight must be strictly positive'),
                        ('check_max_volume', 'CHECK(max_volume>0)', 'Maximum volume must be strictly positive')]
    
    # Function for computing display name
    @api.depends('name', 'max_weight', 'max_volume')
    def _compute_display_name(self):
        for record in self:
            name = f"{record.name} ({record.max_weight}kg, {record.max_volume}cm)"
            record.display_name = name
