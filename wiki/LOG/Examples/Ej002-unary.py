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

# ──────────────
# ── MAIN
# ──────────────

# -- Apuntar al primer caracter
tokenindex = tokenindex + 1

# -- Leer el primer caracter
token = input_buffer[tokenindex]

# -- Imprimir el primer token
print(f"Token: {token}")

# -- Apuntar al siguiente carácter
tokenindex = tokenindex + 1

# -- Leerlo!
token = input_buffer[tokenindex]

# -- Imprimirlo!
print(f"Token: {token}")
