from odoo import models, fields, api

class Board(models.Model):
    _name = 'board'
    name = fields.Char('Mesa')
    table_lines = fields.One2many('board.line', 'table_id', string='Table lines')

class BoardLine(models.Model):
    _name = 'board.line'
    table_id = fields.Many2one('board', string='Table Reference', required=True, ondelete='cascade',
                              index=True, copy=False)
    employee_id = fields.Many2one('hr.employee', string="Empleado")
    #@api.onchange('employee_id')
    #def set_empleados(self):
    #    board = self.table_id
    #    lista = {}
    #    orden=self
    #    t = self.env['board.line'].search([('table_id', '=', board.id)])
    #    ta = self.env['hr.employee'].search([('id', 'in', t)])
    #    return {
    #        'domain': {
    #            'employee_id': [('project_id', '=', ta)]
    #        }
    #    }



