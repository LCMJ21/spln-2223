import ply.yacc as yacc
from lex import tokens

"""
Dic -> meta E*

E -> Items *
Item -> AT-Conc (p.e. Area)
    | Ling

AT-Conc -> Id ':' val

Ling -> IdLing ':' T*

T -> Termo AT-T*

AT-T -> '+' id ':' valor
"""

def p_1(p): 
    "dic : Es"
    pass

def p_2(p):
    "Es : E SEPARATOR Es"
    pass

def p_3(p):
    "Es : E"
    pass

def p_4(p):
    "E : ITEMS"
    pass

def p_5(p):
    "ITEMS : ITEM ITEMS"
    pass

def p_6(p):
    "ITEMS : ITEM"
    pass

def p_7(p):
    "ITEM : AT_CONC BREAK_LINE"
    pass

def p_8(p):
    "ITEM : LING"
    pass

def p_9(p):
    "AT_CONC : VAL ':' VAL"
    pass

def p_10(p):
    "LING : IDLING ':' BREAK_LINE TS "
    pass

def p_11(p):
    "TS : T TS"
    pass

def p_12(p):
    "TS : T"
    pass

def p_13(p):
    "T : '#' VAL BREAK_LINE AT_TS"
    pass

def p_14(p):
    "AT_TS : AT_T AT_TS"
    pass

def p_15(p):
    "AT_TS : "
    pass

def p_16(p):
    "AT_T : '+' VAL ':' VAL BREAK_LINE"
    pass

def p_error(p):
    print('Syntax error: ', p)
    parser.success = False

# Build the parser
parser = yacc.yacc()
parser.success = True

def readFile(filename):

    # Read line from input and parse it
    f = open(filename, "r", encoding="utf-8")
    program = f.read()
    parser.parse(program)
    f.close()
    if parser.success:
        print(f"{filename} -> Parsing completed")

readFile("first_example.txt")
readFile("medicina.txt")