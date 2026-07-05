class RestauranteServices:

    def __init__(self):
        self.platillos = []
        self.bebidas = []

    def agregar_platillo(self, platillo):
        self.platillos.append(platillo)
        print("Platillo agregado correctamente.")

    def agregar_bebida(self, bebida):
        self.bebidas.append(bebida)
        print("Bebida agregada correctamente.")

    def mostrar_productos(self):

        print("\n========== MENÚ DEL RESTAURANTE ==========")

        print("\nPLATILLOS")

        if len(self.platillos) == 0:
            print("No existen platillos registrados.")
        else:
            for platillo in self.platillos:
                print("-----------------------------")
                print("Nombre:", platillo.nombre)
                print("Precio: $", platillo.get_precio())
                print("Ingredientes:", platillo.mostrar_ingredientes())

        print("\nBEBIDAS")

        if len(self.bebidas) == 0:
            print("No existen bebidas registradas.")
        else:
            for bebida in self.bebidas:
                print("-----------------------------")
                print("Nombre:", bebida.nombre)
                print("Precio: $", bebida.get_precio())
                print("Tamaño:", bebida.mostrar_tamaño())