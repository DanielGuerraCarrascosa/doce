# -*- coding: utf-8 -*-
# Part of Aselcis Consulting SL. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.one
    def asset_create(self):
        if self.asset_category_id:
            value = 0
            taxes = self.invoice_line_tax_ids.children_tax_ids if self.invoice_line_tax_ids.children_tax_ids else self.invoice_line_tax_ids
            for tax in taxes:
                if not tax.account_id and not tax.refund_account_id:
                    price_include = tax.price_include or tax._context.get(
                        'force_price_include')
                    if (tax.amount_type == 'percent' and not price_include) or (tax.amount_type == 'division' and price_include):
                        value += self.price_subtotal_signed * tax.amount / 100
                    if tax.amount_type == 'percent' and price_include:
                        value += self.price_subtotal_signed - \
                            (self.price_subtotal_signed / (1 + tax.amount / 100))
                    if tax.amount_type == 'division' and not price_include:
                        value += self.price_subtotal_signed / \
                            (1 - tax.amount / 100) - self.price_subtotal_signed
                    if tax.amount_type == 'fixed':
                        value += tax.amount * self.quantity
            value = value + self.price_subtotal_signed
            vals = {
                'name': self.name,
                'code': self.invoice_id.number or False,
                'category_id': self.asset_category_id.id,
                'value': value if value != 0 else self.price_subtotal_signed,
                'partner_id': self.invoice_id.partner_id.id,
                'company_id': self.invoice_id.company_id.id,
                'currency_id': self.invoice_id.company_currency_id.id,
                'date': self.invoice_id.date_invoice,
                'invoice_id': self.invoice_id.id,
            }
            changed_vals = self.env['account.asset.asset'].onchange_category_id_values(
                vals['category_id'])
            vals.update(changed_vals['value'])
            asset = self.env['account.asset.asset'].create(vals)
            if self.asset_category_id.open_asset:
                asset.validate()
        return True
