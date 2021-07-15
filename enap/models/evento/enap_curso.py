#
#
#    Copyright © 2020; Brasil; IT Brasil; Todos os direitos reservados
#    Copyright © 2020; Brazil; IT Brasil; All rights reserved
#

from constantes.enap_cursos import CURSO, CURSOS
from typing import DefaultDict
from odoo import api, fields, models
from odoo.exceptions import ValidationError
from ...constantes import *


class EnapCurso(models.Model):
    _name = 'enap.curso'
    _description = 'ENAP - Curso'
    #_order = 'titulo'
    #_rec_name = 'titulo'
    #_inherit = ['image.mixin']

    nome = fields.Char(
        string='Nome do Curso',
        size=200,
        required=True,
    )

    tipo = fields.Selection(
        selection=CURSO,
        string='Curso',
        #required=True,
    )

    disciplina = fields.One2many(
        comodel_name='enap.curso.disciplina',
        inverse_name='curso_id',
        string='Disciplina',
    )
