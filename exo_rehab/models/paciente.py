from odoo import models, fields

class ExoPaciente(models.Model):
    _name = 'exo.paciente'
    _description = 'Paciente de Rehabilitación'

    name = fields.Char(string='Nombre Completo', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    historial = fields.Text(string='Historial Clínico')
    telefono = fields.Char(string='Teléfono')