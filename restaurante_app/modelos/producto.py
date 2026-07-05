class Producto:

    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio: float):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio no puede ser negativo.")

    def __str__(self):
        return f"{self.nombre} - ${self.__precio:.2f}"