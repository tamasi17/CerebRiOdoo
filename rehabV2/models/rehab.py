from odoo import models, fields

class Rehab(models.Model):
    _name = 'rehab'  # Este es el nombre técnico del modelo
    _description = 'Registro de Rehabilitación'

    # Campo obligatorio para que los registros tengan un título o nombre
    name = fields.Char(string="Nombre del Paciente", required=True)

    injury_level = fields.Selection([
        ('mild', 'Leve'),
        ('moderate', 'Moderada'),
        ('severe', 'Severa')
    ], string="Nivel de Lesión")

    rehab_start_date = fields.Date(string="Inicio de Rehabilitación")

    # Un campo de texto para notas clínicas
    notes = fields.Text(string="Observaciones")