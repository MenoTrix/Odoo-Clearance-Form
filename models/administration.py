from odoo import fields,models


class Administration (models.Model):
    _name="administration"
    telecom=fields.Boolean(string="الاتصالات")
    transportation=fields.Boolean(string="الحركة")
    housing=fields.Boolean(string="الإسكان")
    name=fields.Char(string="الاسم")
    date=fields.Date(string="التاريخ")
    signature=fields.Char(string="التوقيع")
    
    