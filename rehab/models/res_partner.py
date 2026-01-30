from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'  # Nombre técnico del modelo original

    # Añadimos un campo nuevo que no existe en el estándar
    injury_level = fields.Selection([
        ('mild', 'Leve'),
        ('moderate', 'Moderada'),
        ('severe', 'Severa')
    ], string="Nivel de Lesión")

    rehab_start_date = fields.Date(string="Inicio de Rehabilitación")