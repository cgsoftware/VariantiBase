# -*- encoding: utf-8 -*-

import wizard
import pooler
import time
from tools.translate import _
from osv import osv, fields
from tools.translate import _


class gen_righe_var(osv.osv_memory):
    _name = 'gen.righe.var'
    _description = 'Generazione Righe Varianti'
    _columns = {
       'dimensione_id': fields.many2one('product.variant.base.dimension', 'Varianti da Caricare', required=True, help="Seleziona la tabella variante di base da caricare"),
    }
    
    def genera(self,cr, uid, ids, context=None):
        # import pdb;pdb.set_trace()
        data = self.read(cr, uid, ids)
        lines = self.pool.get('product.variant.varianti.base').search(cr,uid,[('dimension_id','=',data[0]['dimensione_id'])])
        for riga_varbase in  self.pool.get('product.variant.varianti.base').browse(cr,uid,lines):         
            new_riga ={
                       'name':riga_varbase.name,
                       'dimension_id':context['record_id'],
                       }
            ok = self.pool.get('product.variant.dimension.value').create(cr,uid,new_riga)
        return {'type': 'ir.actions.act_window_close'}
gen_righe_var()    