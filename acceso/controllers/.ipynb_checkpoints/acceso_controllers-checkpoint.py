# -*- coding: utf-8 -*-
import base64
import hashlib

from odoo import http
from odoo.http import request
from Crypto.Cipher import DES3
from Crypto import Random

class Acceso(http.Controller):
    @http.route('/acceso_desde_portalfarma', auth='public', website=True)
    def pintar_pag_acceso(self, **kw):
        return http.request.render('acceso.acceso_desde_portalfarma',{})
    
    @http.route('/acceso_desde_portalfarma_ko', auth='public', website=True)
    def acceso_ko(self, **kw):
        
        return http.request.render('acceso.acceso_desde_portalfarma_ko',{})
    
    @http.route('/acceso_desde_portalfarma_ok', auth='public', website=True)
    def acceso_ok(self, **kw):
        
        userDNI = request.params['usd']
        userPass = request.params['userPass']
        
        
        db = '(danielguerracarrascosa-doce-main-2743393'
        login = 'admin'
        password = 'admin'
        request.session.authenticate(db, login, password)
        
        
        user = http.request.env['res.users'].search([('login', '=', userDNI)])
        id_user = user.id
        
        user = http.request.env['res.users'].browse(id_user)
        user.password = userPass
        http.request.env.cr.commit()
        
        return http.request.render('acceso.cuenta_recuperada_portalfarma',{'dni':userDNI})
    
    @http.route('/decodifica', auth='public', website=True)
    def decodifica(self, **kw):
        """ codificar base64 (import base64)
        message = "Texto o cadena a codificar"
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        return(base64_message)
        """
        
        """ decodificar base64 (import haslib)
        base64_message = 'UHl0aG9uIGlzIGZ1bg=='
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')

        return(message)
        """
        
        """ pasar md5 
        text = "Texto o cadena a codificar"

        hash_object = hashlib.md5(text.encode())
        md5_hash = hash_object.hexdigest()

        return(md5_hash)
        """
        
        
    
        """ codificar tripleDes (`pip install pycrypto` / import DES3 y Random) """
        
        key = 'Sixteen byte key' #16 or 24 bytes long
        iv = '10100110'
        
        """
        cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)
        plaintext = 'sona si latine loqueri  ' # multiplo de 8
        encrypted_text = cipher_encrypt.encrypt(plaintext)
        encrypted_text = base64.b64encode(encrypted_text)
        
        return(encrypted_text)
        """
        
        
        """ decodificar tripleDes """
        
        
        cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv)
        textoRecibido = '2TB084elRCMKpXHQytk7WJ2nqlqXYqWj'
        textoRecibido = base64.b64decode(textoRecibido)
        er = cipher_decrypt.decrypt(textoRecibido)
       
    
        a = [27, 9, 45, 27, 0, 72, 171, 54]
        b = ''.join(map(chr, a))
        
        return (b)