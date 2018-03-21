# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2010-2012 OpenERP s.a. (<http://openerp.com>).
#
#
#    Author : Smerghetto Daniel  (Omniasolutions)
#    mail:daniel.smerghetto@omniasolutions.eu
#    Copyright (c) 2014 Omniasolutions (http://www.omniasolutions.eu) 
#    All Right Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

'''
Created on Dec 18, 2017

@author: daniel
'''
from odoo import models
from odoo import fields
from odoo import api
from odoo import _
import logging
import datetime


class MrpProduction(models.Model):

    _name = "mrp.production"
    _inherit = ['mrp.production']

    state = fields.Selection(selection_add=[('external', 'External Production')])
    external_partner = fields.Many2one('res.partner', string='External Partner')

    @api.model
    @api.returns('self', lambda value:value.id)
    def create(self, vals):
        return super(MrpProduction, self).create(vals)

    def getSupplierLocation(self):
        for lock in self.env['stock.location'].search([('usage', '=', 'supplier'),
                                                       ('active', '=', True),
                                                       ('company_id', '=', False)]):
            return lock.id
        return False

    @api.multi
    def button_produce_externally(self):
        values = {}
        location = self.routing_id.location_id
        partner = location.partner_id
        if not partner:
            partner = self.env['res.partner'].search([], limit=1)
        if not location:
            location = self.getSupplierLocation()
        values['external_partner'] = partner.id
        values['move_raw_ids'] = [(6, 0, self.move_raw_ids.ids)]
        values['move_finished_ids'] = [(6, 0, self.move_finished_ids.ids)]
        values['partner_location_id'] = location.id
        obj_id = self.env['mrp.production.externally.wizard'].create(values)
        self.env.cr.commit()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'mrp.production.externally.wizard',
            'view_mode': 'form,tree',
            'view_type': 'form',
            'res_id': obj_id.id,
            'context': {'wizard_id': obj_id.id},
            'target': 'new',
        }

    @api.multi
    def button_cancel_produce_externally(self):
        stockPickingObj = self.env['stock.picking']
        for manOrderBrws in self:
            stockPickList = stockPickingObj.search([('origin', '=', manOrderBrws.name)])
            for pickBrws in stockPickList:
                pickBrws.action_cancel()
            manOrderBrws.write({'state': 'confirmed'})
