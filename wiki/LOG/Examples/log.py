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
