from odoo import models


class AccountReconcileModelLine(models.Model):
    """Extends ``account.reconcile.model.line`` with widget journal-item helpers."""
    _inherit = "account.reconcile.model.line"

    def _prepare_aml_vals(self, partner):
        """Return base journal-item values for a reconciliation rule line."""
        raise NotImplementedError("Not yet implemented.")

    def _apply_in_manual_widget(self, residual_amount_currency, residual_balance, partner, st_line):
        """Return journal-item values for the manual reconciliation widget."""
        raise NotImplementedError("Not yet implemented.")

    def _apply_in_bank_widget(self, residual_amount_currency, residual_balance, partner, st_line):
        """Return journal-item values for the bank reconciliation widget."""
        raise NotImplementedError("Not yet implemented.")

    def _get_amount_currency_by_regex(self, st_line, residual_amount_currency, amount_string):
        """Extract an amount from statement text using the rule's regex pattern."""
        raise NotImplementedError("Not yet implemented.")
