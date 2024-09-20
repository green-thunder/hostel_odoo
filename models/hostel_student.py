from odoo import models, fields

class HostelStudent(models.Model):
    _name = 'hostel.student'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Hostel student information'

    name = fields.Char('Student name')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', help='Student gender')

    active = fields.Boolean('Active', default=True, help='Activate/Deactivate hostel record')
    room_id = fields.Many2one('hostel.room', 'Room', help='Select hostel room')

    hostel_id = fields.Many2one('hostel.hostel', related='room_id.hostel_id')
    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    

