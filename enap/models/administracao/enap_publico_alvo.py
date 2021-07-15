#
#
#    Copyright © 2020; Brasil; IT Brasil; Todos os direitos reservados
#    Copyright © 2020; Brazil; IT Brasil; All rights reserved
#

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EnapPublicoAlvo(models.Model):
    _name = 'enap.publico.alvo'
    _description = 'ENAP - Público Alvo'
    _order = 'nome'
    _rec_name = 'nome'

    nome = fields.Char(
        string='Público alvo',
        size=400,
        required=True,
        index=True,
    )
