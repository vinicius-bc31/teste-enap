#
#
#    Copyright © 2020; Brasil; IT Brasil; Todos os direitos reservados
#    Copyright © 2020; Brazil; IT Brasil; All rights reserved
#

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EnapEventoParceiro(models.Model):
    _name = 'enap.evento.parceiro'
    _description = 'ENAP - Eventos (parceiro)'
    _order = 'nome'
    _rec_name = 'nome'
    _inherit = ['image.mixin']

    evento_id = fields.Many2one(
        comodel_name ='enap.evento',
        string='ENAP - Eventos',
        required = True,
        ondelete ='cascade',
    )

    nome = fields.Char(
        string='Parceiro',
        size=400,
        required=True,
        index=True,
    )

    image_1920 = fields.Binary(
        string="Imagens",
        readonly=False
    )







