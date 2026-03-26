# Developed by: Md. Jubaer Mahmud Sarker
# LinkedIn: https://www.linkedin.com/in/jmsman3/

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_customer = fields.Boolean(
        string='Is a Customer',
        default=False,
        help='If checked, this contact will appear in Sales Order customer selections.',
    )
    is_vendor = fields.Boolean(
        string='Is a Vendor',
        default=False,
        help='If checked, this contact will appear in Purchase Order vendor selections.',
    )
