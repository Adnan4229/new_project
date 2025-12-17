from odoo import models, fields, api


class SchoolResult(models.Model):
    _name = 'result.school'
    _description = 'Result'

    student_id = fields.Many2one('student.school', string="Student", required=True)
    exam_id = fields.Many2one('exam.school', string="Exam")
    marks = fields.Float(string="Marks")
    grade = fields.Char(string="Grade", compute='_compute_grade', store=True)

    @api.depends('marks')
    def _compute_grade(self):
        for rec in self:
            if rec.marks >= 80:
                rec.grade = 'A'
            elif rec.marks >= 60:
                rec.grade = 'B'
            else:
                rec.grade = 'C'
