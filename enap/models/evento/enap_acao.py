#
#
#    Copyright © 2020; Brasil; IT Brasil; Todos os direitos reservados
#    Copyright © 2020; Brazil; IT Brasil; All rights reserved
#

from typing import DefaultDict
from odoo import api, fields, models
from odoo.exceptions import ValidationError
from ...constantes import *


class EnapAcao(models.Model):
    _name = 'enap.acao'
    _description = 'ENAP - Tipo de ação'
    _order = 'titulo'
    _rec_name = 'titulo'
    _inherit = ['image.mixin']

    titulo = fields.Char(
        string='Nome do Evento',
        size=200,
        required=True,
    )

    tipo_acao = fields.Selection(
        selection=TIPO_ACAO,
        string='Tipo de ação',
        required=True,
    )

    descricao = fields.Char(
        string='Descrição',
        size=350,
        required=True,
    )

    codigo = fields.Char(
        string='Código',
    #    required=True,
    )

    formato_id = fields.Many2one(
        string='Formato',
        comodel_name='enap.formato',
        required=True,
        ondelete='restrict',
    )

    eixo_tematico_ids = fields.Many2many(
        string='Eixos Temáticos',
        comodel_name='enap.eixo.tematico',
        relation='enap_evento_eixo_tematico',
        column1='evento_id',
        column2='eixo_tematico_id',
        required=True,
        ondelete='restrict'
    )

    visibilidade = fields.Selection(
        selection=EVENTO_VISIBILIDADE,
        string='Visibilidade do evento',
        required=True,
    )

    modalidade = fields.Selection(
        selection=MODALIDADE,
        string='Modalidade',
        required=True,
    )

    link_gravacao = fields.Char(
        string='Link da Gravação',
    )

    local = fields.Char(
        string='Local'
    )

    fuso_horario = fields.Selection(
        string='Fuso horário',
        selection=FUSO_HORARIO,
        default='America/Sao_Paulo',
        required=True,
    )

    periodo_ids = fields.One2many(
        comodel_name='enap.acao.dt.realizacao',
        inverse_name='evento_id',
        string='Período de realização',
    )

    sobre = fields.Html(
        string='Sobre',
        help='Fale mais sobre o evento',
        sanitize=True,
        sanitize_tags=True,
        sanitize_attributes=True,
        sanitize_style=False,
        strip_style=False,
        strip_classes=False,
    )

    convidado_ids = fields.One2many(
        comodel_name='enap.evento.convidado',
        inverse_name='evento_id',
        string='Convidados',
    )

    publico_alvo_ids = fields.Many2many(
        string='Público-alvo',
        comodel_name='enap.publico.alvo',
        relation='enap_evento_publico_alvo',
        column1='evento_id',
        column2='publico_alvo_id',
        required=True,
        ondelete='restrict'
    )

    publico_alvo_para_quem = fields.Text(
        string='Para quem é este evento?',
    )

    parceiros_ids = fields.One2many( # ou apoiadores
        comodel_name='enap.evento.parceiro',
        inverse_name='evento_id',
        string='Parceiros',
    )

    image_1920 = fields.Binary(
        string="Imagens",
        readonly=False,
    )

    organizador_id = fields.Many2one(
        string='Organizador',
        comodel_name='res.partner',
    )

    organizador_email = fields.Char(
        string='E-mail do organizador',
        related='organizador_id.email',
        store=True,
    )

    organizador_coordenacao_geral = fields.Char(
        string='Coordenação geral do organizador',
        related='organizador_id.coordenacao_geral',
        store=True,
    )

    organizador_diretoria = fields.Char(
        string='Diretoria do organizador',
        related='organizador_id.diretoria',
        store=True,
    )

    link_evento = fields.Char( # ou link do "mata burro"
        string='Link landing page do evento',
    )

    state = fields.Selection(
        selection=STATE,
        string='Estado do evento',
    )

    ingresso_restricao = fields.Char(
        string='Restrição do evento',
    )

    ingresso_limite_vagas = fields.Integer(
        string='Limite de vagas do evento',
    )

    ingresso_data_inicial = fields.Datetime( # ou date
        string='Data inicial do ingresso',
    )

    ingresso_data_final = fields.Datetime( # ou date
        string='Data final do ingresso',
    )

    ingresso_ids = fields.One2many(
        string='Ingressos',
        comodel_name='enap.acao.ocorrencia',
        inverse_name='evento_id',
        domain=[('tipo','=',TIPO_INSCRICAO_INGRESSO)]
    )

    ingressos_confirmados = fields.Integer(
        string='Ingressos confirmados',
        compute='_compute_ingressos_confirmados',
    )

    convite_data_inicial = fields.Datetime(
        string='Data inicial do convite',
    )

    convite_data_final = fields.Datetime(
        string='Data final do convite',
    )

    convite_ids = fields.One2many(
        string='Convites',
        comodel_name='enap.acao.ocorrencia',
        inverse_name='evento_id',
        domain=[('tipo','=',TIPO_INSCRICAO_CONVITE)]
    )


    convites_confirmados = fields.Integer(
        string='Convites confirmados',
        compute='_compute_convites_confirmados',
    )

    data_inicial = fields.Datetime(
        string='Data inicial',
        compute='_compute_data_inicial_final',
        store=True,
    )

    data_final = fields.Datetime(
        string='Data final',
        compute='_compute_data_inicial_final',
        store=True,
    )

    progress = fields.Float(
        string='Ingressos', 
        compute='_compute_progress_ingressos'
    )

    curso_id = fields.Many2one(
        string='Cursos',
        comodel_name='enap.curso',
    )

    curso_disciplina_ids = fields.One2many(
        string='Disciplinas',
        comodel_name='enap.acao.curso.disciplina',
        # inverse_name='evento_id',
    )

    presenca_ids = fields.One2many(
        string='Presenças',
        comodel_name='enap.acao.presenca',
        # inverse_name='evento_id',
    )

    @api.depends('periodo_ids')
    def _compute_data_inicial_final(self):
        for evento in self:
            evento.data_inicial = False
            evento.data_final = False

            if not evento.periodo_ids:
                continue

            evento.data_inicial = evento.periodo_ids[0].data_hora_inicial
            evento.data_final = evento.periodo_ids[-1].data_hora_final

    @api.depends('convite_ids')
    def _compute_convites_confirmados(self):
        for evento in self:
            confirmados = 0
            for convite in evento.convite_ids:
                if convite.data_inscricao:
                    confirmados += 1
            evento.convites_confirmados = confirmados

    @api.depends('ingresso_ids')
    def _compute_ingressos_confirmados(self):
        for evento in self:
            confirmados = 0
            for ingresso in evento.ingresso_ids:
                if ingresso.data_inscricao:
                    confirmados += 1
            evento.ingressos_confirmados = confirmados

    @api.depends('convites_confirmados','ingressos_confirmados')
    def _compute_progress_ingressos(self):
        for evento in self:
            progress = 0
            progress += evento.convites_confirmados if evento.convites_confirmados > 0 else 0
            progress += evento.ingressos_confirmados if evento.ingressos_confirmados > 0 else 0
            if progress >= evento.ingresso_limite_vagas: 
                progress = 100 
            else:
                progress = (progress / evento.ingresso_limite_vagas)*100
            
            evento.progress = progress
