import logging
import re
import string

from dateutil.relativedelta import relativedelta
from markupsafe import Markup

from odoo import Command, SUPERUSER_ID, _, api, fields, models, modules, tools
from odoo.exceptions import UserError, ValidationError
from odoo.fields import Domain
from odoo.tools import SQL, float_compare, float_is_zero, format_date
from odoo.addons.account.tools.structured_reference import is_valid_structured_reference

class AccountBankStatementLine(models.Model):
    _name = 'account.bank.statement.line'

    _inherit = [
        'account.bank.statement.line',
        'mail.thread.main.attachment'
    ]

    cron_last_check = fields.Datetime()

    bank_statement_attachment_ids = fields.One2many(
        'ir.attachment',
        compute='_compute_bank_statement_attachment_ids'
    )

    attachment_ids = fields.One2many(
        'ir.attachment',
        related="move_id.attachment_ids"
    )

    def action_save_close(self):
        return {
            'type': 'ir.actions.act_window_close'
        }

    def action_save_new(self):
        action = self.env['ir.actions.act_window']._for_xml_id(
            'account_reconciliation.action_bank_statement_line_form_bank_reconciliation_widget'
        )

        action['context'] = {
            'default_journal_id': self.env.context['default_journal_id']
        }

        return action

    def action_button_draft(self):
        return self.move_id.button_draft()

    ####################################################
    # COMPUTE METHODS ##################################
    ####################################################
    def _get_attachments_grouped_by_res_id(self, res_model, res_ids, res_fields=None):
        domain = [
            ('res_model', '=', res_model),
            ('res_id', 'in', res_ids),
        ]
        if res_fields is not None:
            domain.append(('res_field', 'in', res_fields))

        return self.env['ir.attachment'].search(domain).grouped('res_id')

    def _compute_bank_statement_attachment_ids(self):
        attachments_by_statement = self._get_attachments_grouped_by_res_id(
            res_model='account.bank.statement',
            res_ids=self.statement_id.ids,
            res_fields=(False, 'invoice_pdf_report_file'),
        )

        for line in self:
            line.bank_statement_attachment_ids = attachments_by_statement.get(line.statement_id.id)

    ####################################################
    # Reconciliation  ##################################
    ####################################################