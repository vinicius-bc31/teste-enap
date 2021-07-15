#
#
#    Copyright © 2020; Brasil; IT Brasil; Todos os direitos reservados
#    Copyright © 2020; Brazil; IT Brasil; All rights reserved
#

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EnapAcaoPresenca(models.Model):
    _name = 'enap.acao.presenca'
    _description = 'ENAP - Ação (presença)'
    #_order = 'nome'
    #_rec_name = 'nome'
    #_inherit = ['image.mixin']

    acao_id = fields.Many2one(
        comodel_name ='enap.acao',
        string='ENAP - Ação',
        required = True,
    )

    partner_id = fields.Many2one(
        comodel_name ='res.partner',
        required = True,
    )

    ocorrencia_id = fields.Many2one(
        comodel_name ='enap.acao.ocorrencia',
        required = True,
    )

    periodo_id = fields.Many2one(
        comodel_name ='enap.acao.dt.realizacao',
        required = True,
    )

    data_hora_chegada = fields.Datetime(
        string = 'Check-in',
    )

    data_hora_saida = fields.Datetime(
        string = 'Check-out',
    )

    







