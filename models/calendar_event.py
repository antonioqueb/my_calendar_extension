from odoo import models, fields

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    company_id = fields.Many2one('res.company', string='Empresa', default=lambda self: self.env.company, required=True)
