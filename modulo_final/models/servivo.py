from odoo import models, fields, api


class Servivo(models.Model):
    _name = 'modulo_final.servivo'
    especie_id = fields.Many2one('modulo_final.especie', string="Especie")
