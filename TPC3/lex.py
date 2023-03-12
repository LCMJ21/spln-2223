import ply.lex as lex

literals = ['#', '+', ':']

tokens = ['IDLING', 'VAL', 'BREAK_LINE', 'SEPARATOR']

t_ignore = ' \t'

def t_IDLING(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*\.'
    return t

def t_VAL(t):
    r'[a-zA-Z0-9_]+' # Change back to r'[a-zA-Z0-9_]+'
    return t

def t_BREAK_LINE(t):
    r'\n+'
    return t

def t_SEPARATOR(t):
    r'---+\n+'
    return t



def t_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position IDK")
    t.lexer.skip(1)

lexer = lex.lex()