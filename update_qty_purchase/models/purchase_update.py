# -*- coding: utf-8 -*-
from odoo import models, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    # @api.multi
    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        location = self.env.ref('stock.stock_location_stock')

        for line in self.order_line:
            product = line.product_id
            qty = line.product_qty
            self.env['stock.quant']._update_available_quantity(product, location, qty)
            # print('Updated Quantity', updated_qty)

        return res
