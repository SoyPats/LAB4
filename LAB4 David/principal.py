
from os import system
import archivos as arch

listProductos = []

def agregarProducto():
    system("cls")
    codigo = int(input("Ingrese el codigo del producto a agregar: "))
    nombre = input("Ingrese el nombre del producto a agregar: ")
    marca = input("Ingrese la marca del producto a agregar: ")
    precio = float(input("Ingrese el precio del producto a agregar: "))
    existencias = int(input("Ingrese las existencias del producto: "))

    proveedor = dict()
    codigoProveedor = int(input("Ingrese el código del proveedor: "))
    nombreProveedor = input("Ingrese el nombre del proveedor: ")
    paisProveedor = input("Ingrese el país del proveedor: ")
    proveedor["codigoProveedor"] = codigoProveedor
    proveedor["nombreProveedor"] = nombreProveedor
    proveedor["paisProveedor"] = paisProveedor

    producto = dict()
    producto["codigo"] = codigo
    producto["nombre"] = nombre
    producto["marca"] = marca
    producto["precio"] = precio
    producto["existencias"] = existencias
    producto["proveedor"] = proveedor

    listProductos.append(producto)

    system("cls")
    print("Producto agregado correctamente")
    system("pause")

def eliminarProducto():
    system("cls")
    idProducto = int(input("Ingrese el código del producto a eliminar: "))
    for i in listProductos:
        if i["codigo"] == idProducto:
            listProductos.remove(i)
            print("Producto eliminado correctamente")
            break
    else:
        print("Producto no encontrado")
    system("pause")

def actualizarPrecioProducto():
    system("cls")
    idProducto = int(input("Ingrese el código del producto a actualizar: "))
    for i in listProductos:
        if i["codigo"] == idProducto:
            i["precio"] = float(input("Ingrese el nuevo precio del producto: "))
            print("Precio actualizado correctamente")
            break
    else:
        print("Producto no encontrado")
    system("pause")

def listarProductos():
    system("cls")
    if len(listProductos) > 0:
        for producto in listProductos:
            print(f"{producto['codigo']}. {producto['nombre']}")
            print(f"Marca: {producto['marca']}")
            print(f"Precio: {producto['precio']}")
            print(f"Existencias: {producto['existencias']}")
            print(f"Proveedor: {producto['proveedor']['nombreProveedor']}")
            print()
    else:
        print("No hay productos en la lista")
    system("pause")

def buscarProducto():
    system("cls")
    codigo = int(input("Ingrese el código del producto a buscar: "))
    for i in listProductos:
        if i["codigo"] == codigo:
            print(f"{i['codigo']}. {i['nombre']}")
            print(f"Marca: {i['marca']}")
            print(f"Precio: {i['precio']}")
            print(f"Existencias: {i['existencias']}")
            print(f"Proveedor: {i['proveedor']['nombreProveedor']}")
            print()
            break
    else:
        print("Producto no encontrado")
    system("pause")

def guardarInventario():
    arch.guardarInventario(listProductos)

def cargarInventario():
    arch.cargarInventario(listProductos)

def menuPrincipal():
    while True:
        try:
            system("cls")
            print("----------Bienvenido al programa de gestión de productos----------")
            print("1. Agregar producto")
            print("2. Eliminar producto")
            print("3. Actualizar precio de producto")
            print("4. Listar productos")
            print("5. Buscar producto")
            print("6. Guardar inventario en archivo")
            print("7. Cargar inventario desde archivo")
            print("8. Salir")

            opcion = int(input("Elija una opción: "))

            if opcion == 1:
                agregarProducto()
            elif opcion == 2:
                eliminarProducto()
            elif opcion == 3:
                actualizarPrecioProducto()
            elif opcion == 4:
                listarProductos()
            elif opcion == 5:
                buscarProducto()
            elif opcion == 6:
                guardarInventario()
            elif opcion == 7:
                cargarInventario()
            elif opcion == 8:
                exit()
            else:
                print("Opción no válida")

        except ValueError:
            system("cls")
            print("Error: Ingrese un valor válido")
            system("pause")

if __name__ == "__main__":
    menuPrincipal()
















