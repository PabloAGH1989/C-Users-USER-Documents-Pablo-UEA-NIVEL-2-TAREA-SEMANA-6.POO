from modelos.producto import Producto


class Bebida(Producto):

    def __init__(self, nombre: str, precio: float, tamaño: str):
        super().__init__(nombre, precio)
        self.tamaño = tamaño

    def cambiar_tamaño(self, nuevo_tamaño: str):
        self.tamaño = nuevo_tamaño

    def mostrar_tamaño(self):
        return self.tamaño