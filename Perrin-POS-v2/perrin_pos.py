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
            print("Nombre:", producto["Nombre"], "| Precio: ₡", producto["Precio"], "| Stock:", producto["Stock"])
    else:
        print("No hay productos")

def agregar_producto(productos):
    nuevo_producto = {
        "Nombre": input("Qué producto desea agregar al sistema?: ").strip(),
        "Precio": float(input("Ingrese el precio del producto: ").strip()),
        "Stock": int(input("Ingrese el stock del producto: ").strip())
    }

    

    if nuevo_producto["Nombre"]:
        productos.append(nuevo_producto)
        print("Poducto agregado exitosamente!")
    else:
        print("Vuelva a escribir el producto...")
    
def eliminar_producto(productos):
    if productos:
        borrar = input("Qué producto desea borrar? ").strip()

        for producto in productos:
            if borrar == producto["Nombre"]:
                productos.remove(producto)
                print("Producto eliminado exitosamene!")

    else:
        print("No hay productos para eliminar")

def realizar_venta(productos):
    if productos:
        compra = input("Qué producto desea comprar? ")

        for producto in productos:
            if producto["Nombre"] == compra:
                print(producto)

                cantidad = int(input("Cuantas unidades desea comprar: "))

                if cantidad <= producto["Stock"]:
                    producto["Stock"] -= cantidad

                    total_venta = producto["Precio"] * cantidad

                    print("Debe de pagar: ₡", total_venta)

                    return total_venta

    else:
        print("No hay productos en el inventario")

while menu != 6:
    mostrar_menu()

    menu = int(input("Qué opción desea realizar?: "))

    if menu == 1:
        ver_productos(productos)
    elif menu == 2:
        agregar_producto(productos)
    elif menu == 3:
        eliminar_producto(productos)
    elif menu == 4:
        realizar_venta(productos)
    elif menu == 5:
        total_vendido = realizar_venta(productos)
        print(total_vendido)
    elif menu == 6:
        print("Cerrando Perrin POS v2...")
    else:
        print("Opción inválida")

