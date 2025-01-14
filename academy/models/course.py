from odoo import api, fields, models

class Course(models.Model):
    _name ="academy.course"
    _description = "Course Info"

    name = fields.Char(string="Title", required= True)
    active = fields.Boolean(string="Active", default=True)

    description = fields.Text(string='Description')
    level = fields.Selection(string="Level",
                             selection=[
                                 ('beginner','Beginner'),
                                 ('intermediate','Intermediate'),
                                  ('advanced','Advanced'),
                             ],
                             copy=False)
    sesion_ids = fields.One2many(comodel_name='academy.session', string='Sessions', inverse_name='course_id')
    currency_id = fields.Many2One(comodel_name="res.currency", string="Precio", default= lambda self:self.env.company.currency_id.id)
    base_price = fields.Monetary(string="Precio base", currency_field= "currency_id")
    additional_fee = fields.Monetary(string="Fee Adicional", currency_field= "currency_id")
    total_price = fields.Monetary(string="Precio total", currency_field= "currency_id", compute="_compute_total_price")
    
    @api.depends("base_price", "additional_fee")
    def _compute_total_price(self):
        for record in self:
            if(record.base_price < 0):
                raise ValidationError(('EL precio no puede ser negativo'))
            record.total_price = record.base_price + record.additional_fee
