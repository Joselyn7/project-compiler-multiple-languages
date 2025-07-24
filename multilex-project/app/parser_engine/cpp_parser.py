import ply.yacc as yacc
from app.parser_engine.lexer.cpp_lexer import tokens, lexer

syntax_tree = []

# Programa principal
def p_program(p):
    'program : statement_list'
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

# Tipos de sentencias permitidas
def p_statement(p):
    '''statement : var_decl
                 | assignment
                 | return_stmt
                 | cout_stmt'''

    p[0] = p[1]

# Declaración de variable: int x;
def p_var_decl(p):
    'var_decl : INT IDENTIFIER SEMICOLON'
    p[0] = ('var_decl', p[2])

# Asignación: x = 5;
def p_assignment(p):
    'assignment : IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = ('assign', p[1], p[3])

# Retorno: return x;
def p_return_stmt(p):
    'return_stmt : RETURN expression SEMICOLON'
    p[0] = ('return', p[2])

# Sentencia cout: cout << "texto";
def p_cout_stmt(p):
    'cout_stmt : COUT LSHIFT STRING SEMICOLON'
    p[0] = ('cout', p[3])  # p[3] contiene el string

# Expresiones con operadores binarios
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

# Número: 42
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

# Identificador: x
def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = ('identifier', p[1])

# Manejo de errores
def p_error(p):
    if p:
        raise SyntaxError(f"Error de sintaxis en '{p.value}' (línea {p.lineno})")
    else:
        raise SyntaxError("Error de sintaxis al final del archivo")

# Construcción del parser
parser = yacc.yacc()
