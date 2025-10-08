#!/usr/bin/env python3
# ──────────────────────────────────────────
# ── Analisis sintáctico de un lenguaje
# ── Gramatica:
# ──  S → o
# ──────────────────────────────────────────

# -- Acceso a las funciones del modulo de apoyo
from log import Input


# ────────────────────────────────────────────────────────
# -- CONSUMIR un simbolo de la entrada
# -- Se espera que en la entrada haya un simbolo determinado
# -- Si lo hay se consume: es decir, se da por valido y se
# -- lee el siguiente
# -- Si NO lo hay, se imprime un mensaje de error
# --
# -- ENTRADA:
# --   input: Buffer de entrada a analizar(clase Input)
# --   expected: Simbolo a consumir
# ────────────────────────────────────────────────────────
def consume(input: Input, expected: str):
    if input.token == expected:
        input.advance()
    else:
        print(f'  ❌ERROR: Token esperado: {expected}')


# ────────────────────────────────────────────────────────
# -- Funcion para parseo basico
# -- ENTRADA:
# --   input: Buffer de entrada a analizar(clase Input)
# ────────────────────────────────────────────────────────
def parse(input: Input):
    print("\n🟢 ANALISIS:")

    # -- Leer token actual
    input.advance()

    # -- Comprobar que se recibe un simbolo especifico
    consume(input, "o")
    print()


# ──────────────
# ── MAIN
# ──────────────
# -- Crear las entradas a probar
input0 = Input("", debug=True)
input1 = Input("o", debug=True)
input2 = Input("oo", debug=True)
input3 = Input("ao", debug=True)

parse(input0)
parse(input1)
parse(input2)
parse(input3)

print()
