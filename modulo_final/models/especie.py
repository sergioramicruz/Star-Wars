from odoo import models, fields, api


class Especie(models.Model):
    _name = 'modulo_final.especie'
    name = fields.Char(string="Especie")
    image = fields.Binary("Image", help="Selecciona imagen aqui")

