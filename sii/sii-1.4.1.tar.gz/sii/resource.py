# coding=utf-8
import re
from copy import deepcopy
from unidecode import unidecode
from decimal import Decimal, localcontext

from sii import __SII_VERSION__
from sii.models import invoices_record
from sii.utils import COUNTRY_CODES

SIGN = {'N': 1, 'R': 1, 'A': -1, 'B': -1, 'RA': 1, 'C': 1, 'G': 1}  # 'BRA': -1


def get_invoice_sign(invoice):
    if invoice.type.endswith('refund'):
        return -1
    return 1


def get_iva_values(invoice, in_invoice, is_export=False, is_import=False):
    """

    :param invoice:
    :param in_invoice: indica si es una factura recibida
    :type in_invoice: bool
    :param is_export: indica si es una exportación
    :type  is_export: bool
    :param is_import: indica si es una importación
    :type is_import: bool
    :return:
    """
    vals = {
        'sujeta_a_iva': False,
        'detalle_iva': [],
        'no_sujeta_a_iva': False,
        'iva_exento': False,
        'iva_no_exento': False,
        'detalle_iva_exento': {'BaseImponible': 0},
        'importe_no_sujeto': 0
    }

    invoice_total = invoice.amount_total
    # iva_values es un diccionario que agrupa los valores del IVA por el tipo
    # impositivo. ejemplo:
    #
    # iva_values = {
    #     21.0: {
    #         'BaseImponible': ...,
    #         'TipoImpositivo': ...,
    #         'Cuota...': ...
    #     },
    #     18.0: {
    #         'BaseImponible': ...,
    #         'TipoImpositivo': ...,
    #         'Cuota...': ...
    #     }
    # }
    iva_values = {}

    for inv_tax in invoice.tax_line:
        if 'iva' in inv_tax.name.lower():
            vals['sujeta_a_iva'] = True

            if invoice_total < 0:
                invoice_total += (abs(inv_tax.tax_amount) + abs(inv_tax.base))
            else:
                invoice_total -= (abs(inv_tax.tax_amount) + abs(inv_tax.base))

            is_iva_exento = (
                inv_tax.tax_id.amount == 0 and inv_tax.tax_id.type == 'percent'
            )
            # IVA 0% Exportaciones y IVA 0% Importaciones tienen amount 0 y se
            # detectan como IVA exento
            if not is_export and not is_import and is_iva_exento:
                vals['iva_exento'] = True
                vals['detalle_iva_exento']['BaseImponible'] += inv_tax.base
            else:
                sign = get_invoice_sign(invoice)
                tipo_impositivo = inv_tax.tax_id.amount * 100
                base_imponible = sign * abs(inv_tax.base)
                if in_invoice:
                    cuota_key = 'CuotaSoportada'
                else:
                    cuota_key = 'CuotaRepercutida'
                cuota = sign * abs(inv_tax.tax_amount)
                if tipo_impositivo in iva_values:
                    aux = iva_values[tipo_impositivo]
                    aux['BaseImponible'] += base_imponible
                    aux[cuota_key] += cuota
                else:
                    iva = {
                        'BaseImponible': base_imponible,
                        'TipoImpositivo': tipo_impositivo,
                        cuota_key: cuota
                    }
                    iva_values[tipo_impositivo] = iva
                vals['iva_no_exento'] = True

    vals['detalle_iva'] = iva_values.values()

    invoice_total = round(invoice_total, 2)
    if invoice_total != 0:
        vals['no_sujeta_a_iva'] = True
        vals['importe_no_sujeto'] = invoice_total

    return vals


def get_contraparte(partner, in_invoice):
    vat_type = partner.sii_get_vat_type()
    contraparte = {'NombreRazon': unidecode(partner.name)}

    partner_country = partner.country_id or partner.country

    if vat_type == '02':
        if not partner.aeat_registered and not in_invoice:
            contraparte['IDOtro'] = {
                'CodigoPais': partner_country.code,
                'IDType': '07',
                'ID': partner.vat
            }
        else:
            contraparte['NIF'] = partner.vat
    else:
        contraparte['IDOtro'] = {
            'CodigoPais': partner_country.code,
            'IDType': vat_type,
            'ID': partner.vat
        }

    return contraparte


