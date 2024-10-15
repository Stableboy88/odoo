{
    'name': 'Currency Sync',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Sync currency rates from Bangkok Bank API',
    'description': """
        This module syncs currency rates from the Bangkok Bank API.
    """,
    'author': 'Stableboy',
    'depends': ['base'],
    'data': [
        'views/currency_sync_views.xml',
    ],
    'installable': True,
    'application': True,
}