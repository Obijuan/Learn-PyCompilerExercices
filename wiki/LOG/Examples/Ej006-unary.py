#!/usr/bin/env python3
# ──────────────────────────────────────────
# ── Analisis sintáctico de un lenguaje
# ── Gramatica:
# ──  S → o
# ──────────────────────────────────────────

# -- Acceso a las funciones del modulo de apoyo
from log import Input

# ──────────────
# ── MAIN
# ──────────────

# -- Crear la entrada
input = Input("o")

# -- Leer los dos primeros simbolos
for _ in range(2):

    # -- Leer siguiente simbolo de la entrada
    input.advance()

    # -- Imprimirlo!
    print(f"Token: {input.str_token()}")

# -- Fin
print("Analisis completado!")