def get_factura_emitida_tipo_desglose(invoice):
    in_invoice = False
    is_export = invoice.sii_out_clave_regimen_especial == '02'  # Exportación
    iva_values = get_iva_values(
        invoice, in_invoice=in_invoice, is_export=is_export
    )

    if bool(is_export):
        if iva_values['sujeta_a_iva']:
            detalle_iva = iva_values['detalle_iva']

            entrega = {
                'Sujeta': {
                    'NoExenta': {
                        'TipoNoExenta': 'S1',
                        'DesgloseIVA': {
                            'DetalleIVA': detalle_iva
                        }
                    }
                }
            }
        else:
            detalle_iva_exento = iva_values['detalle_iva_exento']

            entrega = {
                'Sujeta': {
                    'Exenta': detalle_iva_exento
                }
            }
            # Exenta por el artículo 21
            entrega['Sujeta']['Exenta']['CausaExencion'] = 'E2'

        tipo_desglose = {
            'DesgloseTipoOperacion': {
                'Entrega': entrega
            }
        }
    else:
        desglose = {}
        detalle_iva_exento = iva_values['detalle_iva_exento']
        detalle_iva = iva_values['detalle_iva']
        importe_no_sujeto = iva_values['importe_no_sujeto']

        if iva_values['sujeta_a_iva']:
            desglose['Sujeta'] = {}
            if iva_values['iva_exento']:
                desglose['Sujeta']['Exenta'] = detalle_iva_exento
            if iva_values['iva_no_exento']:
                desglose['Sujeta']['NoExenta'] = {
                    'TipoNoExenta': 'S1',
                    'DesgloseIVA': {
                        'DetalleIVA': detalle_iva
                    }
                }
        if iva_values['no_sujeta_a_iva']:
            fp = invoice.fiscal_position
            if fp and 'islas canarias' in unidecode(fp.name.lower()):
                desglose['NoSujeta'] = {
                    'ImporteTAIReglasLocalizacion': importe_no_sujeto
                }
            else:
                desglose['NoSujeta'] = {
                    'ImportePorArticulos7_14_Otros': importe_no_sujeto
                }

        partner_vat = invoice.partner_id.vat
        partner_vat_starts_with_n = (
            partner_vat and partner_vat.upper().startswith('N')
        )
        has_id_otro = invoice.partner_id.sii_get_vat_type() != '02'
        if has_id_otro or partner_vat_starts_with_n:
            tipo_desglose = {
                'DesgloseTipoOperacion': {
                    'PrestacionServicios': desglose
                }
            }
        else:
            tipo_desglose = {
                'DesgloseFactura': desglose
            }

    return tipo_desglose


