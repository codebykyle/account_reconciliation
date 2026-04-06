from odoo import models


class AccountMove(models.Model):
    """Extends ``account.move`` with bank reconciliation navigation hooks."""
    _inherit = "account.move"

    def action_open_bank_reconciliation_widget(self):
        """Open the bank reconciliation widget for the move's statement line."""
        raise NotImplementedError("Not yet implemented.")

    def action_open_bank_reconciliation_widget_statement(self):
        """Open the widget scoped to the statement(s) linked to this move."""
        raise NotImplementedError("Not yet implemented.")

    def action_open_business_doc(self):
        """Open the reconciliation widget when a bank line is linked; otherwise fall back to standard behavior."""
        raise NotImplementedError("Not yet implemented.")

    def _get_mail_thread_data_attachments(self):
        """Include statement and reconciliation attachments in the chatter payload."""
        raise NotImplementedError("Not yet implemented.")

    def _compute_payments_widget_to_reconcile_info(self):
        """Extend the invoice payment widget with bank-statement-backed outstanding items."""
        raise NotImplementedError("Not yet implemented.")

    def js_assign_outstanding_line(self, line_id):
        """Assign a bank-statement-backed outstanding line to the invoice."""
        raise NotImplementedError("Not yet implemented.")

    def js_remove_outstanding_partial(self, partial_id):
        """Remove a reconciliation partial originating from a bank statement line."""
        raise NotImplementedError("Not yet implemented.")
