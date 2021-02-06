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
    x_org8 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "8. ¿Lleva los registros y controles correspondientes en los Libros de Entradas o Ingresos ( Ventas)?",
    )
    x_org9 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "9. ¿Lleva los registros y controles correspondientes en los Libros de Salidas o Egresos (Compras)?",
    )
    x_org10 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "10. ¿Lleva control y registro de caja menor?",
    )
    x_org11 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "11. ¿Lleva el registro y control en el Libro Auxiliar de Cuentas por Cobrar?",
    )
    x_org12 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "12. ¿Lleva el registro y control en el Libro Auxiliar de Cuentas por Pagar?",
    ) 
    x_org13= fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "13. ¿Lleva el registro y control en el Libro Auxiliar de Caja, Bancos?",
    ) 
    x_org14 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "14. ¿Elabora Conciliaciones Bancarias?",
    ) 
    x_org15 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "15. ¿Lleva libro de inventario y balances de la empresa?",
    )
    x_org16 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "16. ¿La empresa elabora planillas para el pago de sus trabajadores?",
    )
    x_org17 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "17. ¿ Elabora los Estados Financieros: Estado de Resultados y Balance General?",
    )
    x_org18 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "18. ¿Lleva el control del Flujo de Efectivo de su empresa (flujo de caja)?",
    ) 
    x_org19= fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "19. ¿Cuenta con un Sistema Contable (Manual o Automatizado)?",
    ) 
    x_org20 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "20. ¿Ha contrado un contador colegiado para el manejo de su contabilidad?",
    ) 
    x_org21 = fields.Selection(
        [
            ('0', 'No Aplica'),
            ('1', 'Si'),
            ('2', 'En Proceso'),
            ('3', 'No'),
        ], "21. ¿Realizan procesos de auditoría interna/ externa, ambas en la empresa?",
    )

