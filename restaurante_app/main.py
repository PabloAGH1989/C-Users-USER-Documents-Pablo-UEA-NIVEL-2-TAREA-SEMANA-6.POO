from servicios.restaurante import RestauranteServices
from modelos.platillo import Platillo
from modelos.bebida import Bebida


def registrar_platillo(restaurante):

    nombre = input("Ingrese el nombre del platillo: ")
    precio = float(input("Ingrese el precio del platillo: "))

    ingredientes = input(
        "Ingrese los ingredientes separados por comas: "
    ).split(",")

    ingredientes = [i.strip() for i in ingredientes]

    platillo = Platillo(nombre, precio, ingredientes)

    restaurante.agregar_platillo(platillo)


def registrar_bebida(restaurante):

    nombre = input("Ingrese el nombre de la bebida: ")
    precio = float(input("Ingrese el precio de la bebida: "))
    tamaño = input("Ingrese el tamaño de la bebida: ")

    bebida = Bebida(nombre, precio, tamaño)

    restaurante.agregar_bebida(bebida)


def main():

    restaurante = RestauranteServices()

    while True:

        print("\n========== SISTEMA DEL RESTAURANTE ==========")
        print("1. Registrar Platillo")
        print("2. Registrar Bebida")
        print("3. Mostrar Menú")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_platillo(restaurante)

        elif opcion == "2":
            registrar_bebida(restaurante)

        elif opcion == "3":
            restaurante.mostrar_productos()

        elif opcion == "4":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opción incorrecta.")


if __name__ == "__main__":
    main()