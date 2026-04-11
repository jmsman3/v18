{
    'name': 'Contact Role-Based Filtering',
    'version': '18.0.1.0.0',
    'category': 'Custom Modules',
    'summary': 'Role-based contact classification — filter customers in Sales and vendors in Purchase',
    'description': """
Contact Role-Based Filtering
=============================

Problem Solved:
---------------
In standard Odoo, all contacts (Customers, Vendors, Employees, Others) appear
in Sales and Purchase dropdowns together. This causes users to select wrong
contacts, leading to incorrect documents, dirty data, and reporting errors.

Solution:
---------
Adds two simple boolean fields to every contact — Is a Customer and Is a Vendor.
Sales Orders show only customers. Purchase Orders show only vendors.
Dual-role contacts appear in both. Contacts with no role appear in neither.

Visibility Rules:
-----------------
- Customer only     → visible in Sales only
- Vendor only       → visible in Purchase only
- Customer + Vendor → visible in both
- None              → visible in neither

Smart Auto-Role:
----------------
- New contact created from Sales Order → auto-set as Customer
- New contact created from Purchase Order → auto-set as Vendor

Developed by: Md. Jubaer Mahmud Sarker
LinkedIn: https://www.linkedin.com/in/jmsman3/
    """,
    'author': 'OdooNest',
    'website': 'https://www.linkedin.com/in/jmsman3/',
    'depends': ['sale_management', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml',
    ],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
