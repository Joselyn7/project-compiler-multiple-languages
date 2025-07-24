def t_FUNCTION_DEF(t):
    r'\b(?:int|float|char|void)\s+[a-zA-Z_]\w*\s*\(\s*(?:[a-zA-Z_]\w*\s+[a-zA-Z_]\w*\s*)*\)\s*{'
    return t

def t_FUNCTION_DECL(t):
    r'\b(int|float|char|void)\s+[a-zA-Z_]\w*\(\s*(?:.+?)?\s*\);?'
    return t

def t_ASSIGN(t):
    r'[a-zA-Z_]\w*\s*='
    t.value = t.value.rstrip('\n')
    return t

def t_RETURN(t):
    r'\breturn\b\s+([a-zA-Z_]|\d+)\w*(\s*[\+\-%\*/]\s*([a-zA-Z_]|\d+)\w*)*\s*;?'
    return t

def t_FUNCTION_CALL(t):
    r'\b(?:[a-zA-Z_]\w*\.)*[a-zA-Z_]\w*\(\s*(?:.+?)?\s*\);?'
    return t

def t_CALCULATION_OR_IDENTIFIER(t):
    r'([a-zA-Z_]|\d+)\w*(\s*[\+\-%\*/]\s*([a-zA-Z_]|\d+)\w*)*\s*;?'
    return t

def t_CLASS(t):
    r'\bclass\b\s+[a-zA-Z_]\w*\s*(\([^)]*\))?\s*{'
    return t

def t_BRANCH(t):
    r'\bif\b|\belse\s+if\b|\belse\b'
    return t

def t_FOR_LOOP(t):
    r'\bfor\s*\(\s*.*?\s*\)\s*{'
    return t

def t_WHILE_LOOP(t):
    r'\bwhile\s*\(\s*.*?\s*\)\s*{'
    return t

t_ignore = ' \t\n}'

def t_error(t):
    print(f"Caracter inválido: {t.value[0]}")
    t.lexer.skip(1)