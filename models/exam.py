from odoo import models, fields

class SchoolExam(models.Model):
    _name = 'exam.school'
    _description = 'Exam'

    name = fields.Char(required=True)
    class_id = fields.Many2one('class.school')
    subject_id = fields.Many2one('subject.school')
    exam_date = fields.Date()
    result_ids = fields.One2many('result.school', 'exam_id')
    result_ids = fields.One2many('result.school', 'exam_id', string="Results")