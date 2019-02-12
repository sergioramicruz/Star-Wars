from odoo import models, fields, api


class Planeta(models.Model):
    _name = 'modulo_final.planeta'
    name = fields.Char(string="Planeta")
    distancia = fields.Integer()
    destruido = fields.Boolean(default=False)
    fecha_destruccion = fields.Date()
