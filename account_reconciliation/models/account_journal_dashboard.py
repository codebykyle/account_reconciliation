from odoo import models


class AccountJournal(models.Model):
    """Extends ``account.journal`` with reconciliation dashboard actions."""
    _inherit = "account.journal"

    def action_open_reconcile(self):
        """Open the reconciliation widget for liquidity journals; fall back to posted/unreconciled items otherwise."""
        raise NotImplementedError("Not yet implemented.")

    def action_open_to_check(self):
        """Open the widget filtered to lines flagged for manual review."""
        raise NotImplementedError("Not yet implemented.")

    def action_open_bank_transactions(self):
        """Open the widget in transaction-first mode for this journal."""
        raise NotImplementedError("Not yet implemented.")

    def action_open_reconcile_statement(self):
        """Open the widget scoped to the statement selected in context."""
        raise NotImplementedError("Not yet implemented.")

    def open_invalid_statements_action(self):
        """Open invalid statements for this journal."""
        raise NotImplementedError("Not yet implemented.")

    def open_action(self):
        """Use the reconciliation widget as the default action for liquidity journals."""
        raise NotImplementedError("Not yet implemented.")

    def get_total_journal_amount(self):
        """Return the formatted current balance and invalid-statement flag for the dashboard."""
        raise NotImplementedError("Not yet implemented.")
