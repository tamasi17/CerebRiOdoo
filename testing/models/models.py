# models/models.py
from odoo import models, fields, api

class ProductBetaRating(models.Model):
    _name = 'product.beta.rating'  # <--- This is the Table Name
    _description = 'Client Product Rating'

    name = fields.Char(string="Title", required=True)
    rating = fields.Selection([
        ('1', '1 Star'),
        ('2', '2 Stars'),
        ('3', '3 Stars'),
        ('4', '4 Stars'),
        ('5', '5 Stars'),
    ], string="Rating", default='5')

    review = fields.Text(string="Review")