import ply.yacc as yacc
from app.parser_engine.lexer.js_lexer import tokens, lexer

syntax_tree = []

# Programa puede ser una lista de sentencias (sin necesidad de function)
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])
    syntax_tree.append(p[0])

# Lista de sentencias
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

# Sentencias
def p_statement(p):
    '''statement : var_decl
                 | assignment
                 | return_stmt'''
    p[0] = p[1]

# Declaraciones de variable
def p_var_decl(p):
    '''var_decl : VAR var_list optional_semicolon
                | LET var_list optional_semicolon
                | CONST var_list optional_semicolon'''
    p[0] = ('var_decl_multi', p[1], p[2])

def p_var_list_multiple(p):
    'var_list : var_list COMMA var_item'
    p[0] = p[1] + [p[3]]

def p_var_list_single(p):
    'var_list : var_item'
    p[0] = [p[1]]

def p_var_item_assign(p):
    'var_item : IDENTIFIER ASSIGN expression'
    p[0] = ('var_init', p[1], p[3])

def p_var_item_noassign(p):
    'var_item : IDENTIFIER'
    p[0] = ('var', p[1])


# Asignación
def p_assignment(p):
    'assignment : IDENTIFIER ASSIGN expression optional_semicolon'
    p[0] = ('assign', p[1], p[3])

# Retorno
def p_return_stmt(p):
    'return_stmt : RETURN expression optional_semicolon'
    p[0] = ('return', p[2])

# Expresiones
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = ('identifier', p[1])


def p_optional_semicolon(p):
    '''optional_semicolon : SEMICOLON
                          | empty'''
    pass

def p_empty(p):
    'empty :'
    pass


# Error
def p_error(p):
    if p:
        raise SyntaxError(f"Error de sintaxis en '{p.value}' (línea {p.lineno})")
    else:
        raise SyntaxError("Error de sintaxis al final del archivo")

# Parser
parser = yacc.yacc(start='program')


