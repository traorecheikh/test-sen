
from odoo import api, fields, models

#Display amount in words in Sale order
class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'
    
    invoice_id = fields.Many2one('account.move', compute = '_compute_invoice')
      

    @api.depends('can_edit_wizard')
    def _compute_invoice(self):
        # The communication can't be computed in '_compute_from_lines' because
        # it's a compute editable field and then, should be computed in a separated method.
        for wizard in self:
            if wizard.can_edit_wizard:
                batches = wizard._get_batches()
                wizard.invoice_id = batches[0]['lines'].move_id.id
                wizard.invoice_id.display_account_bank = wizard.partner_bank_id.acc_number
            else:
                wizard.invoice_id = False
    
