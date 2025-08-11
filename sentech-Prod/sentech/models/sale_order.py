from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    libelle = fields.Char(string="Libellé: ")

    def _prepare_invoice(self):
        _logger.debug("=============================== I N S I D E    F U N C T I O N =====================")
        res = super()._prepare_invoice()
        res['libelle'] = self.libelle
        return res


