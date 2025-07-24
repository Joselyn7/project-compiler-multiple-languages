import ply.lex as lex

# Palabras reservadas
reserved = {
    'let': 'LET',
    'var': 'VAR',
    'const': 'CONST',
    'function': 'FUNCTION',
    'return': 'RETURN'
}

# Lista de tokens (se combinan los del diccionario y los tokens personalizados)
tokens = [
    'IDENTIFIER', 'NUMBER',
    'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'SEMICOLON', 'COMMA'
] + list(reserved.values())

# Expresiones regulares simples para tokens
t_ASSIGN    = r'='
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_SEMICOLON = r';'
t_COMMA     = r','

# Identificadores y palabras reservadas
def t_IDENTIFIER(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Verifica si es palabra reservada
    return t

# Números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabs
t_ignore = ' \t'

# Saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en línea {t.lineno}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()


