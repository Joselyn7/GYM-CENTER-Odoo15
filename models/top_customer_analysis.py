from odoo import fields, models
from odoo import tools


class TopCustomerAnalysis(models.Model):
    _name = 'top.customer.analysis'
    _description = 'Top de los mejores clientes'
    _rec_name = 'start_date'

    cod = fields.Char(string='Código', size=50, required=False)
    res_partner_id = fields.Many2one(string='Persona que reserva', comodel_name='gym.center.user', required=False)
    installation_id = fields.Many2one(string='Máquina', comodel_name='gym.machine', required=False)
    total = fields.Float(string="Total", size=10, required=False)
    start_date = fields.Datetime(string='Fecha de inicio del alquiler', required=False)
    end_date = fields.Datetime(string='Fecha de fin del alquiler', required=False)
    status = fields.Selection(selection=[("pagado", "Pagado"), ("sin cancelar", "Sin Cancelar")])


# def init(self):
#     tools.drop_view_if_exists(self.env.cr, 'top_customer_analysis')
#     self.env.cr.execute("""
#              CREATE OR REPLACE VIEW top_customer_analysis AS(
#                  SELECT
#                      row_number() OVER () AS id,
#                      SELECT
#                             c.id as res_partner_id
#                       FROM gym.center.user c
#                       LEFT JOIN machine pr
#                       ON (c.id = pr.product_id)
#
#              )""")
