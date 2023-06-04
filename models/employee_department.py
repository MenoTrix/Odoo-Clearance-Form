from odoo import fields,models


class Department (models.Model):
    _name="employee.department"
    name=fields.Char(string="الاسم")
    date=fields.Date(string="التاريخ")
    signature=fields.Char(string="التوقيع")
    
    