# -*- coding: utf-8 -*-

from odoo import models, fields


class User(models.Model):
    _name = "gym.center.user"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Usuarios del Gym"

    name = fields.Char(string='Nombre', size=50, required=True)
    lastname = fields.Char(string='Apellidos', size=50, required=True)
    dni = fields.Char(string='DNI', size=50, required=True)
    location = fields.Char(string='Ubicación', size=100, required=True)
    phone_number = fields.Char(string='Teléfono de contacto', size=64, required=True)
    email = fields.Char(string='Email de contacto', size=240, required=True)
    coupon_code = fields.Char(string='Código de Alta', size=12, required=True)
    status = fields.Selection(selection=[("activo", "Activo"), ("no Activo", "No Activo")])
    image = fields.Binary(string="Image", attachment=True)
    gender = fields.Selection(selection=[
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
    ], string="Género")
