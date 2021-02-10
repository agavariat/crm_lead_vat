# Copyright 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, exceptions


class Lead(models.Model):
    _inherit = "crm.lead"

    vat = fields.Char(
        string="TIN",
        help="Tax Identification Number. The first 2 characters are the "
             "country code.")

#Organización y Administración (15%)
    x_org1 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "1. ¿Cuenta la empresa con plan de trabajo semanal/ quincenal/ mensual/ trimestral/ semestral/ anual?",
        help="Plan de Trabajo: 1 (No lo tiene), 2 (Está en proceso/ en elaboración), 3 (Si, lo tiene y está en ejecución).",
    )
    x_org2 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "2. ¿Cuenta o elabora la empresa presupuesto semanal/ quincenal/ mensual/ trimestral/ semestral/ anual?",
        help="Presupuesto: 1 (No lo tiene), 2 (Está en proceso/ en elaboración), 3 (Si, lo tiene y está en ejecución).  "
    )
    x_org3 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "3. ¿Cuenta la empresa con plan estratégico de desarrollo?",
        help="Plan Estratégico: 1 (No lo tiene), 2 (Está en proceso/elaboración), 3 (Si, lo tiene y está en ejecución)"
    )
    x_org4 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "4. ¿Cuenta su empresa con un organigrama publicado en un lugar visible para sus trabajadores?",
        help="Organigrama: 1 (No lo tiene), 2 (Está en proceso/ en elaboración), 3 (Si, lo tiene y es visible y aplicado)"
    )
    x_org5 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "5. ¿Cuenta la empresa con un manual de procedimientos administrativos y contables?",
        help="Manual de Procedimientos Administrativos y Contables: 1 (No lo tiene), 2 (Está en proceso/ en elaboración), 3 (Si, lo tiene y lo usa cotidianamente)"
    ) 
    x_org6 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "6. ¿Los Socios(as) de la Empresa/ Organización/ Cooperativa, realizan periódicamente sus aportaciones obligatorias según sus estatutos?",
        help="Control de Aportaciones: 0 (No Aplica), 1 (No, no lo hacen), 2 (Está en proceso, unos lo hacen otros no, hay incumplimiento parcial), 3 (Si, lo hacen los socios(as) periódica y puntualmente de conformidad a sus Estatutos y se refleja en el libro de aportaciones)"
    ) 
    x_org7 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "7. ¿Los Socios(as) de la Empresa/ Organización/ Cooperativa, realizan periódicamente sus aportaciones obligatorias según sus estatutos?",
        help="Relación y desarrollo de proveedores: 0 (No Aplica), 1 (No, no ven necesidad de ningún tipo de mejoramiento en la colaboración con proveedores), 2 (Está en proceso, Ven la necesidad de evolucionar y de tomar pasos internos para la colaboración con proveedores ), 3 (Si, desarrollan capacidades y colaboración con proveedores en ciertas áeas)"
    ) 

    x_org8 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "8. ¿Lleva los registros y controles correspondientes en los Libros de Entradas o Ingresos ( Ventas)?",
        help="Libro Auxiliar de Ingresos: 1 (No lo tiene), 2 (Está en proceso de adopción), 3 (Si, lo tiene y lo usa cotidianamente)."
    )
    x_org9 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "9. ¿Lleva los registros y controles correspondientes en los Libros de Salidas o Egresos (Compras)?",
        help="Libro Auxiliar de Egresos: 1 (No lo tiene), 2 (Está en proceso de adopción), 3 (Si, lo tiene y lo usa cotidianamente)."
    )
    x_org10 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "10. ¿Lleva control y registro de caja menor?",
        help="Control de Caja Chica: 1 (No la tiene), 2 (Está en proceso de adopción), 3 (Si, lo tiene y la usa cotidianamente)"
    )
    x_org11 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "11. ¿Lleva el registro y control en el Libro Auxiliar de Cuentas por Cobrar?",
        help="Libro de Cuentas por Cobrar: 1 (No lo tiene), 2 (Está en proceso de adopción), 3 (Si, lo tiene y la usa cotidianamente)"
    )
    x_org12 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "12. ¿Lleva el registro y control en el Libro Auxiliar de Cuentas por Pagar?",
        help="Libro de Cuentas por Pagar: 1 (No lo tiene), 2 (Está en proceso de adopción), 3 (Si, lo tiene y la usa cotidianamente)"
    ) 
    x_org13= fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "13. ¿Lleva el registro y control en el Libro Auxiliar de Caja, Bancos?",
        help="Libro de Caja y Bancos: 1 (No lo tiene), 2 (Está en proceso de adopción), 3 (Si, lo tiene y la usa cotidianamente)"
    ) 
    x_org14 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "14. ¿Elabora Conciliaciones Bancarias?",
        help="Conciliaciones Bancarias: 1 (No lo tiene), 2 (Está en proceso de adopción), 3 (Si, lo tiene y la usa cotidianamente)"
    ) 
    x_org15 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "15. ¿Lleva libro de inventario y balances de la empresa?",
        help="Libro de Inventarios y Balance: 1 (No lo tiene), 2 (Está en proceso de adopción), 3 (Si, lo tiene y la usa cotidianamente)"
    )
    x_org16 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "16. ¿La empresa elabora planillas para el pago de sus trabajadores?",
        help="Planilla de Pagos de Personal: 0 (No aplica, es de autoempleo), 1 (No la tiene), 2 (Está en proceso de adopción), 3 (Si, lo tiene y la usa cotidianamente)"
    )
    x_org17 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "17. ¿ Elabora los Estados Financieros: Estado de Resultados y Balance General?",
        help="Sistema Contable (Manual/ Automatizado): 1 (No tiene), 2 (Está en proceso de adopción), 3 (Si, lo tiene y usa cotidianamente)"
    )
    x_org18 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "18. ¿Lleva el control del Flujo de Efectivo de su empresa (flujo de caja)?",
        help="Flujo de Efectivo: 1 (No los elabora), 2 (Está en proceso de adopción), 3 (Si, los elabora periódicamente)"
    ) 
    x_org19= fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "19. ¿Cuenta con un Sistema Contable (Manual o Automatizado)?",
        help="Sistema Contable (Manual/ Automatizado): 1 (No tiene), 2 (Está en proceso de adopción), 3 (Si, lo tiene y usa cotidianamente)"
    ) 
    x_org20 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "20. ¿Ha contrado un contador colegiado para el manejo de su contabilidad?",
        help="Contratación de Servicios Contables: 1 (No los contrata), 2 (En proceso, está planificado hacerlo), 3 (Si, los contrata periódicamente)."
    ) 
    x_org21 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "21. ¿Realizan procesos de auditoría interna/ externa, ambas en la empresa?",
        help="Auditoría: 1 (No hacen ningún proceso de auditoría), 2 (En proceso, están planificado hacerlo), 3 (Si, realizan auditoría interna/ externa/ ambas periódicamente)."
    )
    #Producción y Ambiente (15%)
    x_pa1 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "1. ¿La empresa tiene un programa de limpieza de sus áreas de trabajo?",
        help="Programa de limpieza y desinfección: 1 (No lo tiene), 2 (Está en proceso de adopción), 3 (Si, lo tiene y está en ejecución)."
    )

