# 🧠 Compilador Multilenguaje 

## 📘 Descripción del proyecto

Este trabajo propone un **compilador multilenguaje** que alcanza hasta la fase sintáctica, basado en una arquitectura modular que separa analizadores léxicos y sintácticos por lenguaje, facilitando su escalabilidad y mantenimiento.

Como aporte, se incorpora un **mecanismo de inferencia automática del lenguaje de entrada** basado en una estrategia de puntuación: cada token reconocido aporta un peso predefinido, lo que permite seleccionar dinámicamente el analizador sintáctico correspondiente.

La herramienta ha sido desarrollada en **Python**, utilizando la biblioteca **PLY (Python Lex-Yacc)**, e implementada sobre **Flask** para ofrecer una interfaz web interactiva. Actualmente, admite código fuente en **C++, Java, Python y JavaScript**.

---

## 🛠️ Instalación y ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/Joselyn7/project-compiler-multiple-languages.git
cd multilex-project

2. Instala las dependencias:

pip install -r requirements.txt
 
3. Ejecuta la aplicación:

python run.py

