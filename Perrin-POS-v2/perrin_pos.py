# ============================================================
#              PERRIN POS v2 — PARTE 2
#                 AGREGAR PRODUCTOS
# ============================================================

# OBJETIVO:
# Crear una función que permita agregar productos a la lista
# principal del sistema.


# ------------------------------------------------------------
# PASO 1 — CREAR LA FUNCIÓN
# ------------------------------------------------------------

# Crear una función llamada agregar_producto.
#
# La función debe recibir como parámetro la lista de productos.
#
# Pista de estructura:
#
# def agregar_producto(...):


# ------------------------------------------------------------
# PASO 2 — PEDIR EL PRODUCTO
# ------------------------------------------------------------

# Dentro de la función:
#
# Preguntar al usuario qué producto desea agregar.
#
# Guardar lo que escriba en una variable.


# ------------------------------------------------------------
# PASO 3 — VALIDAR EL PRODUCTO
# ------------------------------------------------------------

# Comprobar si el usuario realmente escribió algo.
#
# SI escribió un producto:
#     → agregarlo a la lista.
#     → mostrar "Producto agregado correctamente".
#
# SI NO escribió nada:
#     → NO agregar nada.
#     → mostrar "El producto no puede estar vacío".
#
# PISTAS:
#
# if variable:
#
# lista.append(...)


# ------------------------------------------------------------
# PASO 4 — CONECTARLO AL MENÚ
# ------------------------------------------------------------

# Buscar esta parte del programa:
#
# elif menu == 2:
#
# Quitar el print provisional de "Agregar producto".
#
# En su lugar, llamar a agregar_producto()
# y enviarle la lista de productos como argumento.


# ------------------------------------------------------------
# PASO 5 — PROBAR EL SISTEMA
# ------------------------------------------------------------

# PRUEBA 1:
#
# Elegir opción 1.
#
# Resultado esperado:
# "No hay productos"


# PRUEBA 2:
#
# Elegir opción 2.
# Escribir: Leche
#
# Resultado esperado:
# "Producto agregado correctamente"


# PRUEBA 3:
#
# Elegir opción 1.
#
# Resultado esperado:
# Leche


# PRUEBA 4:
#
# Agregar:
# Pan
# Huevos
#
# Luego elegir "Ver productos".
#
# Resultado esperado:
#
# Leche
# Pan
# Huevos


# PRUEBA 5 — VALIDACIÓN:
#
# Elegir opción 2.
# NO escribir ningún producto y presionar Enter.
#
# Resultado esperado:
# "El producto no puede estar vacío"
#
# IMPORTANTE:
# El dato vacío NO debe aparecer después en la lista.


# ============================================================
#                NO HACER TODAVÍA
# ============================================================

# ❌ No agregar precios.
# ❌ No agregar cantidades.
# ❌ No realizar ventas.
# ❌ No utilizar diccionarios.
# ❌ No buscar la solución en Copilot 😂
#
# Utilizar únicamente cosas que ya conocemos:
#
# - Funciones
# - Parámetros
# - input()
# - if / else
# - listas
# - append()
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
    agregar = input("Qué producto desea agregar? ")

    if agregar:
        productos.append(agregar)
        print("Producto agregado correctamente")
    else:
        print("El producto no puede estar vacío")


while menu != 6:
    mostrar_menu()

    menu = int(input("Qué opción desea realizar?: "))

    if menu == 1:
        ver_productos(productos)
    elif menu == 2:
        agregar_producto(productos)
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

    