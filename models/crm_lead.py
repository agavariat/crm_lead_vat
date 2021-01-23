# Copyright 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, exceptions


class Lead(models.Model):
    _inherit = "crm.lead"

    vat = fields.Char(
        string="TIN",
        help="Tax Identification Number. The first 2 characters are the "
             "country code.")

    x_org1 = fields.Selection(
        [
            ('52', 'No Aplica'),
            ('50', 'Si'),
            ('53', 'En Proceso'),
            ('51', 'No'),
        ], "¿Cuenta la empresa con plan de trabajo semanal/ quincenal/ mensual/ trimestral/ semestral/ anual?",
    )
    x_org2 = fields.Selection(
        [
            ('52', 'No Aplica'),
            ('50', 'Si'),
            ('53', 'En Proceso'),
            ('51', 'No'),
        ], "¿Cuenta la empresa con plan de trabajo semanal/ quincenal/ mensual/ trimestral/ semestral/ anual?",
    )
    
