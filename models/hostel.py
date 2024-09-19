from odoo import fields, models, api

class Hostel(models.Model):
    _name = 'hostel.hostel'
    _description = 'Information about hostel'

    name = fields.Char('Hostel name', required=True)
    hostel_code = fields.Char('Code', required=True)
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip', change_default=True)
    city = fields.Char('City')

    state_id = fields.Many2one('res.country.state', string='State')
    country_id = fields.Many2one('res.country', string='Country')

    phone = fields.Char('Phone', required=True)
    mobile = fields.Char('Mobile', required=True)
    email = fields.Char('Email')

    hostel_floors = fields.Integer('Total Floors')
    image = fields.Binary('Hostel Image')
    active = fields.Boolean('Active', default=True, help="Activate/Deactivate hostel record")
    type = fields.Selection([("male", "Boys"), ("female", "Girls"), ("common", "Common")], string="Type",
                            help="Type of Hostel", required=True, default="common")
    other_info = fields.Text("Other information", help="Enter more information")    
    description = fields.Html("Description")
    hostel_rating = fields.Float("Hostel Average Rating", digits='Rating Value')

    category_id = fields.Many2one('hostel.category')

    ref_doc_id = fields.Reference(
        selection='_referencable_models',
        string='Reference Document'
    )

    @api.depends('hostel_code')
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if record.hostel_code:
                name = f'{record.name} ({record.hostel_code})'
            record.display_name = name


    @api.model
    def _referencable_models(self):
        models = self.env['ir.model'].search([
            ('field_id.name', '=', 'message_ids')
        ])

        return [(x.model, x.name) for x in models]

    
    