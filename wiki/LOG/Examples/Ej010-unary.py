#!/usr/bin/env python3
# ──────────────────────────────────────────
# ── Analisis sintáctico de un lenguaje
# ── Gramatica:
# ──  S → o
# ──────────────────────────────────────────

# -- Acceso a las funciones del modulo de apoyo
from log import Input

# -- Objeto global: Entrada. Inicialmente está
# -- asociado a la cadena nula
input = Input()


# ────────────────────────────────────────────────────────
# -- Funcion para parseo del simbolo auxiliar inicial
# -- de la gramatica
# --
# -- ENTRADA:
# --   input: Buffer de entrada a analizar(clase Input)
# ────────────────────────────────────────────────────────
def S():

    # -- Comprobar que se recibe un simbolo especifico
    input.consume("o")


# ────────────────────────────────────────────────────────
# -- Funcion basica de parse
# -- Se inicia el parse del simbolo auxiliar inicial de
# -- la gramatica y se gestionan los errores
# --
# -- ENTRADA:
# --   input: Buffer de entrada a analizar(clase Input)
# ────────────────────────────────────────────────────────
def parse(input_str: str):

    # -- Inicializar la entrada con un nuevo valor
    input.reset(input_str, debug=True)

    print("\n🟢 ANALISIS:")

    # -- Leer token actual
    input.advance()

    # -- Analisis del simbolo inicial de la gramatica!
    try:
        S()

    except RuntimeError as emsg:
        # -- Ha ocurrido algun error
        print(emsg)

    print()


# ──────────────
# ── MAIN
# ──────────────
parse("")
parse("o")
parse("oo")
parse("ao")

print()
