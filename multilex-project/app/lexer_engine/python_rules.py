def t_PYTHON_DEF(t):
    r'\bdef\b\s+[a-zA-Z_]\w*\s*\(\s*\)\s*:\s*'
    return t

def t_PYTHON_CLASS(t):
    r'class\s+[a-zA-Z_]\w*\s*:'
    return t

def t_PYTHON(t):
    r'\b(self|pass|except|try)\b'
    return t

def t_PYTHON_PRINT(t):
    r'\bprint\s*\(\s*.*?\s*\)'
    return t

def t_PYTHON_ELIF(t):
    r'\belif\b'
    return t

def t_PYTHON_FOR_LOOP(t):
    r'\bfor\b\s+[a-zA-Z_]\w*\s+in\s+.*?:'
    return t

def t_PYTHON_WHILE_LOOP(t):
    r'\bwhile\b\s+.*?:'
    return t

