def t_CPP(t):
    r'\b(this->[a-zA-Z_]\w*|virtual|cin|using|namespace|std|<<|>>)\b[a-zA-Z_]?;?'
    return t

def t_CPP_INCLUDE(t):
    r'\#include\s*<.*?>'
    return t

def t_CPP_PRINT(t):
    r'\bcout\s*(<<\s*(?:[a-zA-Z_]\w*|"([^"]*)"))*\s*(<<endl)*;?'
    return t

def t_CPP_VAR_DECL(t):
    r'\b(?:int|float|char|double|bool|long|short)\s+[a-zA-Z_]\w*\s*(?:=\s*[^;]+)?\s*;'
    return t