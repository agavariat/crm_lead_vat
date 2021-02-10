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
    x_pa2 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "2.  ¿La empresa cuenta con un plan de seguridad y prevención de contingencias?",
        help="Plan de seguridad y contingencias: 1 (No lo tiene), 2 (Está en proceso de adopción), 3 (Si, lo tiene y está en ejecución)"
    )
    x_pa3 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "3.  ¿Tiene la empresa diagramas de flujo de sus procesos?",
        help="Flujo de Procesos: 1 (No lo tiene), 2 (Está en proceso de adopción), 3 (Si, lo tiene y lo utilizan para administrar la producción)."
    )
    x_pa4 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "4.  ¿Cuenta la empresa con una base de datos/ red de proveedores de materias primas, insumos, otros necesarios para el aseguramiento de sus procesos productivos?",
        help="Base de datos de proveedores: 1 (No la tiene establecida), 2 (Está en proceso de adopción), 3 (Si, lo tiene y lo utilizan para asegurar la producción)."
    )
    x_pa5 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "5.  ¿Se tiene en la empresa definidos los estándares de los procesos de producción de los productos/servicios que vende?",
        help="Estándares de procesos productivos: 1 (No, no los tienen definidos), 1 (Está en proceso, los están definiendo, en proceso de adopción), 3 (Si, tienen definidos los estándares de los procesos productivos y los implementan)."
    )
    x_pa6 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "6.  ¿Tiene su empresa un sistema de control/ gestion de calidad adoptado e implementado?",
        help="Control/ gestión de la calidad: 1 (No lo tiene establecido), 2 (Está en proceso de adopción), 3 (Si, lo tiene y es parte integral de la filosofía, sistema de valores de la empresa)."
    )
    x_pa7 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "7.  ¿La empresa sabe cuáles son los costos de cada etapa del proceso de producción?",
        help="Costeo del producto: 1 (No lo hace), 2 (Está en proceso de adopción), 3 (Si, lo hace y lo utilizan para administrar la producción)."
    )
    x_pa8 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "8. ¿La empresa desarrolla prototipos de productos con el objetivo de innovar, asegurar calidad y lanzar nuevos productos al mercado?",
        help="Desarrollo de prototipos: 1 (No lo hace), 2 (Está en proceso de adopción), 3 (Si, lo hace y lo utilizan para lanzar nuevos productos y/o servicios al mercado)."
    )
    x_pa9 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "9. ¿Tiene la empresa un plan/programa de mantenimiento preventivo (Instalaciones, maquinaria, equipo, herramientas, otros)?",
        help="Plan/Programa de mantenimiento preventivo: 1 (No lo tiene), 2 (Está en proceso de adopción), 3 (Si, lo tiene, asignan presupuesto y lo realizan acciones periódicamente en la empresa)."
    )
    x_pa10 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "10. ¿Es adecuado el nivel tecnológico de la maquinaria?",
        help="Tecnología de la maquinaria: 1 (tecnología básica de la maquinaria), 2 (en proceso de reconversión, se tiene algunas maquinaría de tecnología de punta), 3 (Si, en su mayoria se tiene maquinaria de tecnología de punta)."
    )
    x_pa11 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "11. ¿Es adecuado el grado de obsolescencia y estado de conservación de la maquinaria?",
        help="Grado de obsolecencia de la maquinaria: 1 (maquinaria obsoltea y en mal estado), 2 (maquinaria obsoleta pero en excelente estado), 3 (Si, maquinaria actualizada y en buen estado)."
    )
    x_pa12 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "12. ¿El nivel de suficiencia o cobertura de la maquiaria es adecuada al mercado actual? ",
        help="Nivel de Suficiencia de la maquinaría: 1. (insuficiente para la necesidad del mercado), 2 (muy ajustada a la necesidad del mercado), 3 (maquinaria suficiente y un porcentaje extra para altas demanadas y crecimiento proyectado)"
    )
    #Ambiente
    x_pa13 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "13. ¿Tiene su empresa un plan ambiental? ",
        help="Plan ambiental: 1 (No conoce del tema, no tiene plan ambiental, ni planificado elaborarlo), 2 (Está en proceso de elaboración/ adopción, se está capacitando), 3 (Si, lo tiene y está en ejecución continua)."
    )
    x_pa14 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "14.  ¿Tiene la empresa un plan de manejo de desechos sólidos?",
        help="Plan de manejo de desechos sólidos: 0 (No Aplica, no genera desechos sólidos con su actividad), 1 (No conoce del tema, no tiene planificado elaborarlo), 2 (Está en proceso de elaboración/ adopción), 3 (Lo tiene y está en ejecución continua)."
    )
    x_pa15 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "15. ¿Tiene la empresa un plan de manejo de desechos líquidos? ",
        help="Plan de manejo de desechos líquidos: 0 (No Aplica, no genera desechos líquidos con su actividad) 1 (No conoce del tema, no tiene planificado elaborarlo), 2 (Está en proceso de elaboración/ adopción), 3 (Lo tiene y está en ejecución continua)."
    )
    x_pa16 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "16. ¿Recicla o reusa sus desechos?",
        help="Plan/Programa de reciclaje: 1 (No conoce del tema, no tiene planificado elaborarlo), 2 (Está en proceso de elaboración/ adopción), 3 (Lo tiene y está en ejecución continua)."
    )
    x_pa17 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "17. ¿Ha adoptado la empresa alguna medida para disminuir el consumo de energía?",
        help="Eficiencia energética: 1 (No tiene plan/programa de reducción de consumo de energía), 2 (Está en proceso de elaboración y adopción), 3 (Tiene un programa de eficiencia energética en ejecución)."
    )
    x_pa18 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "18. ¿La empresa se integra en alguna actividad que contribuye a la conservación de fuentes de agua, otros recursos naturales?",
        help="Conservación de recursos naturales: 1 (No, no participa en acciones de conservación de recursos naturales, ni tiene planificado hacerlo), 2  (Está en proceso, se está capacitando sobre el tema, esta sensibilizado/ ya ha planificado participar en acciones de conservación de recursos naturales, servicios ecosistémicos), 3 (Está participando la empresa en acciones voluntarias de conservación de recursos naturales/ en mecanismos de compensación de servicios ecosistémicos, otras)."
    )
    #Análisis Financiero (15%)
    x_fa1 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "1. ¿Para determinar el precio de los productos/ servicios la empresa considera los costos fijos y variables?",
        help="Método para determinar precios: 1 (No lo hace), 2 (Está en proceso de adopción), 3 (Si, lo hace y los utiliza para determinar precios de los productos y/o servicios)."
    )
    x_fa2 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "2. ¿Lleva la empresa registro de inventarios de materias primas, producto en proceso y terminado?",
        help="Control de inventarios: 1 (No lo hace), 2 (Está en proceso de adopción), 3 (Si, lo hace y levantan periódicamente los inventarios y la información la utilizan para preparar estados financieros)."
    )
    x_fa3 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "3. ¿Realiza la empresa retención de impuesto sobre ventas y hace su declaración mensual a la DIAN?",
        help="Retención y declaración de impuesto sobre ventas (ISV): 0 (No Aplica, esta acogida al Monotributo), 1 (No, no sabe, no realiza retención ni declaración), 2 (En proceso, está reuniendo requisitos para ser retenedor de ISV), 3 (Si, es retenedor de impuesto sobre ventas y los declara mensualmente)."
    )
    x_fa4 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "4. ¿Realiza la empresa declaración anual de Impuesto Sobre la Renta (DIAN)?",
        help="Declaración de Impuesto Sobre la Renta (ISR): 0 (No Aplica, ), 1 (No, no sabe, no realiza declaración), 2 (En proceso, está en proceso para realizar declaración de impuesto sobre la renta), 3 (Si, realiza anualmente ejercicio de declaración de ISR)."
    )
    x_fa5 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "5. ¿Realiza la empresa declaración  de sus ingresos a la Alcaldia Municipal (ICA)?",
        help="Declaración de Ingresos a la municipalidad: 1 (No, no sabe, no realiza declaración), 2 (En proceso, está en proceso para realizar declaración a la Alcaldía Municipal, unos meses si, otros no), 3 (Si, realiza periódicamente el ejercicio de declarar ingresos a la Alcaldía Municipal)."
    )
    x_fa6 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "6. ¿Conoce el nivel de ventas en la que su empresa cubre sus costos? (Punto de Equilibrio)",
        help="Punto de equilibrio: 1 (No sabe del tema), 2 (Está en proceso de formación, conociendo método para calcularlo), 3 (Si, conoce el nivel de producción y/o ventas en Lempiras donde sus ingresos igualan los costos de producción)."
    )
    x_fa7 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "7. ¿Conoce la empresa su capacidad de endeudamiento? ",
        help="Capacidad de endeudamiento: 1 (No lo tiene, desconoce del tema), 2 (Está en proceso, la empresa está realizando ejercicio de conocer su capacidad para cumplir con requisitos que le exigen los agentes financieros), 3 (Si, la empresa conoce con exactitud su nivel de liquidez para cumplir con los compromisos y su nivel de solvencia para pagar esos compromisos)."
    )
    x_fa7 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "7. ¿Conoce la empresa su capacidad de endeudamiento? ",
        help="Capacidad de endeudamiento: 1 (No lo tiene, desconoce del tema), 2 (Está en proceso, la empresa está realizando ejercicio de conocer su capacidad para cumplir con requisitos que le exigen los agentes financieros), 3 (Si, la empresa conoce con exactitud su nivel de liquidez para cumplir con los compromisos y su nivel de solvencia para pagar esos compromisos)."
    )
    x_fa8 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "8. Capacidad de endeudamiento: 1 (No lo tiene, desconoce del tema), 2 (Está en proceso, la empresa está realizando ejercicio de conocer su capacidad para cumplir con requisitos que le exigen los agentes financieros), 3 (Si, la empresa conoce con exactitud su nivel de liquidez para cumplir con los compromisos y su nivel de solvencia para pagar esos compromisos).",
        help="Gestión de préstamos: 0 (No Aplica, no tiene interés en préstamos), 1 (No ha realizado gestiones, no es elegible su empresa por el sistema financiero), 2 (Está en proceso de reunir requisitos para optar a la oferta de servicios financieros del medio, tiene en gestión un préstamo), 3 (Si, ha recibido préstamo de una entidad de servicios financieros y está activo en su pago)."
    )
    x_fa9 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "9. ¿Tiene la empresa un plan de inversiones?",
        help="Plan de inversión: 1 (No lo tiene, desconoce del tema), 2 (Está en proceso, la empresa está realizando ejercicio de planificar sus inversiones para crecimiento empresarial), 3 (Si, la empresa tiene un plan de inversiones y está en ejecución conforme el plan establecido)."
    )
    x_fa10 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "10. ¿Tiene la empresa un plan de negocios elaborado/ en ejecución?",
        help="Modelo/Plan de negocios: 1 (No lo tiene, desconoce del tema), 2 (Está en proceso, la empresa está elaborando su documento de modelo de negocio), 3 (si, la empresa tiene un modelo/plan de negocios y se está ejecutando a conformidad)."
    )
    x_fa11 = fields.Selection(
        [
            ('no_aplica', 'No Aplica'),
            ('si', 'Si'),
            ('en_proceso', 'En Proceso'),
            ('no', 'No'),
        ], "11. ¿En la empresa toman decisiones con base a información financiera?",
        help="Análisis financiero: 1 (No lo tiene, desconoce del tema), 2 (Está en proceso, la empresa está en proceso de preparar información financiera para elaborar análisis), 3 (Si, la empresa tienen información financiera que le permite conocer la justa realidad de su situación financiera y evalúa su gestión)."
    )
