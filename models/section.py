from odoo import models, fields

class SchoolSection(models.Model):
    _name = 'section.school'
    _description = 'Section'
    name = fields.Char(required=True)
    class_id = fields.Many2one('class.school')
    student_ids = fields.One2many('student.school', 'section_id')