def get_fact_rect_sustitucion_fields(invoice, opcion=False):
    """

    Ejemplo: La factura nº1 de base imponible 1.000 € y cuota 210 € va a ser
    objeto de rectificación.

    Opción 1: La modificación por sustitución supondría emitir una factura
    rectificativa con base imponible de 800 € y cuota 168, en la que se indicará
    que la rectificación realizada es de 1000 € por la base imponible
    rectificada y 210 € por la cuota rectificada.
    Los campos y claves a consignar en el Libro registro de Facturas Expedidas
    son:
        Tipo Comunicación: A0
        Tipo Factura: Rx
        Tipo Rectificativa: S
        Importe Rectificación: se informará de dos campos adicionales con “la
            base rectificada” (1.000) y la “cuota rectificada” (210), con
            independencia de su signo.
        Importe total: se indicará el importe final válido 968.
        Desglose IVA: base imponible: 800, cuota repercutida 168.

    Opción 2: La modificación por sustitución supondría emitir una factura con
    base imponible de -1000 € y una factura rectificativa en la que se indicará
    que la base imponible es de 800 €.
    En la primera factura los campos y claves a consignar en el Libro registro
    de Facturas Expedidas son:
        Tipo Comunicación: A0
        Tipo Factura: F1
        Desglose IVA: se indicará el importe que se rectifica (base imponible:
            (-1.000), cuota repercutida (-210).)
    En la segunda de las facturas rectificativas los campos y claves a consignar
    en el Libro registro de Facturas Expedidas son:
        Tipo Comunicación: A0
        Tipo Factura: Rx
        Tipo Rectificativa: S
        Importe Rectificación: se informará de dos campos adicionales con “la
            base rectificada” 0 y la “cuota rectificada” 0.
        Importe total: se indicará el importe final válido 968
        Desglose IVA: base imponible: 800, cuota repercutida 168.

    :param opcion: tipo de opcion para los campos de sustitucion (1 o 2)
        Opcion 1: un solo envío

    :type opcion: int
    :return:
    """
    rectificativa_fields = {
        'TipoRectificativa': 'S'  # Por sustitución
    }

    if opcion == 1:
        factura_rectificada = invoice.rectifying_id
        rectificativa_fields['ImporteRectificacion'] = {
            'BaseRectificada': abs(factura_rectificada.amount_untaxed),
            'CuotaRectificada': abs(factura_rectificada.amount_tax)
        }
    elif opcion == 2:
        rectificativa_fields['ImporteRectificacion'] = {
            'BaseRectificada': 0,
            'CuotaRectificada': 0
        }

    return rectificativa_fields


def get_factura_emitida(invoice, rect_sust_opc1=False, rect_sust_opc2=False):

    rectificativa = rect_sust_opc1 or rect_sust_opc2

    factura_expedida = {
        'TipoFactura': 'R4' if rectificativa == 'R' else 'F1',
        'ClaveRegimenEspecialOTrascendencia':
            invoice.sii_out_clave_regimen_especial,
        'ImporteTotal': get_invoice_sign(invoice) * invoice.amount_total,
        'DescripcionOperacion': invoice.sii_description,
        'Contraparte': get_contraparte(invoice.partner_id, in_invoice=False),
        'TipoDesglose': get_factura_emitida_tipo_desglose(invoice)
    }

    # Si la factura es una operación de arrendamiento
    # de local de negocio (alquiler)
    if invoice.sii_out_clave_regimen_especial in ['12', '13']:
        detalle_inmueble = {}

        codigo_comunidad_autonoma = (
            invoice.address_contact_id.state_id.comunitat_autonoma.codi
        )

        # '01', '02', ..., '19': Comunidades autónomas de España
        if codigo_comunidad_autonoma in [str(s).zfill(2) for s in range(1, 20)]:
            ref_catastral = invoice.address_contact_id.ref_catastral
            if ref_catastral:
                detalle_inmueble['ReferenciaCatastral'] = ref_catastral

                # '15': Comunidad Foral de Navarra
                # '16': País Vasco
                if codigo_comunidad_autonoma not in ['15', '16']:
                    situacion_inmueble = '1'
                else:
                    situacion_inmueble = '2'
            else:
                situacion_inmueble = '3'
        else:
            situacion_inmueble = '4'

        detalle_inmueble['SituacionInmueble'] = situacion_inmueble

        factura_expedida['DatosInmueble'] = {
            'DetalleInmueble': detalle_inmueble
        }

    if rectificativa:
        opcion = 0
        if rect_sust_opc1:
            opcion = 1
        elif rect_sust_opc2:
            opcion = 2
        vals = get_fact_rect_sustitucion_fields(invoice, opcion=opcion)

        factura_rectificada = invoice.rectifying_id
        vals['FacturasRectificadas'] = {
            'IDFacturaRectificada': [{
                'NumSerieFacturaEmisor': factura_rectificada.number,
                'FechaExpedicionFacturaEmisor': factura_rectificada.date_invoice
            }]
        }

        factura_expedida.update(vals)

    return factura_expedida


