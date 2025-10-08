#!/usr/bin/env python3
# ──────────────────────────────────────────
# ── Analisis sintáctico de un lenguaje
# ── Gramatica:
# ──  S → λ
# ──  S → oA
# ──  A → o
# ──  A → λ
# Lenguaje a detectar: L = {λ, o, oo}
# ──────────────────────────────────────────

# -- Acceso a las funciones del modulo de apoyo
from log import Input

# -- Objeto global: Entrada. Inicialmente está
# -- asociado a la cadena nula
input = Input()


# ────────────────────────────────────────────────────────
# -- Funcion para parseo del simbolo no terminal inicial
# -- de la gramatica
# ────────────────────────────────────────────────────────
def S():

    # -- Comprobar los casos, segun el token actual
    # -- CASO 1: Cadena nula
    if input.token == '':
        pass

    # -- CASO 2: marca unaria
    elif input.token == 'o':

        # -- Consumir caracter terminal
        input.consume('o')

        # -- Procesar simbolo no terminal
        A()

    # -- Resto de casos: Error
    else:
        raise RuntimeError("⭕ ERROR: Token esperados: o | <empty>")


# ──────────────────────────────
# -- Parseo de las cadenas A
# ──────────────────────────────
def A():

    # -- Tenemos dos opciones, que se determinan
    # -- segun el valor del token actual
    # -- CASO 1
    if input.token == 'o':
        # -- consumir este token
        input.consume('o')

    # -- CASO 2: cadena nula
    elif input.token == '':
        pass  # -- No se hace nada

    # -- Resto de casos: Error
    else:
        raise RuntimeError("⭕ ERROR: Token esperados: o | <empty>")


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
parse("")
parse("o")
parse("oo")
parse("ooo")
parse("ao")

print()
