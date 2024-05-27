from odoo import fields, api, models

class Chore(models.Model):
    _name = 'home.chore'
    
    title = fields.Char("Title")
    description = fields.Text("Description")
    executue_date = fields.Datetime("Execute date")
    partner_id = fields.Many2one("res.partner", string="Assigned")
    status = fields.Selection([
        ("in_progress", "In progress"),
        ('draft', 'Draft'),
        ('done', 'Done'),
        ("blocked", "Blocked"),
        ('cancel', 'Cancel'),
        
    ])
    