import ast

from odoo import models


class AccountAccount(models.Model):
    """Extends ``account.account`` with a reconciliation entry point."""
    _inherit = "account.account"

    def action_open_reconcile(self):
        """Open unreconciled posted journal items filtered to this account."""
        self.ensure_one()

        action_values = self.env['ir.actions.act_window']._for_xml_id(
            ''  # todo: add xml id
        )

        domain = ast.literal_eval(
            action_values['domain']
        )

        domain.append(
            ('account_id', '=', self.id)
        )

        action_values['domain'] = domain

        return action_values
