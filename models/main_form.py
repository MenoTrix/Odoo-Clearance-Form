from odoo import fields,models


class Form (models.Model):
    _name="main.form"
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name="emp_name"
    emp_name=fields.Many2one("hr.employee",string="الاسم")
    nationality=fields.Many2one(related="emp_name.country_id",string="الجنسية")
    title=fields.Many2one(related="emp_name.job_id",string="المسمي الوظيفي")
    empNo=fields.Char(related="emp_name.mobile_phone",string="الرقم الموظف")
    section=fields.Many2one(related="emp_name.department_id",string="القسم")
    location=fields.Many2one(related="emp_name.work_location_id",string="الإدارة")
    clearanceReason=fields.Html(string="سبب اخلاء الطرف")
    exit_reason=fields.Selection([
        ("vacation","اجازة"),("exit","نهاية خدمة")
    ],string="سبب الاخلاء ")
    
    # *****************************************
    # *****************************************

    # Employee Department
    
    emp_department_id=fields.Many2one("employee.department" ,string="الاسم")
    emp_department_date=fields.Date(related='emp_department_id.date' , string="التاريخ")
    emp_department_signature=fields.Char(related='emp_department_id.signature' , string="التوقيع")
    emp_department_reason=fields.Html(string="حدد")
    emp_department_reason=fields.Boolean(string="يخلي طرفة")

    
    # *****************************************
    # *****************************************
    # it Department
    
    
    it_department_name=fields.Many2one("it.department" ,string="الاسم")
    it_department_date=fields.Date(related='it_department_name.date' , string="التاريخ")
    it_department_signature=fields.Char(related='it_department_name.signature' , string="التوقيع")
    it_department_reason=fields.Html(string="حدد")
    it_department_clear=fields.Boolean(string="يخلي طرفة")
    
    
    # *****************************************
    # *****************************************
    # stores
    
    
    stores_department_name=fields.Many2one("store" ,string="الاسم")
    stores_department_date=fields.Date(related='stores_department_name.date' , string="التاريخ")
    stores_department_signature=fields.Char(related='stores_department_name.signature' , string="التوقيع")
    stores_department_reason=fields.Html(string="حدد")
    stores_department_clear=fields.Boolean(string="يخلي طرفة")

    # *****************************************
    # *****************************************
    # Administration
    
    
    administration_department_telecom=fields.Boolean(string="الاتصالات")
    administration_department_transportation=fields.Boolean(string="الحركة")
    administration_department_housing=fields.Boolean(string="الإسكان")
    administration_department_name=fields.Many2one("administration" ,string="الاسم")
    administration_department_date=fields.Date(related='administration_department_name.date' , string="التاريخ")
    administration_department_signature=fields.Char(related='administration_department_name.signature' , string="التوقيع")
    administration_department_reason=fields.Html(string="حدد")
    administration_department_clear=fields.Boolean(string="يخلي طرفة")
    
    
    # *****************************************
    # *****************************************
    # financial
    
    
    financial_department_name=fields.Many2one("financial" ,string="الاسم")
    financial_department_date=fields.Date(related='financial_department_name.date' , string="التاريخ")
    financial_department_signature=fields.Char(related='financial_department_name.signature' , string="التوقيع")
    financial_department_reason=fields.Html(string="حدد")
    financial_department_clear=fields.Boolean(string="يخلي طرفة")
    # *****************************************
    # *****************************************
    # Personnel
    
    
    personnel_department_loans=fields.Boolean(string="السلف")
    personnel_department_empCard=fields.Boolean(string="البطاقة الوظيفية")
    personnel_department_medicalCard=fields.Boolean(string="بطاقة التأمين")
    personnel_department_name=fields.Many2one("personnel" ,string="الاسم")
    personnel_department_date=fields.Date(related='personnel_department_name.date' , string="التاريخ")
    personnel_department_signature=fields.Char(related='personnel_department_name.signature' , string="التوقيع")
    personnel_department_reason=fields.Html(string="حدد")
    personnel_department_clear=fields.Boolean(string="يخلي طرفة")
    
    
    # *****************************************
    # *****************************************
    # Personnel use only
    
    
    personnel_use_clear=fields.Boolean(string="يخلي طرفة")
    personnel_use_reason=fields.Html(string="حدد")
    personnel_use_stamp=fields.Char(string="الختم")
    personnel_use_signature=fields.Char(string="التوقيع")
    personnel_use_date=fields.Date(string="التاريخ")
    
    
    