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

# -- Leer primer simbolo de la entrada
input.advance()
print(f"Token: {input.token}")

# -- Leer el segundo simbolo
input.advance()
print(f"Token: {input.token}")
