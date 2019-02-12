from odoo import models, fields, api


class Sith(models.Model):
    _name = 'modulo_final.sith'
    nombre = fields.Char(string="Nombre")
    especie = fields.Many2one('modulo_final.especie', string="Especie")
    rabia = fields.Integer()
    afin_oscu = fields.Integer(string="Afinidad con la Oscuridad")
    color_sable = fields.Selection([
        ('rojo1', "Rojo"),
        ('rojo2', "Rojo Oscuro"),
    ])
    mandoble = fields.Boolean(string="Usa mandoble", default=False)

    @api.onchange('rabia')
    def _nivel_afin_oscu(self):
        self.afin_oscu = self.rabia * 2

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
