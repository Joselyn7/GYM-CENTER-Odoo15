from odoo import fields, models


class TopSellingProduct(models.Model):
    _name = 'top.selling.product'
    _description = 'Las máquinas más adquiridas'
    _rec_name = 'start_date'

    cod = fields.Char(string='Código', size=50, required=False)
    res_partner_id = fields.Many2one(string='Persona que reserva', comodel_name='gym.center.user', required=False)
    installation_id = fields.Many2one(string='Máquina', comodel_name='gym.machine', required=False)
    total = fields.Float(string="Total", size=10, required=False)
    start_date = fields.Datetime(string='Fecha de inicio del alquiler', required=False)
    end_date = fields.Datetime(string='Fecha de fin del alquiler', required=False)
    status = fields.Selection(selection=[("pagado", "Pagado"), ("sin cancelar", "Sin Cancelar")])

