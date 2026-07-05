from modelos.producto import Producto


class Platillo(Producto):

    def __init__(self, nombre: str, precio: float, ingredientes: list):
        super().__init__(nombre, precio)
        self.ingredientes = ingredientes

    def agregar_ingrediente(self, ingrediente: str):
        self.ingredientes.append(ingrediente)

    def eliminar_ingrediente(self, ingrediente: str):
        if ingrediente in self.ingredientes:
            self.ingredientes.remove(ingrediente)
        else:
            raise ValueError("El ingrediente no existe.")

    def mostrar_ingredientes(self):
        return ", ".join(self.ingredientes)