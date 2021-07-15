#
#
#    Copyright © 2020; Brasil; IT Brasil; Todos os direitos reservados
#    Copyright © 2020; Brazil; IT Brasil; All rights reserved
#

from datetime import datetime
from pytz import timezone, UTC
from math import floor

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

from ...constantes import *


class EnapAcaoOcorrencia(models.Model):
    _name = 'enap.acao.ocorrencia'
    _description = 'ENAP - Ocorrências de ações'
    #_order = 'nome'
    #_rec_name = 'descricao'
    #_inherit = ['mail.thread', 'mail.activity.mixin']

    acao_id = fields.Many2one(
        comodel_name='enap.acao',
        string='ENAP - Ação',
        required=True,
        ondelete='cascade',
    )

    tipo = fields.Selection(
        selection=TIPO_INSCRICAO,
        string='Tipo',
    )

    partner_id = fields.Many2one( 
        string='Partner',
        comodel_name='res.partner',
        required=True,
    )

    periodo_ids = fields.Many2one(
        comodel_name='enap.acao.dt.realizacao',
        inverse_name='evento_id',
        string='Período de realização',
    )

    nome = fields.Char( 
        string='Nome completo',
        related='partner_id.name',
        readonly=False,
        store=True,
    )

    email = fields.Char(
        string='E-mail',
        related='partner_id.email',
        readonly=False,
        store=True,
    )

    cpf = fields.Char(
        string='CPF',
        related='partner_id.cpf',
        readonly=False,
        store=True,
    )

    esfera_governo = fields.Char(
        string='Esfera de governo',
        related='partner_id.esfera_governo',
        readonly=False,
        store=True,
    )

    esfera_poder = fields.Char(
        string='Esfera de poder',
        related='partner_id.esfera_poder',
        readonly=False,
        store=True,
    )

    orgao_lotacao = fields.Char(
        string='Orgão de lotação',
        related='partner_id.orgao_lotacao',
        readonly=False,
        store=True,
    )

    cargo = fields.Char(
        string='Cargo',
        related='partner_id.cargo',
        readonly=False,
        store=True,
    )

    acessibilidade_audiodescricao = fields.Boolean(
        string='Audiodescrição',
        related='partner_id.acessibilidade_audiodescricao',
        readonly=False,
        store=True,
    )

    acessibilidade_legendagem_simultanea = fields.Boolean(
        string='legendagem simultânea',
        related='partner_id.acessibilidade_legendagem_simultanea',
        readonly=False,
        store=True,
    )

    acessibilidade_libras = fields.Boolean(
        string='Libras',
        related='partner_id.acessibilidade_libras',
        readonly=False,
        store=True,
    )

    data_inscricao = fields.Date(
        string='Data de inscrição (ou convite aceito)',
    )
