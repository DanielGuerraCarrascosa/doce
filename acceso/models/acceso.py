# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Acceso(models.Model):

    _inherit = 'website'
    
    #usuarioAcceso = fields.Char(string='Title', required=True)
    #passwordAcceso = fields.Text(string='Description')
    #checkPrivacidadAcceso = fields.Boolean(string='Check Privacidad', default=False)
    
    #@api.multi
    #def WS_acceso_portalfarma(self):
        