
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "BREAK_LINE IDLING SEPARATOR VALdic : EsEs : E SEPARATOR EsEs : EE : ITEMSITEMS : ITEM ITEMSITEMS : ITEMITEM : AT_CONC BREAK_LINEITEM : LINGAT_CONC : VAL ':' VALLING : IDLING ':' BREAK_LINE TS TS : T TSTS : TT : '#' VAL BREAK_LINE AT_TSAT_TS : AT_T AT_TSAT_TS : AT_T : '+' VAL ':' VAL BREAK_LINE"
    
_lr_action_items = {'VAL':([0,5,7,10,12,13,18,19,20,21,23,24,25,26,27,29,31,],[8,8,-8,8,-7,16,-10,-12,22,-11,-15,-13,-15,28,-14,30,-16,]),'IDLING':([0,5,7,10,12,18,19,21,23,24,25,27,31,],[9,9,-8,9,-7,-10,-12,-11,-15,-13,-15,-14,-16,]),'$end':([1,2,3,4,5,7,11,12,15,18,19,21,23,24,25,27,31,],[0,-1,-3,-4,-6,-8,-5,-7,-2,-10,-12,-11,-15,-13,-15,-14,-16,]),'SEPARATOR':([3,4,5,7,11,12,18,19,21,23,24,25,27,31,],[10,-4,-6,-8,-5,-7,-10,-12,-11,-15,-13,-15,-14,-16,]),'BREAK_LINE':([6,14,16,22,30,],[12,17,-9,23,31,]),':':([8,9,28,],[13,14,29,]),'#':([17,19,23,24,25,27,31,],[20,20,-15,-13,-15,-14,-16,]),'+':([23,25,31,],[26,26,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'dic':([0,],[1,]),'Es':([0,10,],[2,15,]),'E':([0,10,],[3,3,]),'ITEMS':([0,5,10,],[4,11,4,]),'ITEM':([0,5,10,],[5,5,5,]),'AT_CONC':([0,5,10,],[6,6,6,]),'LING':([0,5,10,],[7,7,7,]),'TS':([17,19,],[18,21,]),'T':([17,19,],[19,19,]),'AT_TS':([23,25,],[24,27,]),'AT_T':([23,25,],[25,25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> dic","S'",1,None,None,None),
  ('dic -> Es','dic',1,'p_1','parser.py',21),
  ('Es -> E SEPARATOR Es','Es',3,'p_2','parser.py',25),
  ('Es -> E','Es',1,'p_3','parser.py',29),
  ('E -> ITEMS','E',1,'p_4','parser.py',33),
  ('ITEMS -> ITEM ITEMS','ITEMS',2,'p_5','parser.py',37),
  ('ITEMS -> ITEM','ITEMS',1,'p_6','parser.py',41),
  ('ITEM -> AT_CONC BREAK_LINE','ITEM',2,'p_7','parser.py',45),
  ('ITEM -> LING','ITEM',1,'p_8','parser.py',49),
  ('AT_CONC -> VAL : VAL','AT_CONC',3,'p_9','parser.py',53),
  ('LING -> IDLING : BREAK_LINE TS','LING',4,'p_10','parser.py',57),
  ('TS -> T TS','TS',2,'p_11','parser.py',61),
  ('TS -> T','TS',1,'p_12','parser.py',65),
  ('T -> # VAL BREAK_LINE AT_TS','T',4,'p_13','parser.py',69),
  ('AT_TS -> AT_T AT_TS','AT_TS',2,'p_14','parser.py',73),
  ('AT_TS -> <empty>','AT_TS',0,'p_15','parser.py',77),
  ('AT_T -> + VAL : VAL BREAK_LINE','AT_T',5,'p_16','parser.py',81),
]
