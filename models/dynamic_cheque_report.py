# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class dynamic_cheque_template(models.AbstractModel):
	_name='report.generate_dynamic_cheque_app.report_dynamic_check_print'

	def get_amount_in_word_line(self, payment_id, cheque_format):
		amount_word = payment_id.currency_id.amount_to_text(payment_id.amount)
		first_line = (amount_word[0:cheque_format.words_in_fl_line])
		s1 = cheque_format.words_in_fl_line
		s2 = cheque_format.words_in_fl_line + cheque_format.words_in_sc_line
		second_line = (amount_word[s1:s2])
		localdict = {
			'first_line' : first_line,
			'second_line': second_line
		}
		return localdict

	def _get_report_values(self, docids, data=None):
		wizard  = self.env['dynamic.cheque.wizard'].browse(docids)
		return {
				'doc_model': 'dynamic.cheque',
				'cheque_format' : wizard.cheque_format,
				'payment_id' : wizard.payment_id,
				'get_amount_in_word_line': self.get_amount_in_word_line,
				}

class report_paperformat(models.Model):
	_inherit = "report.paperformat"

	custom_report = fields.Boolean('Temp Formats', default=False)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: