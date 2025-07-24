import ply.yacc as yacc
from app.parser_engine.lexer.java_lexer import tokens, lexer

syntax_tree = []

# Programa: función principal
def p_program(p):
    'program : PUBLIC STATIC VOID IDENTIFIER LPAREN RPAREN block'
    p[0] = ('main_function', p[4], p[7])
    syntax_tree.append(p[0])

# Bloque de instrucciones entre llaves (omitimos llaves por simplicidad xd)
def p_block(p):
    '''block : statement_list'''
    p[0] = p[1]

# Lista de sentencias
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

# Sentencias posibles
def p_statement(p):
    '''statement : var_decl
                 | assignment
                 | return_stmt'''
    p[0] = p[1]

# Declaración: int x;
def p_var_decl(p):
    'var_decl : INT IDENTIFIER SEMICOLON'
    p[0] = ('var_decl', p[2])

# Asignación: x = 10;
def p_assignment(p):
    'assignment : IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = ('assign', p[1], p[3])

# Retorno: return x;
def p_return_stmt(p):
    'return_stmt : RETURN expression SEMICOLON'
    p[0] = ('return', p[2])

# Expresiones aritméticas
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

# Número
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

# Identificador
def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = ('identifier', p[1])

# Errores
def p_error(p):
    if p:
        raise SyntaxError(f"Error de sintaxis en '{p.value}' (línea {p.lineno})")
    else:
        raise SyntaxError("Error de sintaxis al final del archivo")

# Construcción
parser = yacc.yacc()

