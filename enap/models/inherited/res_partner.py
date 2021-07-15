#
#
#    Copyright © 2020; Brasil; IT Brasil; Todos os direitos reservados
#    Copyright © 2020; Brazil; IT Brasil; All rights reserved
#

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from ...constantes import *


class ResPartner(models.Model):
    _inherit = 'res.partner'

    nome_social = fields.Char(
        string='Nome social'
    )

    cpf = fields.Char(
        string='CPF',
        size=14,
    )

    esfera_governo = fields.Char(
        string='Esfera de governo',
    )

    esfera_poder = fields.Char(
        string='Esfera de poder',
    )

    orgao_lotacao = fields.Char(
        string='Orgão de lotação',
    )

    cargo = fields.Char(
        string='Cargo'
    )

    acessibilidade_audiodescricao = fields.Boolean(
        string='Audiodescrição'
    )

    acessibilidade_legendagem_simultanea = fields.Boolean(
        string='Legendagem Simultânea'
    )

    acessibilidade_libras = fields.Boolean(
        string='Libras'
    )

    is_aluno = fields.Boolean( # tipo de cadastro
        string='É aluno'
    )

    is_professor = fields.Boolean( # tipo de cadastro
        string='É professor'
    )

    is_coordenador = fields.Boolean( # tipo de cadastro
        string='É coordenador'
    )
    
    enap_acao_evento_ids = fields.One2many(
        string='Eventos relacionados',
        comodel_name='enap.acao.partner.id',
        inverse_field_name='', 
        domain=[('tipo','=',TIPO_ACAO_EVENTO)]
    )

    enap_acao_curso_ids = fields.One2many(
        string='Cursos relacionados',
        comodel_name='enap.acao.partner.id',
        inverse_field_name='', 
        domain=[('tipo','=',TIPO_ACAO_CURSO)]
    )

    # validacao_cpf




