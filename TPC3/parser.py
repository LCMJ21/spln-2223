from dataclasses import dataclass
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

@dataclass
class LanguageEntry:
    language: str
    term: dict

def p_1(p): 
    "dic : Es"
    for term in p[1]: # <dt><h3><b>Coffee</b></h3></dt><dd>- black hot drink</dd>
        parser.html += f"""
        <h2><b>{list(term[-1].term)[0]}</b></h2>
        <dl>"""
        for key, value in term[:-1]:
            parser.html += f"""
            <dt><h3><b>{key}</b></h3></dt><dd>- {value}</dd>"""
        parser.html += """
        </dl>"""

def p_2(p):
    "Es : E SEPARATOR Es"
    p[0] = [p[1]] + p[3]

def p_3(p):
    "Es : E"
    p[0] = [p[1]]

def p_4(p):
    "E : ITEMS"
    p[0] = p[1]

def p_5(p):
    "ITEMS : ITEM BREAK_LINE ITEMS"
    p[0] = [p[1]] + p[3]

def p_6(p):
    "ITEMS : ITEM"
    if p[1] is not None:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_7(p):
    "ITEM : AT_CONC"
    p[0] = p[1]

def p_8(p):
    "AT_CONC : VAL ':' VAL"
    p[0] = (p[1], p[3])

def p_9(p):
    "ITEM : LING"
    p[0] = p[1]

def p_10(p):
    "LING : IDLING ':' BREAK_LINE TS "
    p[0] = LanguageEntry(p[1], p[4])

def p_11(p):
    "TS : T TS"
    p[2].update(p[1])
    p[0] = p[2]

def p_12(p):
    "TS : T"
    p[0] = p[1]

def p_13(p):
    "T : '#' VAL BREAK_LINE AT_TS"
    p[0] = {p[2]: p[4]}

def p_14(p):
    "AT_TS : AT_T BREAK_LINE AT_TS"
    p[0] = [p[1]] + p[2]

def p_15(p):
    "AT_TS : "
    p[0] = []

def p_16(p):
    "AT_T : '+' VAL ':' VAL"
    p[0] = (p[2], p[4])

def p_error(p):
    print('Syntax error: ', p)
    parser.success = False

# Build the parser
parser = yacc.yacc()
parser.success = True
parser.html ="""
<h1>English dictionary<code><br /></code></h1>
<ul>"""

def readFile(filename):

    # Read line from input and parse it
    f = open(filename, "r", encoding="utf-8")
    program = f.read()
    parser.parse(program)
    f.close()
    if parser.success:
        print(f"{filename} -> Parsing completed")
        parser.html += """
</ul>"""
        open(f"{filename[:-4]}.html", "w", encoding="utf-8").write(parser.html)


readFile("first_example.txt")
#readFile("medicina.txt")