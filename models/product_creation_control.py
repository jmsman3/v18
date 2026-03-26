# Developed by: Md. Jubaer Mahmud Sarker
# LinkedIn: https://www.linkedin.com/in/jmsman3/

from odoo import models, fields, api, _

# Maps context source key → boolean field on product.creation.control
SOURCE_FIELD_MAP = {
    'product_menu':     'allow_product_menu',
    'purchase_line':    'allow_purchase_line',
    'sales_line':       'allow_sales_line',
    'bom':              'allow_bom',
    'inventory':        'allow_inventory',
    'vendor_pricelist': 'allow_vendor_pricelist',
}


class ProductCreationControl(models.Model):
    _name = 'product.creation.control'
    _description = 'Product Creation Control'
    _rec_name = 'user_id'
    _order = 'user_id'

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        required=True,
        ondelete='cascade',
        index=True,
    )

    # ── Product Creation Source Permissions ──────────────────────────────
    allow_product_menu = fields.Boolean(
        string='Product Menu',
        help='Allow creating products directly from the Product menu.',
    )
    allow_purchase_line = fields.Boolean(
        string='Purchase Order Line',
        help='Allow creating products from a Purchase Order line.',
    )
    allow_sales_line = fields.Boolean(
        string='Sales Order Line',
        help='Allow creating products from a Sales Order line.',
    )
    allow_bom = fields.Boolean(
        string='Manufacturing BOM',
        help='Allow creating products from a Bill of Materials.',
    )
    allow_inventory = fields.Boolean(
        string='Inventory Operations',
        help='Allow creating products from Inventory adjustments.',
    )
    allow_vendor_pricelist = fields.Boolean(
        string='Vendor Pricelist',
        help='Allow creating products from Vendor Pricelist / Supplier Info.',
    )

    # ── Product Edit Permissions ─────────────────────────────────────────
    allow_product_name_change = fields.Boolean(
        string='Change Product Name',
        help='Allow this user to edit/rename an existing product name.',
    )
    allow_product_category_change = fields.Boolean(
        string='Change Product Category',
        help='Allow this user to change the category of an existing product.',
    )

    _sql_constraints = [
        ('user_unique', 'UNIQUE(user_id)',
         'A product creation control configuration already exists for this user.'),
    ]

    @api.model
    def check_permission(self, field_name):
        """
        Generic permission check for any boolean field on this model.

        Returns True  → allowed
        Returns False → blocked

        Superuser (env.su) always returns True.
        If no control record exists for the user → False (blocked by default).
        """
        if self.env.su:
            return True

        control = self.sudo().search(
            [('user_id', '=', self.env.user.id)], limit=1
        )
        if not control:
            return False

        return bool(control[field_name])

    @api.model
    def get_user_permission(self, source):
        """Check product CREATION permission for a given source key."""
        field_name = SOURCE_FIELD_MAP.get(source, 'allow_product_menu')
        return self.check_permission(field_name)
