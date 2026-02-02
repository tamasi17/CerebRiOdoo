from odoo import models, fields, api


class EventEvent(models.Model):
    _inherit = 'event.event'

    proposal_status = fields.Selection([
        ('draft', 'Borrador'),
        ('proposed', 'Propuesto'),
        ('approved', 'Aprobado'),
        ('rejected', 'Rechazado')
    ], string='Estado de Propuesta', default='draft', tracking=True)

    def action_approve_proposal(self):
        """Aprueba la propuesta técnica de BCI."""
        self.write({'proposal_status': 'approved'})

    def action_reject_proposal(self):
        """Rechaza la propuesta de integración."""
        self.write({'proposal_status': 'rejected'})

    def action_set_to_proposed(self):
        self.write({'proposal_status': 'proposed'})