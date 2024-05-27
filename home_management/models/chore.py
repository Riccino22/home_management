from odoo import fields, api, models

class Chore(models.Model):
    _name = 'home.chore'
    
    executue_date = fields.Datetime("Execute date")
    