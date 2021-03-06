# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2008 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields, osv

#
# Dimensions Definition
#
class product_variant_base_dimension(osv.osv):
    _name = "product.variant.base.dimension"
    _description = "Dimension Base"

    _columns = {
        'name' : fields.char('Dimension', size=64),
        'varianti_ids' : fields.one2many('product.variant.varianti.base', 'dimension_id', 'Dimension Values'),
    }

    _order = "name"


product_variant_base_dimension()


class product_variant_varianti_base(osv.osv):

    _name = "product.variant.varianti.base"
    _description = "Righe base Varianti"

    _columns = {
        'name' : fields.char('Dimension Value', size=64, required=True),
        'dimension_id' : fields.many2one('product.variant.base.dimension', 'Dimensione Base', required=True, ondelete='cascade'),
         
    }
    _order = "name"

product_variant_varianti_base()

