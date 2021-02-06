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
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "1. ¿Cuenta la empresa con plan de trabajo semanal/ quincenal/ mensual/ trimestral/ semestral/ anual?",
    )
    x_org2 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "2. ¿Cuenta o elabora la empresa presupuesto semanal/ quincenal/ mensual/ trimestral/ semestral/ anual?",
    )
    x_org3 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "3. ¿Cuenta la empresa con plan estratégico de desarrollo?",
    )
    x_org4 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "4. ¿Cuenta su empresa con un organigrama publicado en un lugar visible para sus trabajadores?",
    )
    x_org5 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "5. ¿Cuenta la empresa con un manual de procedimientos administrativos y contables?",
    )
    x_org6 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "6. ¿Los Socios(as) de la Empresa/ Organización/ Cooperativa, realizan periódicamente sus aportaciones obligatorias según sus estatutos?",
    )
    x_org7 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "7. ¿Los Socios(as) de la Empresa/ Organización/ Cooperativa, realizan periódicamente sus aportaciones obligatorias según sus estatutos?",
    )
    campo8 = fields.Selection(
        [
            ('no_aplica', 'no aplica')
        ], "hola"
    )