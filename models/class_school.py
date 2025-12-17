from odoo import models ,fields , api


class SchoolClass(models.Model):
    _name = 'class.school'
    _description = 'Class'

    name = fields.Char(required=True)
    teacher_id = fields.Many2one('teacher.school')
    section_ids = fields.One2many('section.school', 'class_id')
    student_ids = fields.One2many('student.school', 'class_id')
    subject_ids = fields.Many2many('subject.school')
