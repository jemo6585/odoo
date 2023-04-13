
from odoorpc import ODOO
odoo = ODOO('0.0.0.0', port=8000)
odoo.login('jemo', 'reecejames934@gmail.com', 'jmin-dbpb-dwwy')
# Get all invoice ids
invoice_ids = odoo.env['account.account.invoice'].search([])

# Get invoice data for the first invoice
invoice_data = odoo.env['account.account.invoice'].read([invoice_ids[0]])
for i in invoice_data:
    print(i)