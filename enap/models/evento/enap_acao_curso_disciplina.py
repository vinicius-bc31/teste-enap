#
#
#    Copyright © 2020; Brasil; IT Brasil; Todos os direitos reservados
#    Copyright © 2020; Brazil; IT Brasil; All rights reserved
#

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EnapAcaoCursoDisciplina(models.Model):
    _name = 'enap.acao.curso.disciplina'
    _description = 'ENAP - Ação (Curso Disciplina)'
    #_order = 'nome'
    #_rec_name = 'nome'
    #_inherit = ['image.mixin']

    acao_id = fields.Many2one(
        comodel_name ='enap.acao',
        string='Tipo de ação',
        #required = True,
    )

    nome_da_disciplina = fields.Char(
        string='Nome da disciplina',
        required=True,
    )








