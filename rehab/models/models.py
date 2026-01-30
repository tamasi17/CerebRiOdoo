from odoo import models, fields, api

class Rehab(models.Model):
    _name = 'rehab'  # <--- This is the Table Name
    _description = 'Rehab for losers'

    name = fields.Char(string="Title", required=True)
    rating = fields.Selection([
        ('1', '1 Star'),
        ('2', '2 Stars'),
        ('3', '3 Stars'),
        ('4', '4 Stars'),
        ('5', '5 Stars'),
    ], string="Rating", default='5')

    review = fields.Text(string="Review")