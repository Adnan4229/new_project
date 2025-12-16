from odoo import models, fields, api
class SchoolParent(models.Model):
    _name = 'parent.school'
    _description = 'School Parent'
    _order = 'parent_name'
    parent_name = fields.Char(string='Parent Name')
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email Address')
    address = fields.Char(string='Address')
    # student_ids = fields.One2many(string='Students',)