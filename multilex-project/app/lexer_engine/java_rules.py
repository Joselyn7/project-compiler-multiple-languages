def t_JAVA(t):
    r'\b(finally|super|this\.[a-zA-Z_]\w*|@Override|static|abstract|package)\b;?'
    return t

def t_ACCESS_SPECIFIERS(t):
    r'\b(public|private|protected)\b'
    return t

def t_JAVA_PRINT(t):
    r'System\.out\.println\s*\(\s*.*?\s*\)\s*;'
    return t

def t_JAVA_VAR_DECL(t):
    r'\b(?:int|float|char|double|boolean|long|short|String)\s+[a-zA-Z_]\w*\s*(?:=\s*[^;]+)?\s*;'
    return t
