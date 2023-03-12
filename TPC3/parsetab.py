
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "BREAK_LINE IDLING SEPARATOR VALdic : EsEs : E SEPARATOR EsEs : EE : ITEMSITEMS : ITEM BREAK_LINE ITEMSITEMS : ITEMITEM : AT_CONCAT_CONC : VAL ':' VALITEM : LINGLING : IDLING ':' BREAK_LINE TS TS : T TSTS : TT : '#' VAL BREAK_LINE AT_TSAT_TS : AT_T BREAK_LINE AT_TSAT_TS : AT_T : '+' VAL ':' VAL"
    
_lr_action_items = {'VAL':([0,10,11,12,20,26,30,],[8,8,8,16,22,28,31,]),'IDLING':([0,10,11,],[9,9,9,]),'$end':([1,2,3,4,5,6,7,14,15,16,18,19,21,23,24,27,29,],[0,-1,-3,-4,-6,-7,-9,-2,-5,-8,-10,-12,-11,-15,-13,-15,-14,]),'SEPARATOR':([3,4,5,6,7,15,16,18,19,21,23,24,27,29,],[10,-4,-6,-7,-9,-5,-8,-10,-12,-11,-15,-13,-15,-14,]),'BREAK_LINE':([5,6,7,13,16,18,19,21,22,23,24,25,27,29,31,],[11,-7,-9,17,-8,-10,-12,-11,23,-15,-13,27,-15,-14,-16,]),':':([8,9,28,],[12,13,30,]),'#':([17,19,23,24,27,29,],[20,20,-15,-13,-15,-14,]),'+':([23,27,],[26,26,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'dic':([0,],[1,]),'Es':([0,10,],[2,14,]),'E':([0,10,],[3,3,]),'ITEMS':([0,10,11,],[4,4,15,]),'ITEM':([0,10,11,],[5,5,5,]),'AT_CONC':([0,10,11,],[6,6,6,]),'LING':([0,10,11,],[7,7,7,]),'TS':([17,19,],[18,21,]),'T':([17,19,],[19,19,]),'AT_TS':([23,27,],[24,29,]),'AT_T':([23,27,],[25,25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> dic","S'",1,None,None,None),
  ('dic -> Es','dic',1,'p_1','parser.py',27),
  ('Es -> E SEPARATOR Es','Es',3,'p_2','parser.py',38),
  ('Es -> E','Es',1,'p_3','parser.py',42),
  ('E -> ITEMS','E',1,'p_4','parser.py',46),
  ('ITEMS -> ITEM BREAK_LINE ITEMS','ITEMS',3,'p_5','parser.py',50),
  ('ITEMS -> ITEM','ITEMS',1,'p_6','parser.py',54),
  ('ITEM -> AT_CONC','ITEM',1,'p_7','parser.py',61),
  ('AT_CONC -> VAL : VAL','AT_CONC',3,'p_8','parser.py',65),
  ('ITEM -> LING','ITEM',1,'p_9','parser.py',69),
  ('LING -> IDLING : BREAK_LINE TS','LING',4,'p_10','parser.py',73),
  ('TS -> T TS','TS',2,'p_11','parser.py',77),
  ('TS -> T','TS',1,'p_12','parser.py',82),
  ('T -> # VAL BREAK_LINE AT_TS','T',4,'p_13','parser.py',86),
  ('AT_TS -> AT_T BREAK_LINE AT_TS','AT_TS',3,'p_14','parser.py',90),
  ('AT_TS -> <empty>','AT_TS',0,'p_15','parser.py',94),
  ('AT_T -> + VAL : VAL','AT_T',4,'p_16','parser.py',98),
]
