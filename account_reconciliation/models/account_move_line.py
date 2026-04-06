from odoo import api, fields, models


class AccountMoveLine(models.Model):
    """Extends ``account.move.line`` with move-level attachment access."""
    _inherit = "account.move.line"

    move_attachment_ids = fields.One2many(
        'ir.attachment',
        compute='_compute_attachment'
    )

    @api.depends('move_id')
    def _compute_attachment(self):
        """Mirror the parent move's attachments onto each journal item."""
        raise NotImplementedError("Not yet implemented.")
