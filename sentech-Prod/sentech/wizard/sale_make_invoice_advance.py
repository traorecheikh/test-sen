# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, _
import logging
_logger = logging.getLogger(__name__)

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'

    def _prepare_invoice_values(self, order, name, amount, so_line):
        _logger.debug("=============================== I N S I D E    F U N C T I O N =====================")
        res = super()._prepare_invoice_values(order, name, amount, so_line)
        res['libelle'] = order.libelle
        return res

