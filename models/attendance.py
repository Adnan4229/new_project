from odoo import models, fields

class SchoolAttendance(models.Model):
    _name = 'attendance.school'
    _description = 'Attendance'

    date = fields.Date(default=fields.Date.today)
    student_id = fields.Many2one('student.school', required=True)
    class_id = fields.Many2one('class.school', required=True)
    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent')
    ], default='present')