# -*- coding: utf-8 -*-
# Part of Aselcis. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class CrossoveredBudgetLines(models.Model):
    _inherit = "crossovered.budget.lines"

    analytic_group_id = fields.Many2one(store=True)
    