#!/usr/bin/env python3
# ──────────────────────────────────────────
# ── MODULO AUXILIAR LOG
# ── Aquí se meten todas las clases y funciones
# ── de apoyo para los ejemplos
# ──────────────────────────────────────────

# ─────────────────────────────────────────────────
# ── CLASE INPUT
# La usamos para gestionar todo lo relacionado con
# la entrada de los simbolos
# ─────────────────────────────────────────────────
class Input:

    # -------------------------------------------------
    # -- Crear un buffer de entrada, inicializado con
    # -- la cadena indicada
    # -------------------------------------------------
    def __init__(self, buffer='', debug=False):

        # -- Inicializar las propiedades
        self.reset(buffer, debug)

    # ------------------------------------------------------------
    # -- Inicializar las propiedades a sus valores iniciales
    # -- o los datos por el usuario
    # ------------------------------------------------------------
    def reset(self, buffer='', debug=False):
        # -- Inicializar todas las propiedades a sus valores iniciales
        # -- o dados por el usuario

        # -- Propiedad: Buffer de entrada
        self._buffer = buffer

        # -- Propiedad: Indice al buffer de entrada
        self.index = -1

        # -- Propiedad: Simbolo actual
        self.token = ''

        # -- Propiedad debug
        self._debug = debug

    # ─────────────────────────────────────────────────
    # ── AVANZAR
    # ── Leer el siguiente simbolo de la entrada
    #  Se incrementa el indice al buffer y se
    # lee el simbolo actual
    # ─────────────────────────────────────────────────
    def advance(self):

        # -- Apuntar al siguiente caracter
        self.index += 1

        # -- Leer simbolo actual
        try:
            self.token = self._buffer[self.index]

        except IndexError:
            # -- Hemos llegado al final
            # -- Devolver la cadena vacia
            self.token = ''

        # -- En modo debug se imprime el token actual
        if self._debug:
            print(f"Token: {self.str_token()}")

    # ─────────────────────────────────────────────────
    # ── DEVOLVER la cadena asociada al token actual
    # Si el token actual es la cadena nula, se imprime
    # el mensaje <empty>
    # De lo contrario se devuleve el propio simbolo
    # ─────────────────────────────────────────────────
    def str_token(self):
        token = "<empty>" if self.token == '' else self.token
        return token

    # ────────────────────────────────────────────────────────
    # -- CONSUMIR un simbolo de la entrada
    # -- Se espera que en la entrada haya un simbolo determinado
    # -- Si lo hay se consume: es decir, se da por valido y se
    # -- lee el siguiente
    # -- Si NO lo hay, se genera una EXCEPCION de error
    # --
    # -- ENTRADA:
    # --   expected: Simbolo a consumir
    # ────────────────────────────────────────────────────────
    def consume(self, expected: str):
        if self.token == expected:
            self.advance()
        else:
            raise RuntimeError(f'⭕ERROR: Token esperado: {expected}')

    # ────────────────────────────────────────────────────────
    # -- Consumir una cadena de caracteres
    # -- Se llama a CONSUMIR tantas veces como caracteres hay
    # -- en la cadena
    # ────────────────────────────────────────────────────────
    def consume_str(self, expected_str: str):

        # -- Recorrer la cadena completa
        # -- consumiendo los caracteres uno a uno
        for expected in expected_str:
            self.consume(expected)
