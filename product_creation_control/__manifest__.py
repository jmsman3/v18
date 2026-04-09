{
    'name': 'Product Creation Control',
    'version': '18.0.1.0.0',
    'category': 'Product Control',
    'summary': 'Control product creation sources per user',
    'description': """
Product Creation Control
========================

Controls who can create or edit products and from which source in Odoo.

Problem Solved:
---------------
In standard Odoo, any user can create products from multiple places
(Product Menu, Sales Order, Purchase Order, BOM, Inventory, Vendor Pricelist),
leading to duplicate products, dirty master data, and reporting errors.

Solution:
---------
Assign per-user permissions to control exactly which product creation
sources each user is allowed to use. Also controls whether users can
edit existing product names and categories.

Sources Controlled:
-------------------
- Product Menu
- Sales Order Line
- Purchase Order Line
- Manufacturing BOM
- Inventory Operations
- Vendor Pricelist

Edit Permissions:
-----------------
- Change Product Name
- Change Product Category

Developed by: Md. Jubaer Mahmud Sarker
LinkedIn: https://www.linkedin.com/in/jmsman3/
    """,
    'author': 'The OdooCraft Solution',
    'website': 'https://www.linkedin.com/in/jmsman3/',
    'depends': ['product', 'purchase', 'sale_management', 'mrp', 'stock'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/product_creation_control_views.xml',
        'views/purchase_order_views.xml',
        'views/sale_order_views.xml',
        'views/mrp_bom_views.xml',
        'views/stock_views.xml',
        'views/product_supplierinfo_views.xml',
        'views/menu.xml',
    ],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
