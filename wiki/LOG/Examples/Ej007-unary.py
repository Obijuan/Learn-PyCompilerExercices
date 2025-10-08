#!/usr/bin/env python3
# ──────────────────────────────────────────
# ── Analisis sintáctico de un lenguaje
# ── Gramatica:
# ──  S → o
# ──────────────────────────────────────────

# -- Acceso a las funciones del modulo de apoyo
from log import Input


# ────────────────────────────────────────────────────────
# -- Funcion para lectura de los dos primeros caracteres
# -- de la entrada
# -- ENTRADA:
# --   input: Buffer de entrada a analizar(clase Input)
# ────────────────────────────────────────────────────────
def read2(input: Input):

    print("🟢 ANALISIS:")

    # -- Leer los dos primeros simbolos
    for _ in range(2):

        # -- Leer siguiente simbolo de la entrada
        input.advance()

        # -- Imprimirlo!
        print(f"Token: {input.str_token()}")

    # -- Fin
    print()


# ──────────────
# ── MAIN
# ──────────────
# -- Crear las entradas a probar
input0 = Input("")
input1 = Input("o")
input2 = Input("oo")

print()
read2(input0)
read2(input1)
read2(input2)
