#
#    Copyright © 2019–; Brasil; Taŭga Tecnologia; Todos os direitos reservados
#    Copyright © 2019–; Brazil; Taŭga Technology; All rights reserved
#

{
    'name': 'ENAP',
    'category': 'IT Brasil',
    'license': 'Other proprietary',
    'author': 'IT Brasil',
    'depends': ['base',],
    'qweb': [],
    'data': [
        'security/inherited_res_groups_data.xml',
        'security/inherited_ir_model_access_data.xml',
        'security/inherited_ir_model_access_data_formato.xml',
        'security/inherited_ir_model_access_data_publico_alvo.xml',
        'security/inherited_ir_model_access_data_eixo_tematico.xml',
        'security/inherited_ir_model_access_data_periodo.xml',
        'security/inherited_ir_model_access_data_convidado.xml',
        'security/inherited_ir_model_access_data_parceiro.xml',
        'security/inherited_ir_model_access_data_inscrito.xml',

        'data/enap_formato_data.xml',
        'data/enap_publico_alvo_data.xml',
        'data/enap_eixo_tematico_data.xml',

        'templates/assets_backend_template.xml',

        'views/enap_menu_administracao_view.xml',
        'views/administracao/enap_formato_view.xml',
        'views/administracao/enap_publico_alvo_view.xml',
        'views/administracao/enap_eixo_tematico_view.xml',
        'views/administracao/res_partner_view.xml',


        'views/enap_menu_evento_view.xml',
        'views/evento/enap_evento_parceiro_view.xml',
        'views/evento/enap_evento_periodo_view.xml',
        'views/evento/enap_evento_convidado_view.xml',
        'views/evento/enap_evento_convite_view.xml',
        'views/evento/enap_evento_ingresso_view.xml',
        'views/evento/enap_evento_view.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'external_dependencies': {'python': [],},
}
