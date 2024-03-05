{
    'name': "stock_transport",
    'version': '1.0',
    'depends': ['stock_picking_batch', 'fleet'],
    'author': "hatr-odoo",
    'description': """
    Description text
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/stock_transport_fleet_category_views.xml',
        'views/stock_transport_stock_picking.xml',
        'views/stock_transport_stock_picking_batch.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'license': 'OEEL-1'
}
