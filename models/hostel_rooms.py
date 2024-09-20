from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta

class HostelRoom(models.Model):
    _name = 'hostel.room'
    _inherit = ['base.archive']

    _sql_constraints = [
        ('room_no_unique', 'unique(room_num)', 'Room number must be unique!')
    ]

    name = fields.Char('Room name', required=True)
    room_num = fields.Integer('Room No', required=True)
    floor_num = fields.Integer('Floor No', required=True)

    currency_id = fields.Many2one('res.currency', string='Currency')
    rent_amount = fields.Monetary('Rent Amount', 
                                  help='Enter rent amount per month', 
                                  currency_field='currency_id')

    hostel_id = fields.Many2one('hostel.hostel', 'Hostel', help='Name of hostel')
    student_ids = fields.One2many('hostel.student', 'room_id', string='Students', help='Enter student')
    hostel_amenities_ids = fields.Many2many('hostel.amenities', 
                                            'hostel_room_amenities_rel', 
                                            'room_id', 'amenitiy_id', 
                                            string='Amenities', 
                                            domain="[('active', '=', True)]", 
                                            help='Select hostel room amenities')

    student_per_room = fields.Integer('Student per room', 
                                      required=True, 
                                      help='Students allocated per room')

    availability = fields.Float('Availability', 
                                help='Room availability in hostel',
                                compute='_compute_check_availability',
                                store=True)

    admission_date = fields.Date('Admission Date', 
                                 help='Date of admission in hostel', 
                                 default=fields.Datetime.today)

    discharge_date = fields.Date('Discharge Date', help='Date of which student discharge')
    duration = fields.Integer('Duration', compute='_compute_check_duration', inverse='_inverse_duration',
                              help='Enter duration of living')
    

    @api.constrains('rent_amount')
    def _check_rent_amount(self):
        """Constraint on negative rent amount"""

        if self.rent_amount < 0:
            raise ValidationError(_('Rent amount per month should not be negative value!'))
        
    @api.depends('admission_date', 'discharge_date')
    def _compute_check_duration(self):
        """Method to check duration"""
        for rec in self:
            if rec.discharge_date and rec.admission_date:
                rec.duration = (rec.discharge_date - rec.admission_date).days

    def _inverse_duration(self):
        for stu in self:
            if stu.discharge_date and stu.admission_date:
                duration = (stu.discharge_date - stu.admission_date).days

                if duration != stu.duration:
                    stu.discharge_date = (stu.admission_date + timedelta(days=stu.duration)).strftime('%Y-%m-%d')

    @api.depends('student_per_room', 'student_ids')
    def _compute_check_availability(self):
        """Method to check room availability"""

        for rec in self:
            rec.availability = rec.student_per_room - len(rec.student_ids)
