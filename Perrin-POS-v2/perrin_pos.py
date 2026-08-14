# ============================================================
#          PERRIN POS v2 — ELIMINAR PRODUCTOS
# ============================================================

# OBJETIVO:
# Crear una función que permita eliminar productos existentes
# de la lista.


# ------------------------------------------------------------
# PASO 1 — CREAR LA FUNCIÓN
# ------------------------------------------------------------

# Crear una función llamada eliminar_producto.
#
# Debe recibir como parámetro la lista de productos.
#
# Pista:
#
# def eliminar_producto(...):


# ------------------------------------------------------------
# PASO 2 — PEDIR EL PRODUCTO
# ------------------------------------------------------------

# Preguntar al usuario qué producto desea eliminar.
#
# Guardar la respuesta en una variable.
#
# Utilizar .strip() para eliminar espacios innecesarios.


# ------------------------------------------------------------
# PASO 3 — COMPROBAR SI EXISTE
# ------------------------------------------------------------

# Comprobar si el producto escrito está dentro
# de la lista de productos.
#
# Aquí necesitarás:
#
# if _____ in productos:


# ------------------------------------------------------------
# PASO 4 — ELIMINAR
# ------------------------------------------------------------

# SI el producto existe:
#
# → eliminarlo utilizando .remove()
# → mostrar:
#
# "Producto eliminado correctamente"
#
#
# SI NO existe:
#
# → NO intentar eliminarlo.
# → mostrar:
#
# "Producto no encontrado"


# ------------------------------------------------------------
# PASO 5 — CONECTAR CON EL MENÚ
# ------------------------------------------------------------

# Actualmente tenemos:
#
# elif menu == 3:
#     print("Eliminar producto")
#
# Reemplazar ese print por una llamada a:
#
# eliminar_producto(...)
#
# Piensa qué argumento necesita recibir.


# ------------------------------------------------------------
# PRUEBA 1
# ------------------------------------------------------------

# Agregar:
#
# Leche
# Pan
# Huevos
#
# Ver productos.
#
# Resultado:
#
# Leche
# Pan
# Huevos


# ------------------------------------------------------------
# PRUEBA 2
# ------------------------------------------------------------

# Elegir eliminar producto.
#
# Escribir:
#
# Pan
#
# Resultado esperado:
#
# "Producto eliminado correctamente"
#
# Después, al ver productos:
#
# Leche
# Huevos


# ------------------------------------------------------------
# PRUEBA 3 — PRODUCTO INEXISTENTE
# ------------------------------------------------------------

# Intentar eliminar:
#
# Chocolate
#
# Resultado esperado:
#
# "Producto no encontrado"
#
# IMPORTANTE:
# El programa NO debe cerrarse ni producir error.


# ============================================================
#                    RETO EXTRA 🌶️
# ============================================================

# ¿Qué pasa si el usuario entra a "Eliminar producto"
# cuando la lista está completamente vacía?
#
# Intenta conseguir que antes de preguntar qué producto
# quiere eliminar, el programa detecte que:
#
# productos = []
#
# y muestre:
#
# "No hay productos para eliminar"
#
# En ese caso NO debería preguntar el nombre del producto.
#
# PISTA:
#
# Ya sabes comprobar si una lista tiene datos:
#
# if productos:
#
# Piensa cómo podrías combinarlo con else.


# ============================================================
# NO UTILIZAR TODAVÍA
# ============================================================

# ❌ try / except
# ❌ diccionarios
# ❌ bases de datos
# ❌ Copilot haciendo el ejercicio por nosotros 😂
#
# TODO se puede resolver utilizando:
#
# - funciones
# - parámetros
# - listas
# - if / else
# - in
# - remove()
# - input()
# - strip()
#
# ============================================================

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

def agregar_producto(productos):
    nuevo_producto = {
        "Nombre": input("Qué producto desea agregar al sistema?: ").strip(),
        "Precio": float(input("Ingrese el precio del producto: ").strip()),
        "Stock": int(input("Ingrese el stock del producto: ").strip())
    }

    

    if nuevo_producto:
        productos.append(nuevo_producto)
        print("Poducto agregado exitosamente!")
    else:
        print("Vuelva a escribir el producto...")
    

def eliminar_producto(productos):
    if productos:
        borrar = input("Qué producto desea borrar? ").strip()

        if borrar in productos:
            productos.remove(borrar)
            print("Producto borrado exitosamente")
        else:
            print("Ese producto no existe, inténtelo nuevamente.")
    else:
        print("No hay productos para eliminar")

def realizar_venta():
    if productos:
        producto_comprado = input("Ingrese el producto que desea comprar")

        if producto_comprado in productos:
            precio = float(input(""))

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
        print("Realizar venta")
    elif menu == 5:
        print("Ver total vendido")
    elif menu == 6:
        print("Cerrando Perrin POS v2...")
    else:
        print("Opción inválida")

        