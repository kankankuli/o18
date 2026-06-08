# -*- coding: utf-8 -*-



from odoo import models, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order"


    def _action_confirm(self):

        res = super(SaleOrderLine,self)._action_confirm()

        location = self.env.ref('stock.stock_location_stock')

        for line in self.order_line:
            product = line.product_id
            qty = line.product_uom_qty
            self.env['stock.quant']._update_available_quantity(product, location, -qty)
            # print('Updated Subtract Quantity', updated_qty)

        return res
