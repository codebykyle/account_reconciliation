{
    'name': 'Account Reconciliation',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Accounting',
    'summary': 'Extends bank reconciliation and matching tools',
    'author': 'Adomi',
    'website': 'https://adomi.io',
    'license': 'LGPL-3',
    'depends': [
        'account',
        'account_statement_base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/views_account_account.xml',
        'views/menu_account_reconciliation.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
