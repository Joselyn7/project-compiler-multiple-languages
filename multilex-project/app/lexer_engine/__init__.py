from .python_rules import *
from .cpp_rules import *
from .java_rules import *
from .js_rules import *
from .base_rules import *

import ply.lex as lex


tokens = (
    # Identificadores del lenguaje
    'PYTHON',
    'JAVA',
    'CPP',
    'JAVASCRIPT',

    # Tokens exclusivos por lenguaje
    'PYTHON_DEF',
    'PYTHON_CLASS',
    'PYTHON_PRINT',
    'PYTHON_ELIF',
    'PYTHON_FOR_LOOP',
    'PYTHON_WHILE_LOOP',

    'CPP_INCLUDE',
    'CPP_PRINT',
    'CPP_VAR_DECL',

    'ACCESS_SPECIFIERS',
    'JAVA_PRINT',
    'JAVA_VAR_DECL',

    'JS_FUNCTION_DEF',
    'JS_VAR_DECL',
    'JS_LET_CONST_DECL',
    'JS_PRINT',

    # Tokens compartidos (aparecen en varios lenguajes)
    'FUNCTION_DEF',
    'FUNCTION_DECL',
    'VAR_DECL',
    'CLASS',
    'ASSIGN',
    'RETURN',
    'FUNCTION_CALL',
    'CALCULATION_OR_IDENTIFIER',
    'BRANCH',
    'FOR_LOOP',
    'WHILE_LOOP',
)

lexer = lex.lex()