from odoo import fields, api, models
from odoo.exceptions import ValidationError

class Chore(models.Model):
    _name = 'home.chore'
    
    title = fields.Char("Title")
    description = fields.Text("Description")
    execute_date = fields.Datetime("Execute date")
    partner_id = fields.Many2one("res.partner", string="Assigned")
    status = fields.Selection([
        ("in_progress", "In progress"),
        ('draft', 'Draft'),
        ('done', 'Done'),
        ("blocked", "Blocked"),
        ('cancel', 'Cancel'),
        
    ])

    @api.constrains("execute_date")
    def _check_date(self):
        for record in self:
            if record.execute_date < fields.Datetime.now():
                raise ValidationError("The date must be today or later")
            
    @api.depends("title")
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.title
    