from odoo import fields,models


class Financial (models.Model):
    _name="financial"
    name=fields.Char(string="الاسم")
    date=fields.Date(string="التاريخ")
    signature=fields.Char(string="التوقيع")
    
    