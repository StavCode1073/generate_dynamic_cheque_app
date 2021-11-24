# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class DynamicCheque(models.Model):
	_name = 'dynamic.cheque'
	_description = "Dynamic Cheque"

	name = fields.Char(string="Cheque Format", required=True )
	partner_id = fields.Char(string="Partner")
	cheque_hight = fields.Float(string='Height')
	cheque_width = fields.Float(string='Width')
	ac_pay = fields.Boolean(string="A/c Pay")
	ac_top_margin = fields.Float(string="Top Margin")
	ac_left_margin = fields.Float(string='Left Margin')
	ac_font_size = fields.Float(string='Font Size')
	top_margin = fields.Float(string="Top Margin")
	left_margin = fields.Float(string='Left Margin')
	font_size = fields.Float(string="Font Size")
	char_spacing = fields.Float(string="Character Spacing")
	payee_top_margin = fields.Float(string='Top Margin')
	payee_left_margin = fields.Float(string='Left Margin')
	payee_width = fields.Float(string="Width")
	payee_font_size = fields.Float(string="Font Size")
	af_top_margin = fields.Float(string='Top Margin')
	af_left_margin = fields.Float(string='Left Margin')
	af_width = fields.Float(string="Width")
	af_font_size = fields.Float(string="Font Size")
	af_currency_symbol = fields.Boolean(string="Currency Symbol")
	af_currency_symbol_position = fields.Selection([('before','Before'),('after','After')],string="Currency Symbol Position", default='before')
	first_line_amount = fields.Char(string='First Line')
	second_line_amount = fields.Char(string='Second Line')
	fl_top_margin = fields.Float(string='First Line Top Margin')
	fl_left_margin = fields.Float(string='First Line Left Margin')
	fl_width = fields.Float(string="First Line Width")
	words_in_fl_line = fields.Integer(string="No. of Word in First Line")
	sc_top_margin = fields.Float(string='Second Line Top Margin')
	sc_left_margin = fields.Float(string='Second Line Left Margin')
	sc_width = fields.Float(string='Second Line Width')
	words_in_sc_line = fields.Integer(string='No. of Word in Second Line')
	sc_font_size = fields.Float(string='Font Size')
	sc_currency_name = fields.Boolean(string='Currency Name')
	sc_currency_name_position = fields.Selection([('before','Before'),('after','After')], string="Currency Name Position", default='before')
	comapny_name = fields.Boolean(string='Company Name')
	comp_font_size = fields.Float(string='Font Size')
	comp_top_margin = fields.Float(string="Top Margin")
	comp_left_margin = fields.Float(string="Left Margin")
	sb_width = fields.Float(string='Width')
	sb_hight = fields.Float(string='Height')
	sb_top_margin = fields.Float(string='Top Margin')
	sb_left_margin = fields.Float(string='Left Margin')
	
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: