# See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api,_
import time
from odoo.exceptions import UserError, ValidationError


class picking(models.Model):
    _inherit = 'stock.picking'

    def write(self, vals):
        res= super(picking, self).write(vals)

        for each in self:
            if 'car_no' in vals :
                print('ccccccc',vals['car_no'])
                drivers=self.env['car.no'].search([('id','=',vals['car_no'])])
                driver_id=drivers and drivers[0].user_id or False
                repo=self.env['car.no.driver'].search([('stock_picking_id','=',each.id)])
                if len(repo):
                    repo[0].car_id=vals['car_no']
                    repo[0].user_id=driver_id and driver_id.id or False

                else:
                    v= {'partner_id': each.partner_id and each.partner_id.id or False ,
                         'user_id': driver_id and driver_id.id or False,
                         'car_id': vals['car_no'],
                         'stock_picking_id': each.id,
                         'delivery_date': each.scheduled_date,

                         }
                    print('vvvvvvvvvvv',v)
                    self.env['car.no.driver'].create(
                        {'partner_id': each.partner_id and each.partner_id.id or False,
                         'user_id': driver_id and driver_id.id or False,
                         'car_id': vals['car_no'],
                         'stock_picking_id': each.id,
                         'delivery_date': each.scheduled_date,

                         }
                       )


        return res


