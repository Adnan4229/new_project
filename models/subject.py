from odoo import models, fields

class SchoolSubject(models.Model):
    _name = 'subject.school'
    _description = 'Subject'
    name = fields.Char(required=True)
    code = fields.Char()
    teacher_ids = fields.Many2many('teacher.school')
    class_ids = fields.Many2many('class.school')