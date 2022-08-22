# -*- coding: utf-8 -*-

from odoo import models, fields


class Installation(models.Model):
    _name = "gym.center.installation"
    _description = "Maquinas del Negocio"

    cod = fields.Char(string='Código', size=50, required=False)
    name = fields.Char(string='Nombre', size=50, required=True)
    brand = fields.Char(string='Marca', size=50, required=True)
    price = fields.Float(string="Precio", size=10, required=True)
    location = fields.Char(string='Ubicación', size=100)
    status = fields.Selection(selection=[("disponible", "Disponible"), ("no disponible", "No Disponible")])
    quantity = fields.Integer(string="Cantidad", required=True)
