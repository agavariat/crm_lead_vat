# Copyright 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class Lead(models.Model):
    _inherit = "crm.lead"

    vat = fields.Char(
        string="TIN",
        help="Tax Identification Number. The first 2 characters are the "
             "country code.")

    x_datos1 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "ACEPTA ENTREGARLE A UNIMINUTO LOS DATOS GENERALES SUYOS Y DEL MICRONEGOCIO CON FINES ACADÉMICOS",
    )
    @api.multi
    def _create_lead_partner(self):
        """Add VAT to partner."""
        return (super(Lead, self.with_context(default_vat=self.vat))
                ._create_lead_partner())

    def _onchange_partner_id_values(self, partner_id):
        """Recover VAT from partner if available."""
        result = super(Lead, self)._onchange_partner_id_values(partner_id)
        if not partner_id:
            return result
        partner = self.env['res.partner'].browse(partner_id)
        if partner.vat:
            result['vat'] = partner.vat
        return result
