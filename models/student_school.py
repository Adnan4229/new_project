from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError, UserError

class StudentSchool(models.Model):
    _name = 'student.school'
    _description = 'Student'

    # Basic Information
    name = fields.Char(string="Full Name", required=True)
    roll_no = fields.Char(string="Roll Number")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    address = fields.Text(string="Address")


    # Additional Information
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute='_compute_age', store=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Gender")
    admission_date = fields.Date(string="Admission Date", default=fields.Date.today)
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    zip_code = fields.Char(string="Zip Code")

    # Relationships (optional)
    class_id = fields.Many2one('class.school', string="Class")
    section_id = fields.Many2one('section.school', string="Section")
    teacher_ids = fields.Many2many('teacher.school', string="Teachers")

    # Linked child records
    attendance_ids = fields.One2many('attendance.school', 'student_id', string="Attendance")
    fee_ids = fields.One2many('fee.school', 'student_id', string="Fees")

    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            if rec.dob:
                rec.age = date.today().year - rec.dob.year
            else:
                rec.age = 0

    @api.constrains('age')
    def _check_age(self):
        for rec in self:
            if rec.age and rec.age < 3:
                raise ValidationError('Student age must be at least 3 years.')

    @api.ondelete(at_uninstall=False)
    def _prevent_delete_active(self):
        for rec in self:
            if rec.state == 'active':
                raise UserError('Cannot delete active student.')
