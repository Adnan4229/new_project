from odoo import models, fields

class SchoolFee(models.Model):
    _name = 'fee.school'
    _description = 'Fee'

    student_id = fields.Many2one('student.school')
    amount = fields.Float()
    month = fields.Selection([
        ('jan', 'January'),
        ('feb', 'February')
    ])
    state = fields.Selection([
        ('draft', 'Draft'),
        ('paid', 'Paid')
    ], default='draft')