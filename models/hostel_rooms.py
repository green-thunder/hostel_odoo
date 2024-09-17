from odoo import models, fields

class HostelRoom(models.Model):
    _name = 'hostel.room'

    name = fields.Char('Room name', required=True)
    room_num = fields.Integer('Room No', required=True)
    floor_num = fields.Integer('Floor No', required=True)

    currency_id = fields.Many2one('res.currency', string='Currency')
    rent_amount = fields.Monetary('Rent Amount', help='Enter rent amount per month', currency_field='currency_id')

    hostel_id = fields.Many2one('hostel.hostel', 'Hostel', help='Name of hostel')
    student_ids = fields.One2many('hostel.student', 'room_id', string='Students', help='Enter student')
    hostel_amenities_ids = fields.Many2many('hostel.amenities', 'hostel_room_amenities_rel', 'room_id', 'amenitiy_id', string='Amenities', domain="[('active', '=', True)]", help='Select hostel room amenities')
    

    