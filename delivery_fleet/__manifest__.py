# See LICENSE file for full copyright and licensing details.

{
    'name': 'Delivery Fleet',
    'version': '13.0.1.0.0',
    'category': 'Stock',
    'license': 'AGPL-3',
    'author': 'Said Yahia',
    'summary': 'Delivery Fleet',
    'depends': [
        'stock','stock_planning'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',

        'views/car_view.xml',
        'views/driver_view.xml',

    ],
    'installable': True,
    'auto_install': False,
}
