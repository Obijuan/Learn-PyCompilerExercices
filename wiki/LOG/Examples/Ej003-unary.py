#!/usr/bin/env python3
# ──────────────────────────────────────────
# ── Analisis sintáctico de un lenguaje
# ── Gramatica:
# ──  S → o
# ──────────────────────────────────────────

# ───── Constantes para indicar el lenguaje de entrada
MSG0 = ""
MSG1 = "o"
MSG2 = "oo"

# ────────── Variables globales
# ── Buffer de entrada
input_buffer = MSG1

# -- Token actual
token = ''

# -- Indice para acceder al buffer
# -- Por defecto apunta al final del buffer
tokenindex = -1


# ─────────────────────────────────────────────────
# ── AVANZAR
# ── Leer el siguiente simbolo de la entrada
#  Se incrementa el indice al buffer y se deposita
# el simbolo leido en la variable global token
# ─────────────────────────────────────────────────
def advance():
    global tokenindex, token

    # -- Apuntar al siguiente carácter
    tokenindex = tokenindex + 1

    # -- Leerlo!
    try:
        token = input_buffer[tokenindex]
    except IndexError:
        # -- Hemos llegado al final
        # -- Deolver la cadena vacia
        token = ''


# ──────────────
# ── MAIN
# ──────────────

# -- Leer primer simbolo de la entrada
advance()
print(f"Token: {token}")

# -- Leer el segundo simbolo
advance()
print(f"Token: {token}")
