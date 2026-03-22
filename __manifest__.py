{
    'name': 'Product Creation Control',
    'version': '18.0.1.0.0',
    'category': 'Product Control',
    'summary': 'Control product creation sources per user',
    'description': """
        Allows administrators to control from which sources
        each user is allowed to create products.
        Sources: Product Menu, Purchase Order, Sales Order,
        Manufacturing BOM, Inventory, Vendor Pricelist.
    """,
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
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
