# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Acceso(http.Controller):
    @http.route('/acceso_desde_portalfarma', auth='public', website=True)
    def pintar_pag_acceso(self, **kw):
        return http.request.render('acceso.acceso_desde_portalfarma',{})
    