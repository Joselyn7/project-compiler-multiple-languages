def t_JAVASCRIPT(t):
    r'\b(document|window|console|function|let|const|var|=>|this)\b'
    return t

def t_JS_FUNCTION_DEF(t):
    r'\bfunction\s+[a-zA-Z_]\w*\s*\(.*?\)\s*{'
    return t

def t_JS_VAR_DECL(t):
    r'\bvar\s+[a-zA-Z_]\w*\s*(=\s*[^;]+)?;'
    return t

def t_JS_LET_CONST_DECL(t):
    r'\b(let|const)\s+[a-zA-Z_]\w*\s*(=\s*[^;]+)?;'
    return t

def t_JS_PRINT(t):
    r'console\.log\s*\(\s*.*?\s*\)\s*;'
    return t
