from odoo import models,fields,api

class teacher_school(models.Model):
    _name = 'teacher.school'
    _description = 'Teacher School'
    name = fields.Char(required=True)
    qualification = fields.Char()
    experience = fields.Integer()
    join_date = fields.Date()
    service_date = fields.Date()

    subject_ids = fields.Many2many('subject.school')
    class_ids = fields.One2many('class.school', 'teacher_id')
    student_ids = fields.Many2many('student.school')