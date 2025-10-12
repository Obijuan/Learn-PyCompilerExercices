#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────────
# ── Capitulo 3. Ejercicio 9
# ── Determinar si la cadena introducida pertenece al lenguaje
# ── definido sobre {a,b} que solo tiene 2 b's
# ───────────────────────────────────────────────────────────────────

ALFABETO = ['a', 'b']

# -- Pedir cadena al usuario
cad = str(input("Cadena: "))

# -- Contador de caracteres b
incb = 0

# -- Recorrer la cadena
for car in cad:
    # -- Comprobar si es un caracter del alfabeto
    if car not in ALFABETO:
        print("No pertenece al lenguaje")
        break

    # -- Si el caracter es b, incrementar el contador
    if car == 'b':
        incb = incb + 1
else:
    if incb == 2:
        print("Pertenece al lenguaje")
    else:
        print("NO pertenece al lenguaje")
