from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    client_rating_ids = fields.One2many(
        comodel_name='product.rating',
        inverse_name='product_tmpl_id',
        string='Ratings'
    )
    average_rating = fields.Float(
        string='Average Rating',
        compute='_compute_average_rating',
        store=True,
        digits=(10, 1),
        help="Computed average of all client ratings."
    )

@api.depends('client_rating_ids.score')
def _compute_average_rating(self):
    for product in self:
        if not product.client_rating_ids:
            product.average_rating = 0.0
            continue

        # Convertimos a int() para poder hacer el promedio
        scores = [int(r.score) for r in product.client_rating_ids if r.score]
        product.average_rating = sum(scores) / len(scores)