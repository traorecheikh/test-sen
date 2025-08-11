from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'
    
    libelle = fields.Char(string="Libellé: ")
