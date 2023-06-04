from odoo import fields,models


class ItDepartment (models.Model):
    _name="it.department"
    name=fields.Char(string="الاسم")
    date=fields.Date(string="التاريخ")
    signature=fields.Char(string="التوقيع")
    
    