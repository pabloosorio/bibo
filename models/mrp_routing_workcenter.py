from odoo import models, fields, api

class MrpRoutingWorkorder(models.Model):
    _inherit = 'mrp.routing.workcenter'
    payment = fields.Float(string="Pago de empleado por pza.")

class MrpWorkerCenter(models.Model):
	_inherit = "mrp.workcenter"
	mesa_default = fields.Many2one('board',string="Mesa por defecto")