from odoo import models,fields,api

class teacher_school(models.Model):
    _name = 'teacher.school'
    _description = 'Teacher School'
    name = fields.Char(string='Name')
    subject = fields.Char(string='Subject')
    qualification = fields.Char(string='Qualification')
    experience = fields.Char(string='Experience')
    join_date = fields.Datetime(string='Join Date')
    service_date = fields.Datetime(string='Service Date')
    # subject_ids = fields.Many2many(string='school.subject')
    # class_ids =fields.One2many('school.class',string='Class IDs')
    # student_ids = fields.Many2many('school.student',string='Students',)
