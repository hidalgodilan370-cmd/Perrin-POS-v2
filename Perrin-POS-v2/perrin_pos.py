productos = []
total_vendido = 0
menu = 0

def mostrar_menu():
    print("===== PERRIN POS v2 =====")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Realizar venta")
    print("5. Ver total vendido")
    print("6. Salir")

def ver_productos(productos):
    if productos:
        for producto in productos:
            print(producto)
    else:
        print("No hay productos")
        


while menu != 6:
    mostrar_menu()

    menu = int(input("Qué opción desea realizar?: "))

    if menu == 1:
        productos = ["Pan", "Lisa", "Huevos"]
        ver_productos(productos)
    elif menu == 2:
        print("Agregar producto")
    elif menu == 3:
        print("Eliminar producto")
    elif menu == 4:
        print("Realizar venta")
    elif menu == 5:
        print("Ver total vendido")
    elif menu == 6:
        print("Cerrando Perrin POS v2...")
    else:
        print("Opción inválida")