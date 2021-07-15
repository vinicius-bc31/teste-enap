#
#
#    Copyright © 2020; Brasil; IT Brasil; Todos os direitos reservados
#    Copyright © 2020; Brazil; IT Brasil; All rights reserved
#

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EnapEixoTematico(models.Model):
    _name = 'enap.eixo.tematico'
    _description = 'ENAP - Eixos Temáticos'
    _order = 'nome'
    _rec_name = 'nome'
    #_inherit = ['mail.thread', 'mail.activity.mixin']

    nome = fields.Char(
        string='Eixo temático',
        size=400,
        required=True,
        index=True,
    )
