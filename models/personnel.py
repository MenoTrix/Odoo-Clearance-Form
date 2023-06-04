from odoo import fields,models


class Personnel (models.Model):
    _name="personnel"
    name=fields.Char(string="الاسم")
    date=fields.Date(string="التاريخ")
    loans=fields.Boolean(string="السلف")
    empCard=fields.Boolean(string="البطاقة الوظيفية")
    medicalCard=fields.Boolean(string="بطاقة التأمين")
    signature=fields.Char(string="التوقيع")
    manager_signature=fields.Char(string="توقيع المدير")
    manager_name=fields.Char(string="اسم المدير")
    # reason=fields.Html(string="حدد")
    # clear=fields.Boolean(string="يخلي طرفة")
    # notClear=fields.Boolean(string="لا يخلي طرفة ")