def get_factura_recibida(invoice, rect_sust_opc1=False, rect_sust_opc2=False):
    in_invoice = True
    # Factura correspondiente a una importación (informada sin asociar a un DUA)
    is_import = invoice.sii_in_clave_regimen_especial == '13'
    iva_values = get_iva_values(
        invoice, in_invoice=in_invoice, is_import=is_import
    )

    cuota_deducible = 0
    importe_total = get_invoice_sign(invoice) * invoice.amount_total

    if iva_values['sujeta_a_iva'] and iva_values['iva_no_exento']:
        detalle_iva = iva_values['detalle_iva']

        desglose_factura = {  # TODO to change
            # 'InversionSujetoPasivo': {
            #     'DetalleIVA': iva_values['detalle_iva']
            # },
            'DesgloseIVA': {
                'DetalleIVA': detalle_iva
            }
        }

        for iva in detalle_iva:
            cuota_deducible += iva['CuotaSoportada']
    else:
        base_imponible_factura = invoice.amount_untaxed

        desglose_factura = {
            'DesgloseIVA': {
                'DetalleIVA': [{
                    'BaseImponible': base_imponible_factura
                }]
            }
        }

    rectificativa = rect_sust_opc1 or rect_sust_opc2

    factura_recibida = {
        'TipoFactura': 'R4' if rectificativa else 'F1',
        'ClaveRegimenEspecialOTrascendencia':
            invoice.sii_in_clave_regimen_especial,
        'ImporteTotal': importe_total,
        'DescripcionOperacion': invoice.sii_description,
        'Contraparte': get_contraparte(
            invoice.partner_id, in_invoice=in_invoice),
        'DesgloseFactura': desglose_factura,
        'CuotaDeducible': cuota_deducible,
        'FechaRegContable': invoice.date_invoice
    }

    if rectificativa:
        opcion = 0
        if rect_sust_opc1:
            opcion = 1
        elif rect_sust_opc2:
            opcion = 2
        vals = get_fact_rect_sustitucion_fields(invoice, opcion=opcion)

        factura_rectificada = invoice.rectifying_id
        vals['FacturasRectificadas'] = {
            'IDFacturaRectificada': [{
                'NumSerieFacturaEmisor': factura_rectificada.origin,
                'FechaExpedicionFacturaEmisor':
                    factura_rectificada.origin_date_invoice
            }]
        }

        factura_recibida.update(vals)

    return factura_recibida


def get_header(invoice):
    cabecera = {
        'IDVersionSii': __SII_VERSION__,
        'Titular': {
            'NombreRazon': invoice.company_id.partner_id.name,
            'NIF': invoice.company_id.partner_id.vat
        },
        'TipoComunicacion': 'A0' if not invoice.sii_registered else 'A1'
    }

    return cabecera


def get_factura_emitida_dict(invoice,
                             rect_sust_opc1=False, rect_sust_opc2=False):
    obj = {
        'SuministroLRFacturasEmitidas': {
            'Cabecera': get_header(invoice),
            'RegistroLRFacturasEmitidas': {
                'PeriodoImpositivo': {
                    'Ejercicio': invoice.period_id.name[3:7],
                    'Periodo': invoice.period_id.name[0:2]
                },
                'IDFactura': {
                    'IDEmisorFactura': {
                        'NIF': invoice.company_id.partner_id.vat
                    },
                    'NumSerieFacturaEmisor': invoice.number,
                    'FechaExpedicionFacturaEmisor': invoice.date_invoice
                },
                'FacturaExpedida': get_factura_emitida(
                    invoice, rect_sust_opc1, rect_sust_opc2
                )
            }
        }
    }

    return obj


def get_factura_recibida_dict(invoice,
                              rect_sust_opc1=False, rect_sust_opc2=False):
    obj = {
        'SuministroLRFacturasRecibidas': {
            'Cabecera': get_header(invoice),
            'RegistroLRFacturasRecibidas': {
                'PeriodoImpositivo': {
                    'Ejercicio': invoice.period_id.name[3:7],
                    'Periodo': invoice.period_id.name[0:2]
                },
                'IDFactura': {
                    'IDEmisorFactura': {
                        'NIF': invoice.partner_id.vat
                    },
                    'NumSerieFacturaEmisor': invoice.origin,
                    'FechaExpedicionFacturaEmisor': invoice.origin_date_invoice
                },
                'FacturaRecibida': get_factura_recibida(
                    invoice, rect_sust_opc1, rect_sust_opc2
                )
            }
        }
    }

    return obj


