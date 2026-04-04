from odoo import _, api, models


class AccountBankStatement(models.Model):
    _inherit = [
        'mail.thread.main.attachment',
        'account.bank.statement'
    ]

    _name = 'account.bank.statement'

    def action_open_bank_reconcile_widget(self):
        self.ensure_one()

        return self.env['account.bank.statement.line']._action_open_bank_reconciliation_widget(
            name=self.name,
            default_context={
                'search_default_statement_id': self.id,
                'search_default_journal_id': self.journal_id.id,
            },
            extra_domain=[
                ('statement_id', '=', self.id)
            ]
        )

    def action_open_journal_invalid_statements(self):
        self.ensure_one()

        return {
            'name': _('Invalid Bank Statements'),
            'type': 'ir.actions.act_window',
            'res_model': 'account.bank.statement',
            'view_mode': 'list',
            'context': {
                'search_default_journal_id': self.journal_id.id,
                'search_default_invalid': True,
            },
        }

    def action_generate_attachment(self):
        report_service = self.env['ir.actions.report'].sudo()
        report_action = self.env.ref('account.action_report_account_statement').sudo()
        attachment_model = self.env['ir.attachment']

        for statement in self:
            pdf_content, _content_type = report_service._render_qweb_pdf(
                report_action,
                res_ids=statement.ids,
            )

            attachment = attachment_model.create({
                'name': (
                    _("Bank Statement %s.pdf", statement.name)
                    if statement.name
                    else _("Bank Statement.pdf")
                ),
                'type': 'binary',
                'mimetype': 'application/pdf',
                'raw': pdf_content,
                'res_model': statement._name,
                'res_id': statement.id,
            })

            statement.attachment_ids |= attachment

        return report_action.report_action(docids=self)

    @api.model_create_multi
    def create(self, vals_list):
        statements = super().create(vals_list)

        if self.env.context.get('skip_pdf_attachment_generation'):
            return statements

        statements_to_attach = statements.filtered(
            lambda statement: statement.is_complete and not self._has_pdf_attachment(statement)
        )

        if statements_to_attach:
            statements_to_attach.action_generate_attachment()

        return statements

    @staticmethod
    def _has_pdf_attachment(statement):
        return any(
            attachment.mimetype == 'application/pdf'
            for attachment in statement.attachment_ids
        )