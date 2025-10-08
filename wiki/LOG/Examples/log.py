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
    def __init__(self, buffer=''):

        # -- Propiedad: Buffer de entrada
        self._buffer = buffer

        # -- Propiedad: Indice al buffer de entrada
        self.index = -1

        # -- Propiedad: Simbolo actual
        self.token = ''

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
            # -- Deolver la cadena vacia
            self.token = ''
