# See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
import time
from odoo.exceptions import UserError, ValidationError


class CarNo(models.Model):
    _name = "car.no"
    _inherit = ['car.no', 'portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    name = fields.Char(tracking=3)
    user_id = fields.Many2one('res.users', string='Driver', required=1, tracking=3)


    _sql_constraints = [
        ('name_driver_uniq', 'unique(name,user_id)', "Car name and Driver already Exist before !"),
    ]


class Car_no_driver(models.Model):
    _name = 'car.no.driver'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']

    _rec_name = 'stock_picking_id'
    _order = 'id desc'
    state = fields.Selection([
        ('draft', 'Draft'),
        ('on_the_way', 'On the way'),
        ('delivered', 'Delivered'),
        ('delivered_partially', 'Delivered partially'),

        ('not_delivered', 'Not delivered'),
    ], string='Status', copy=False, index=True, tracking=3, default='draft')
    car_id = fields.Many2one('car.no', string='Car', tracking=3)

    user_id = fields.Many2one('res.users', string='Driver', tracking=3)
    partner_id = fields.Many2one('res.partner', string='Customer', tracking=3)
    stock_picking_id = fields.Many2one('stock.picking', string='Delivery no', tracking=3)
    delivery_date = fields.Datetime(string='Delivery Date',related='stock_picking_id.scheduled_date', tracking=3)

    desc = fields.Text(string='Desc', tracking=3)
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company)

    country_id = fields.Many2one(related='company_id.country_id')

    state_id = fields.Many2one(related='partner_id.state_id', string='Area', readonly=False)
    zone_id = fields.Many2one(related="partner_id.zone_id", readonly=True, store=True)
    block_no = fields.Char(related='partner_id.block_no', readonly=False)
    parcel = fields.Char(related='partner_id.parcel', readonly=False)
    building_no = fields.Char(related='partner_id.building_no', readonly=False)
    street = fields.Char(related='partner_id.street', readonly=False)
    mobile = fields.Char(related='partner_id.mobile',string='Customer Mobile')
    problem = fields.Selection([
        ('1', 'Customer Change date'),
        ('2', 'customer canceled'),
        ('3', 'customer needs repair'),
        ('4', 'missing products'),

        ('5', 'customer no answer'),
        ('6', 'no time for delivery'),
        ('7', 'damage item'),
        ('8', 'wrong mobile'),
        ('9', 'wrong address'),
        ('10', 'wrong products'),
        ('11', 'wrong quantity'),
        ('12', 'no space in customer house'),

    ], string='Problem', copy=False, index=True, tracking=3,)
    # employee_id = fields.Many2one(comodel_name='hr.employee', string='employee')


Car_no_driver()
