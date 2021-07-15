#
#
#    Copyright © 2020; Brasil; IT Brasil; Todos os direitos reservados
#    Copyright © 2020; Brazil; IT Brasil; All rights reserved
#

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EnapEventoConvidado(models.Model):
    _name = 'enap.evento.convidado'
    _description = 'ENAP - Eventos (convidado)'
    _order = 'nome'
    _rec_name = 'nome'
    _inherit = ['image.mixin']

    evento_id = fields.Many2one(
        comodel_name ='enap.evento',
        string='ENAP - Convidado',
        required = True,
        ondelete ='cascade'
    )

    nome = fields.Char(
        string='Convidado',
        required=True,
        index=True,
    )

    cargo = fields.Char(
        string='Cargo',
        index=True,
    )

    minibiografia = fields.Text(
        string='Biografia',
        index=True,
    )

    url_perfil_profissional = fields.Char(
        string='Url do Perfil Profissional',
        index=True,
    )

    image_1920 = fields.Binary(
        string="Imagens",
        readonly=False,
    )







