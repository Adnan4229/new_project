from odoo import models, fields, api


class School(models.Model):
    _name = 'student.school'
    _description = 'School Management System'


    name = fields.Char(string='Name')
    roll_no = fields.Char(string='Roll No.')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')
    email = fields.Char(string='Email')
    img = fields.Image(string='Image')
    dob = fields.Datetime(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    age = fields.Integer(string='Age')
    admission_date = fields.Datetime(string='Date of Admission')
    city = fields.Char(string='City')
    state = fields.Char(string='State')
    zip_code = fields.Char(string='Zip Code')
