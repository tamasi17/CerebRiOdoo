from odoo import models, fields, api, exceptions

class ProductRating(models.Model):
    _name = 'product.rating'
    _description = 'Product Client Rating'
    _order = 'create_date desc'

    name = fields.Char(
        string='Reference',
        required=True,
        default='New',
        readonly=True
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Client',
        required=True,
        ondelete='cascade'
    )
    product_tmpl_id = fields.Many2one(
        comodel_name='product.template',
        string='Product',
        required=True,
        ondelete='cascade'
    )
    score = fields.Selection([
        ('1', '1 Estrella'),
        ('2', '2 Estrellas'),
        ('3', '3 Estrellas'),
        ('4', '4 Estrellas'),
        ('5', '5 Estrellas'),
    ], string='Score', default='5', required=True)

    comment = fields.Text(string='Feedback')

    @api.model_create_multi
    def create(self, vals_list):
        """Override create to generate sequence or naming convention."""
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                # In a real scenario, use ir.sequence here
                vals['name'] = f"RATING-{fields.Datetime.now()}"
        return super().create(vals_list)

    @api.constrains('score')
    def _check_score_range(self):
        """Ensure the score is within valid bounds."""
        for record in self:
            if not (1 <= record.score <= 5):
                raise exceptions.ValidationError("The rating score must be between 1 and 5.")

    _sql_constraints = [
        ('unique_client_product_rating',
         'unique(partner_id, product_tmpl_id)',
         'A client can only rate a specific product once.')
    ]