

{
    'name': 'Approval App',
    'depends': ['base'],
    'data': [
            'security/ir.model.access.csv',
            'view/approval_app.xml',
            ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
