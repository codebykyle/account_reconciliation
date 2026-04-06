from odoo import models


class AccountReconcileModel(models.Model):
    """Extends ``account.reconcile.model`` with bank widget integration."""
    _inherit = "account.reconcile.model"

    def _apply_lines_for_bank_widget(self, residual_amount_currency, residual_balance, partner, st_line):
        """Return journal-item values a bank-widget rule should create."""
        raise NotImplementedError("Not yet implemented.")

    def get_available_reconcile_model_per_statement_line(self, statement_line_ids):
        """Return available reconciliation models grouped by statement line."""
        raise NotImplementedError("Not yet implemented.")

    def _apply_reconcile_models(self, statement_lines):
        """Apply matching reconciliation rules to the provided statement lines."""
        raise NotImplementedError("Not yet implemented.")

    def _trigger_reconciliation_model(self, statement_line):
        """Trigger the best matching rule for a single statement line."""
        raise NotImplementedError("Not yet implemented.")

    def trigger_reconciliation_model(self, statement_line_id):
        """Public entry point to trigger a rule by statement-line ID."""
        raise NotImplementedError("Not yet implemented.")

    def write(self, vals):
        """Override to preserve base write behavior for reconciliation rules."""
        raise NotImplementedError("Not yet implemented.")

    def create(self, vals_list):
        """Override to preserve base create behavior for reconciliation rules."""
        raise NotImplementedError("Not yet implemented.")

    def action_archive(self):
        """Archive reconciliation models using inherited behavior."""
        raise NotImplementedError("Not yet implemented.")
