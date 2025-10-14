#!/usr/bin/env python3
# ──────────────────────────────────────────
# ── Problema 1
# ── Analizador para la siguiente gramática
# ──  <S> → 'a' <S> 'b'
# ──  <S> → 'c'
# Lenguaje a detectar: L = {c, acb, aacbb, aaacbbb, ...}
# ──────────────────────────────────────────

# -- Acceso a las funciones del modulo de apoyo
from log import Input

# -- Objeto global: Entrada. Inicialmente está
# -- asociado a la cadena nula
input = Input()


# ────────────────────────────────────────────────────────
# -- Funcion para parseo del simbolo no terminal inicial
# -- de la gramatica
# -- <S> → 'a' <S> 'b'
# ────────────────────────────────────────────────────────
def S():

    if input.token == 'a':
        input.consume('a')
        S()
        input.consume('b')
    elif input.token == 'c':
        input.consume('c')
    else:
        raise RuntimeError("Esperado: 'a' o 'c'")


# ────────────────────────────────────────────────────────
# -- Comenzar el parseado
# -- Se procede a parsear el simbolo inicial S de la gramática
# -- No se gestionan aqui los errores
# -- En caso de error genera la EXCEPCION RUNTIMEERROR
# ────────────────────────────────────────────────────────
def parse_start():
    # -- Que comience la fiesta!

    # -- Leer token actual
    input.advance()

    # -- Analisis del simbolo inicial de la gramatica!
    S()

    # -- Parseado termina bien, con exito
    # -- PERO hay que asegurarse que tras S no quedan
    # -- simbolos. Si hay simbolos, tecnicamente
    # -- es un error de parseo, ya que S engloba TODO
    # -- No puede haber nada tras S, por definicion
    if input.token != '':
        error = "⭕ ERROR: Token esperado: <empty>\n"\
                "☑️  Completado, PERO hay caracteres basura\n"\
               f"🗑️  Basura: {input._buffer[input.index:]}"
        raise RuntimeError(error)


# ────────────────────────────────────────────────────────
# -- Funcion basica de parseo
# -- Se inicia el parseo
# -- Se imprimen mensajes de comienzo y fin
# -- Se gestionan los errores
# --
# -- ENTRADA:
# --   input_str: Cadena a parsear
# ────────────────────────────────────────────────────────
def parse(input_str: str):

    # -- Inicializar la entrada con un nueva cadena
    input.reset(input_str, debug=True)

    # -- Quedarse solo con los 10 primeros simbolos de la
    # -- cadena a parsea, para mostrarlos al comienzo
    # -- del analisis
    cad = input_str[0:10]

    # --- UI: Mensaje de inicio
    print(f"\n🟡 ANALISIS: {cad}")

    # -- Que comience el parseo!
    try:
        # -- Parseo
        parse_start()

        # -- Mensaje final de exito
        print("✅ Exito! 🎉🎉🎉")

    # -- Ha ocurrido algun error durante el parseo
    except RuntimeError as emsg:

        # -- Mensaje final de error
        print(emsg)
        print("💔 Fail!")

    print()


# ──────────────
# ── MAIN
# ──────────────
parse("c")
parse("acb")
parse("aacbb")
parse("")
parse("ca")
parse("ab")
parse("acbb")
parse("aacb")
parse("bca")

print()
