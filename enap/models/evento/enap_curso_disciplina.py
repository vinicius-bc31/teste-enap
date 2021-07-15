#
#
#    Copyright © 2020; Brasil; IT Brasil; Todos os direitos reservados
#    Copyright © 2020; Brazil; IT Brasil; All rights reserved
#

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EnapCursoDisciplina(models.Model):
    _name = 'enap.curso.disciplina'
    _description = 'ENAP - Curso Disciplina'
    #_order = 'nome'
    #_rec_name = 'nome'
    #_inherit = ['image.mixin']

    curso_id = fields.Many2one(
        comodel_name ='enap.curso',
        string='Tipo de curso',
        #required = True,
    )

    nome = fields.Char(
        string='Nome da disciplina',
        required=True,
    )








