from odoo import models, fields, api
from odoo.addons import decimal_precision as dp

class BiboProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    ref_bibo = fields.Char('Referencia')

class AccountInvoice(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'

    @api.one
    def _compute_count_line(self):
        self.count_line = len(self.invoice_line_ids)

    count_line = fields.Integer(String='Cantidad de lineas de la factura', compute='_compute_count_line')

class DebtCustomerReport(models.AbstractModel):
    _name = 'report.debt_customer.customer_debt_report'


    @api.model
    def render_html(self, docids, data=None):
        """Render report template"""
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('debt_customer.customer_debt_report')

        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': data['form'],
            'dates': data['dates'],
        }

        return report_obj.render('debt_customer.customer_debt_report', docargs)

class Product(models.Model):
    _inherit = "product.product"
    stock_sventa = fields.Float(string="Material Disponible",digits=dp.get_precision('Product Unit of Measure'))

    @api.depends('stock_quant_ids', 'stock_move_ids')
    def _compute_quantities(self):
        res = self._compute_quantities_dict(self._context.get('lot_id'), self._context.get('owner_id'), self._context.get('package_id'), self._context.get('from_date'), self._context.get('to_date'))
        for product in self:
            product.stock_sventa = (res[product.id]['qty_available'])-(res[product.id]['outgoing_qty'])
            product.qty_available = res[product.id]['qty_available']
            product.incoming_qty = res[product.id]['incoming_qty']
            product.outgoing_qty = res[product.id]['outgoing_qty']
            product.virtual_available = res[product.id]['virtual_available']


    #@api.depends('outgoing_qty', 'qty_available')
    #def _compute_smventa(self):
    #    self.stock_sventa = (self.qty_available) - (self.outgoing_qty)
