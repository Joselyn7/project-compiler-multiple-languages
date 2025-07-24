from flask import Blueprint, render_template, request, send_file, flash
import io
import pandas as pd
import base64
from app.lexer_engine import lexer 
#parsers
from app.parser_engine.python_parser import parser as py_parser, syntax_tree as py_tree
from app.parser_engine.cpp_parser import parser as cpp_parser, syntax_tree as cpp_tree
from app.parser_engine.java_parser import parser as java_parser, syntax_tree as java_tree
from app.parser_engine.js_parser import parser as js_parser, syntax_tree as js_tree

from app.parser_engine.lexer.python_lexer import lexer as py_lexer
from app.parser_engine.lexer.cpp_lexer import lexer as cpp_lexer
from app.parser_engine.lexer.java_lexer import lexer as java_lexer
from app.parser_engine.lexer.js_lexer import lexer as js_lexer

from app.parser_engine.tree_drawer import draw_tree


main_bp = Blueprint('main', __name__)

def test_lexer(data):
    lexer.input(data)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens

def generate_csv_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'data:file/csv;base64,{b64}'
    return href

@main_bp.route("/", methods=["GET", "POST"])
def index():
    tokens_df = None
    detected_msg = None
    download_link = None
    code_input = '''let a = 4
    '''
    max_lang = None
    syntax_error = None
    tree_generated = False

    if request.method == "POST":
        code_input = request.form.get("code_input", "")
        tokens = test_lexer(code_input)
        token_data = [(tok.type, tok.value.strip()) for tok in tokens]
        tokens_df = pd.DataFrame(token_data, columns=["Tipo", "Valor"])

        # diccionario de pesos por lenguaje
        weights = {
            'PYTHON': {
                'PYTHON_DEF': 2,
                'PYTHON_CLASS': 2,
                'PYTHON_PRINT': 1,
                'PYTHON_ELIF': 1.5,
                'PYTHON_FOR_LOOP': 1.5,
                'PYTHON_WHILE_LOOP': 1.5,
            },
            'CPP': {
                'CPP': 1,
                'CPP_INCLUDE': 2,
                'CPP_PRINT': 1.5,
                'CLASS': 1.5,
            },
            'JAVA': {
                'JAVA': 1,
                'JAVA_PRINT': 1.5,
                'CLASS': 1.5,
                'FUNCTION_DECL': 1.5,
                'ACCESS_SPECIFIERS': 1,
            },
            'JAVASCRIPT': {
                'JAVASCRIPT': 1,
                'JS_FUNCTION_DEF': 2,
                'JS_VAR_DECL': 1.5,
                'JS_LET_CONST_DECL': 1.5,
                'JS_PRINT': 1,
            }
        }

        scores = {'PYTHON': 0, 'CPP': 0, 'JAVA': 0, 'JAVASCRIPT': 0}

        for tok in tokens:
            for lang, token_weights in weights.items():
                if tok.type in token_weights:
                    scores[lang] += token_weights[tok.type]

        # Determina el lenguaje con mayor puntuación
        max_lang = max(scores, key=scores.get)
        max_score = scores[max_lang]

        # Aplica umbral mínimo opcional para mayor confiabilidad
        if max_score == 0:
            detected_msg = "No se pudo detectar el lenguaje"
        else:
            detected_msg = f"Lenguaje detectado: {max_lang} (score: {max_score})"

        download_link = generate_csv_link(tokens_df)

        # === ANÁLISIS SINTÁCTICO ===
        # === Generar imagen del árbol de sintaxis ===
        from app.parser_engine.tree_drawer import draw_tree
        try:
            if max_lang == 'PYTHON':
                py_tree.clear()
                py_parser.parse(code_input, lexer=py_lexer)
                tree_generated = True
                if py_tree:
                    draw_tree(py_tree[0], filename="app/static/py_tree")

            elif max_lang == 'CPP':
                cpp_tree.clear()
                cpp_parser.parse(code_input, lexer=cpp_lexer)
                tree_generated = True
                if cpp_tree:
                    draw_tree(cpp_tree[0], filename="app/static/cpp_tree")

            elif max_lang == 'JAVA':
                java_tree.clear()
                java_parser.parse(code_input, lexer=java_lexer)
                tree_generated = True
                if java_tree:
                    draw_tree(java_tree[0], filename="app/static/java_tree")

            elif max_lang == 'JAVASCRIPT': #probando
                print("CÓDIGO RECIBIDO:")
                print(repr(code_input))
                print("=== TOKENS DETECTADOS PARA JAVASCRIPT ===")
                js_lexer.input(code_input)
                while True:
                    tok = js_lexer.token()
                    if not tok:
                        break
                    print(f"{tok.type}: {tok.value}")

                js_tree.clear()
                js_parser.parse(code_input, lexer=js_lexer)
                tree_generated = True

                if js_tree:
                    draw_tree(js_tree[0], filename="app/static/js_tree")

            else:
                syntax_error = f"No se encontró un parser para el lenguaje detectado: {max_lang}"
        except SyntaxError as e:
            syntax_error = str(e)
            tree_generated = False

    return render_template("index.html",
                           code_input=code_input,
                           tables=[tokens_df.to_html(classes='table table-striped', index=False)] if tokens_df is not None else None,
                           detected_msg=detected_msg,
                           download_link=download_link,
                           syntax_error=syntax_error,
                           tree_generated=tree_generated,
                           max_lang=max_lang)