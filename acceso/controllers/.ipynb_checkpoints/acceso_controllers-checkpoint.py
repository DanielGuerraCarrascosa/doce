# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Acceso(http.Controller):
    @http.route('/acceso_desde_portalfarma', auth='public', website=True)
    def pintar_pag_acceso(self, **kw):
        return http.request.render('acceso.acceso_desde_portalfarma',{})
    
    @http.route('/acceso_desde_portalfarma_ko', auth='public', website=True)
    def acceso_ko(self, **kw):
        
        return http.request.render('acceso.acceso_desde_portalfarma_ko',{})
    
    @http.route('/acceso_desde_portalfarma_ok', auth='public', website=True)
    def acceso_ok(self, **kw):
        
        return http.request.render('acceso.cuenta_recuperada_portalfarma',{})