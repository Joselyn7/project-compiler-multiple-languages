import ply.yacc as yacc
from app.parser_engine.lexer.python_lexer import tokens, lexer

syntax_tree = []

def p_program(p):
    'program : statement_list'
    p[0] = ('program', p[1])
    syntax_tree.append(p[0])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : assignment
                 | return_stmt
                 | function_def'''
    p[0] = p[1]

def p_assignment(p):
    'assignment : IDENTIFIER ASSIGN expression'
    p[0] = ('assign', p[1], p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = ('identifier', p[1])

def p_return_stmt(p):
    'return_stmt : RETURN expression'
    p[0] = ('return', p[2])

"""
def p_function_def(p):
    'function_def : DEF IDENTIFIER LPAREN RPAREN COLON'
    p[0] = ('func_def', p[2])
"""
def p_function_def(p):
    'function_def : DEF IDENTIFIER LPAREN RPAREN COLON NEWLINE statement_list'
    p[0] = ('func_def', p[2], p[7])

    
def p_error(p):
    if p:
        raise SyntaxError(f"Error de sintaxis en '{p.value}' (línea {p.lineno})")
    else:
        raise SyntaxError("Error de sintaxis al final del archivo")

parser = yacc.yacc()
