from odoo import fields,models


class Stores (models.Model):
    _name="store"
    name=fields.Char(string="الاسم")
    date=fields.Date(string="التاريخ")
    signature=fields.Char(string="التوقيع")
    # reason=fields.Html(string="حدد")
    # clear=fields.Boolean(string="يخلي طرفة")
    # notClear=fields.Boolean(string="لا يخلي طرفة ")
    
    