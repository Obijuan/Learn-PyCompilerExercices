#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────────
# ── Capitulo 3. Ejercicio 10
# ── Determinar si la cadena introducida pertenece al lenguaje
# ── definido sobre {a,b} que contiene los palíndromos
# ───────────────────────────────────────────────────────────────────

ALFABETO = ['a', 'b']

# -- Pedir cadena al usuario
cad = str(input("Cadena: "))

# -- Longitud de la cadena
n = len(cad)

# -- Recorrer la cadena
for i in range(n):
    if cad[i] != cad[n-i-1]:
        print("No pertenece al lenguaje")
        break

    if cad[i] not in ALFABETO:
        print("No pertenece al lenguaje")
        break
else:
    print("Pertenece al lenguaje. ¡Es palindromo!")
