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


class EnapAcaoDtRealizacao(models.Model):
    _name = 'enap.acao.dt.realizacao'
    _description = 'ENAP - data de realização da ação'
    #_order = 'nome'
    _rec_name = 'descricao'
    #_inherit = ['mail.thread', 'mail.activity.mixin']

    evento_id = fields.Many2one(
        comodel_name='enap.acao',
        string='ENAP - Ação',
        required=True,
        ondelete='cascade',
    )

    nome = fields.Char( # ?
        string='Nome do realização',
    )

    modalidade = fields.Selection( # ?
        selection=MODALIDADE,
        string='Modalidade',
        related='evento_id.modalidade',
    )

    formato_id = fields.Many2one(
        string='Formato',
        comodel_name='enap.formato',
        ondelete='restrict',
        related='evento_id.formato_id'
    )

    descricao = fields.Char(
        string='Descrição',
        size=120,
        compute="_compute_nome",
    )

    data = fields.Date(
        string='Data',
        default=fields.Datetime.now,
    )

    hora_inicial = fields.Float(
        string='Hora inicial',
    )

    hora_final = fields.Float(
        string='Hora final',
    )

    fuso_horario = fields.Selection(
        string='Fuso horário',
        selection=FUSO_HORARIO,
        related='evento_id.fuso_horario',
    )

    data_hora_inicial = fields.Datetime(
        string='Data hora inicial',
        compute='_computer_datahora',
        store=True,
    )

    data_hora_final= fields.Datetime(
        string='Data hora final',
        compute='_computer_datahora',
        store=True,
    )

    @api.depends('evento_id', 'data')
    def _compute_nome(self):
        for item in self:
            nome=''
            if item.evento_id:
                if item.evento_id.titulo:
                    nome += item.evento_id.titulo
                if item.evento_id.modalidade:
                    nome += '\n' + item.evento_id.modalidade
                if item.evento_id.formato_id:
                    nome += '\n' + item.evento_id.formato_id.name_get()[0][1]
            # if item.data:
            #     nome+= ' - '
            #     nome+= item.data.strftime('%d/%m/%Y')
            item.descricao=nome

    @api.depends('data', 'hora_inicial', 'hora_final','fuso_horario')
    def _computer_datahora(self):
        for item in self:
            item.data_hora_inicial = False
            item.data_hora_final = False

            if (not item.hora_inicial) or (not item.hora_final):
                continue

            if item.hora_inicial > item.hora_final:
                raise ValidationError("Hora inicial maior que hora final!")

            fh = timezone(item.fuso_horario or 'America/Sao_Paulo')

            data_inicial = datetime.fromisoformat(f'{item.data} {float_to_time(item.hora_inicial)}')
            data_final = datetime.fromisoformat(f'{item.data} {float_to_time(item.hora_final)}')

            data_inicial = fh.localize(data_inicial)
            data_final = fh.localize(data_final)

            data_inicial = UTC.normalize(data_inicial)
            data_final = UTC.normalize(data_final)

            item.data_hora_inicial = str(data_inicial)[:19]
            item.data_hora_final = str(data_final)[:19]
