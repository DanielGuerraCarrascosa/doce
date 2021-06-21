# -*- coding: utf-8 -*-
import logging
from odoo import http
from odoo.http import request
from odoo.exceptions import UserError
 

_logger = logging.getLogger(__name__)
 

class ChangePasswdExternal(http.Controller):
    _inerit = 'res.users'
    @http.route('/reseteo', auth='none', website=True)
    def reset_password(self, **kw):
        db = 'danielguerracarrascosa-doce-main-2743393'
        login = 'v.fernandez@ampsoftware.com'
        password = 'toor1'
        request.session.authenticate(db, login, password)
        emailRecibido = request.params['email']
        user = http.request.env['res.users'].search([('email', '=', emailRecibido)])
        print("hola estoy en la funcion reset_password por i1nherit")
        print(user)
        print(type(user))
        if len(user) != 1:
            return "no existe el correo introducido"
        else:
            print("usuario existente en BDD")
            return user.action_reset_password()
 

 

    def action_reset_password(self):
        """ create signup token for each user, and send their signup url by email """
        # prepare reset password signup
        print("Llego a la funcion action_reset_password")
        create_mode = bool(self.env.context.get('create_user'))
 

        # no time limit for initial invitation, only for reset password
        expiration = False if create_mode else now(days=+1)
 

        self.mapped('partner_id').signup_prepare(signup_type="reset", expiration=expiration)
 

        # send email to users with their signup url
        template = False
        if create_mode:
            try:
                template = self.env.ref('auth_signup.set_password_email', raise_if_not_found=False)
            except ValueError:
                pass
        if not template:
            template = self.env.ref('auth_signup.reset_password_email')
        assert template._name == 'mail.template'
 

        template_values = {
            'email_to': '${object.email|safe}',
            'email_cc': False,
            'auto_delete': True,
            'partner_to': False,
            'scheduled_date': False,
        }
        template.write(template_values)
 

        for user in self:
            if not user.email:
                raise UserError(_("Cannot send email: user %s has no email address.") % user.name)
            with self.env.cr.savepoint():
                template.with_context(lang=user.lang).send_mail(user.id, force_send=True, raise_exception=True)
            _logger.info("Password reset email sent for user <%s> to <%s>", user.login, user.email)