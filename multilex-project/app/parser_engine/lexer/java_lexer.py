import ply.lex as lex

tokens = [
    'INT', 'RETURN', 'PUBLIC', 'STATIC', 'VOID',
    'IDENTIFIER', 'NUMBER',
    'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'SEMICOLON'
]

t_INT       = r'int'
t_RETURN    = r'return'
t_PUBLIC    = r'public'
t_STATIC    = r'static'
t_VOID      = r'void'
t_ASSIGN    = r'='
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_SEMICOLON = r';'

def t_IDENTIFIER(t):
    r'[a-zA-Z_]\w*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
