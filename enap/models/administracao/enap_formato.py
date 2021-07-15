#
#
#    Copyright © 2020; Brasil; IT Brasil; Todos os direitos reservados
#    Copyright © 2020; Brazil; IT Brasil; All rights reserved
#

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EnapFormato(models.Model):
    _name = 'enap.formato'
    _description = 'ENAP - Formatos de evento'
    _order = 'nome'
    _rec_name = 'nome'
    #_inherit = ['mail.thread', 'mail.activity.mixin']

    nome = fields.Char(
        string='Formato',
        size=400,
        required=True,
        index=True,
    )
