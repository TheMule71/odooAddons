# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011-2013 Serpent Consulting Services (<http://www.serpentcs.com>)
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
############################################################################
import time

from openerp.osv import fields, osv
from openerp.tools.translate import _

class hr_attendance_error(osv.osv_memory):

    _inherit = 'hr.attendance.error'

    def print_report(self, cr, uid, ids, context=None):
        emp_ids = []
        data_error = self.read(cr, uid, ids, context=context)[0]
        date_from = data_error['init_date']
        date_to = data_error['end_date']
        cr.execute("SELECT id FROM hr_attendance WHERE employee_id IN %s AND to_char(name,'YYYY-mm-dd')<=%s AND to_char(name,'YYYY-mm-dd')>=%s AND action IN %s ORDER BY name" ,(tuple(context['active_ids']), date_to, date_from, tuple(['sign_in','sign_out'])))
        attendance_ids = [x[0] for x in cr.fetchall()]
        if not attendance_ids:
            raise osv.except_osv(_('No Data Available !'), _('No records are found for your selection!'))
        attendance_records = self.pool.get('hr.attendance').browse(cr, uid, attendance_ids, context=context)

        for rec in attendance_records:
            if rec.employee_id.id not in emp_ids:
                emp_ids.append(rec.employee_id.id)
        data_error['emp_ids'] = emp_ids
        datas = {
             'ids': ids,
             'model': 'hr.employee',
             'form': data_error
        }
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'hr.attendance.error.webkit',
            'datas': datas,
        }

hr_attendance_error()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: