from odoo import models, fields

class HostelAmenities(models.Model):
    _name = 'hostel.amenities'
    _description = 'Hostel amenities'

    name = fields.Char('Name', help='Provided Hostel Amenity')
    active = fields.Boolean('Active', help='Activate/Deactivate wheter the amenity should be given or not')

    

    