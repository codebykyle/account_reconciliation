from odoo import models


class AccountPayment(models.Model):
    """Extends ``account.payment`` with reconciliation navigation and journal-item helpers."""
    _inherit = "account.payment"

    def action_open_manual_reconciliation_widget(self):
        """Open the posted/unreconciled move-line action for this payment."""
        raise NotImplementedError("Not yet implemented.")

    def button_open_statement_lines(self):
        """Open the bank statement lines matched to this payment."""
        raise NotImplementedError("Not yet implemented.")

    def _get_amls_for_payment_without_move(self):
        """Build journal-item values for payments that lack a move."""
        raise NotImplementedError("Not yet implemented.")

    def _get_aml_amount_in_payment_currency(self, aml):
        """Convert a journal-item amount into the payment currency."""
        raise NotImplementedError("Not yet implemented.")

    def _get_amls_for_reconciliation(self, st_line):
        """Prepare journal items for payment reconciliation against a statement line."""
        raise NotImplementedError("Not yet implemented.")