def refactor_nifs(invoice):
    for partner in (invoice.partner_id, invoice.company_id.partner_id):
        country_code = partner.vat[:2].upper()
        if country_code in COUNTRY_CODES or country_code == 'PS':
            # partner.vat = re.sub('^ES', '', partner.vat.upper())
            partner.vat = partner.vat[2:]


def refactor_decimals(invoice):
    def transform(f):
        return Decimal(str(f))

    invoice.amount_total = transform(invoice.amount_total)
    invoice.amount_untaxed = transform(invoice.amount_untaxed)

    for inv_tax in invoice.tax_line:
        inv_tax.tax_amount = transform(inv_tax.tax_amount)
        inv_tax.base = transform(inv_tax.base)
        inv_tax.tax_id.amount = transform(inv_tax.tax_id.amount)

    if invoice.rectifying_id:
        rectified_invoice = invoice.rectifying_id

        rectified_invoice.amount_total = transform(
            rectified_invoice.amount_total)
        rectified_invoice.amount_untaxed = transform(
            rectified_invoice.amount_untaxed)

        for rect_inv_tax in rectified_invoice.tax_line:
            rect_inv_tax.tax_amount = transform(rect_inv_tax.tax_amount)
            rect_inv_tax.base = transform(rect_inv_tax.base)
            rect_inv_tax.tax_id.amount = transform(rect_inv_tax.tax_id.amount)


class SII(object):
    def __init__(self, invoice):
        self.invoice = invoice
        refactor_nifs(self.invoice)
        refactor_decimals(self.invoice)
        tipo_rectificativa = invoice.rectificative_type
        rectificativa_sustitucion_opcion_1 = tipo_rectificativa == 'RA'
        rectificativa_sustitucion_opcion_2 = tipo_rectificativa == 'R'
        if invoice.type.startswith('in'):
            self.invoice_model = invoices_record.SuministroFacturasRecibidas()
            self.invoice_dict = get_factura_recibida_dict(
                invoice=self.invoice,
                rect_sust_opc1=rectificativa_sustitucion_opcion_1,
                rect_sust_opc2=rectificativa_sustitucion_opcion_2
            )
        elif invoice.type.startswith('out'):
            self.invoice_model = invoices_record.SuministroFacturasEmitidas()
            self.invoice_dict = get_factura_emitida_dict(
                invoice=self.invoice,
                rect_sust_opc1=rectificativa_sustitucion_opcion_1,
                rect_sust_opc2=rectificativa_sustitucion_opcion_2
            )
        else:
            raise AttributeError(
                'Valor desconocido en el tipo de factura: {}'.format(
                    invoice.type
                )
            )

    def get_validation_errors_list(self, errors):
        error_messages = []

        for key, values in errors.items():
            if isinstance(values, dict):
                error_messages += self.get_validation_errors_list(values)
            else:
                error_messages += ['{}: {}'.format(key, val) for val in values]

        return error_messages

    def validate_invoice(self):

        res = {}

        errors = self.invoice_model.validate(self.invoice_dict)

        res['successful'] = False if errors else True
        res['object_validated'] = self.invoice_dict
        if errors:
            errors_list = self.get_validation_errors_list(errors)
            res['errors'] = errors_list

        return res

    def generate_object(self):

        validation_values = self.validate_invoice()
        if not validation_values['successful']:
            raise Exception(
                'Errors were found while trying to validate the data:',
                validation_values['errors']
            )

        res = self.invoice_model.dump(self.invoice_dict)
        if res.errors:
            raise Exception(
                'Errors were found while trying to generate the dump:',
                res.errors
            )

        return res.data
