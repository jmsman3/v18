from odoo import models, api, exceptions, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # ── Helpers ──────────────────────────────────────────────────────────

    def _get_product_creation_source(self):
        return self.env.context.get('product_creation_source', 'product_menu')

    def _is_bypass(self):
        """Return True when checks should be skipped (superuser or internal flag)."""
        return self.env.su or self.env.context.get('bypass_product_creation_check')

    # ── CREATE controls ───────────────────────────────────────────────────

    def _check_product_creation_allowed(self):
        if self._is_bypass():
            return
        source = self._get_product_creation_source()
        allowed = self.env['product.creation.control'].get_user_permission(source)
        if not allowed:
            raise exceptions.UserError(_(
                "You are not allowed to create products from this source.\n"
                "Please contact your system administrator."
            ))

    @api.model_create_multi
    def create(self, vals_list):
        self._check_product_creation_allowed()
        return super().create(vals_list)

    @api.model
    def name_create(self, name):
        self._check_product_creation_allowed()
        return super().name_create(name)

    def copy(self, default=None):
        self = self.with_context(product_creation_source='product_menu')
        return super().copy(default=default)

    # ── WRITE controls ────────────────────────────────────────────────────

    def write(self, vals):
        if not self._is_bypass():
            ctrl = self.env['product.creation.control']

            # Block product name change
            if 'name' in vals:
                # Only raise if at least one record's name is actually changing
                for rec in self:
                    if rec.name != vals['name']:
                        if not ctrl.check_permission('allow_product_name_change'):
                            raise exceptions.UserError(_(
                                "You are not allowed to change a product's name.\n"
                                "Please contact your system administrator."
                            ))
                        break  # permission granted, no need to check further

            # Block product category change
            if 'categ_id' in vals:
                for rec in self:
                    if rec.categ_id.id != vals['categ_id']:
                        if not ctrl.check_permission('allow_product_category_change'):
                            raise exceptions.UserError(_(
                                "You are not allowed to change a product's category.\n"
                                "Please contact your system administrator."
                            ))
                        break

        return super().write(vals)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def name_create(self, name):
        """
        Intercept quick-create on product.product Many2one fields
        (e.g. sale order line, stock move product_id).
        """
        if not self.env.su and not self.env.context.get('bypass_product_creation_check'):
            source = self.env.context.get('product_creation_source', 'product_menu')
            allowed = self.env['product.creation.control'].get_user_permission(source)
            if not allowed:
                raise exceptions.UserError(_(
                    "You are not allowed to create products from this source.\n"
                    "Please contact your system administrator."
                ))
        return super().name_create(name)
