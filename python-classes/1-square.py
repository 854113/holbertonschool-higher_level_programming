#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size):
        """Inicializa un nuevo cuadrado.

        Args:
            size: tamaño del cuadrado (privado).
        """
        self.__size = size
