from odoo import models, fields

class ExoDispositivo(models.Model):
    _name = 'exo.dispositivo'
    _description = 'Exoesqueleto'

    name = fields.Char(string='Número de Serie', required=True)
    modelo = fields.Selection([
        ('pierna_completa', 'Pierna Completa'),
        ('rodilla', 'Módulo Rodilla'),
        ('cadera', 'Módulo Cadera')
    ], string='Modelo', default='pierna_completa')
    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('mantenimiento', 'En Mantenimiento'),
        ('uso', 'En Uso')
    ], string='Estado', default='disponible')