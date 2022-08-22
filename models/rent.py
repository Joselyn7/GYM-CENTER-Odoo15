from odoo import fields, models


class Rent(models.Model):
    _name = 'gym.center.rent'
    _description = 'Alquiler'
    _rec_name = 'start_date'

    cod = fields.Char(string='Código', size=50, required=True)
    res_partner_id = fields.Many2one(string='Persona que reserva', comodel_name='gym.center.user', required=True)
    installation_id = fields.Many2one(string='Máquina', comodel_name='gym.machine', required=True)
    total = fields.Float(string="Total", size=10, required=True)
    start_date = fields.Datetime(string='Fecha de inicio del alquiler', required=True)
    end_date = fields.Datetime(string='Fecha de fin del alquiler', required=True)
    status = fields.Selection(selection=[("pagado", "Pagado"), ("sin cancelar", "Sin Cancelar")])

