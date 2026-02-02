from odoo import models, fields, api

class ExoSesion(models.Model):
    _name = 'exo.sesion'
    _description = 'Sesión de Rehabilitación'

    # Quitamos el readonly=True para que puedas editarlo
    name = fields.Char(
        string='Nombre de la Sesión',
        required=True,
        copy=False,
        default='Nueva Sesión'
    )

    paciente_id = fields.Many2one('exo.paciente', string='Paciente', required=True)
    dispositivo_id = fields.Many2one('exo.dispositivo', string='Exoesqueleto', required=True)
    fecha = fields.Datetime(string='Fecha y Hora', default=fields.Datetime.now)

    # Datos de la terapia
    duracion = fields.Integer(string='Duración (minutos)')

    # Cambiamos a Integer para que sea un valor numérico fácil de editar
    nivel_asistencia = fields.Integer(
        string='Nivel de Asistencia (%)',
        help="0% es sin ayuda, 100% es asistencia total del motor"
    )

    pasos_totales = fields.Integer(string='Pasos Realizados')
    observaciones = fields.Text(string='Observaciones')

    # ESTA ES LA MAGIA PARA EL TÍTULO AUTOMÁTICO
    @api.onchange('paciente_id', 'fecha')
    def _onchange_nombre_sesion(self):
        if self.paciente_id and self.fecha:
            # Formateamos la fecha para que sea legible (Día/Mes/Año)
            fecha_str = self.fecha.strftime('%d/%m/%Y %H:%M')
            self.name = f"Sesión: {self.paciente_id.name} - {fecha_str}"