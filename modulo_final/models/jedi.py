from odoo import models, fields, api


class Jedi(models.Model):
    _name = 'modulo_final.jedi'
    nombre = fields.Char(string="Nombre")
    especie = fields.Many2one('modulo_final.especie', string="Especie")
    color_sable = fields.Selection([
        ('azul', "Azul"),
        ('verde', "Verde"),
        ('morado', "Morado"),
    ])
    ultima_vista = fields.Date()
    planeta_id = fields.Many2one('modulo_final.planeta', string="Planeta")
    midiclorianos = fields.Integer(string="N midiclorianos")
    nivel = fields.Char(string="Nivel", compute='_calc_nivel')
    sith_id = fields.Many2one('modulo_final.sith', string="Sith que le persiguen")

    @api.depends('midiclorianos')
    def _calc_nivel(self):
        for r in self:
            if r.midiclorianos < 100:
                r.nivel = "Padawan"
            elif r.midiclorianos > 100 and r.midiclorianos < 1000:
                r.nivel = "Caballero Jedi"
            else:
                r.nivel = "Consejero Jedi"

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
