
from os import system

def guardarInventario(listProductos):
    system("cls")
    with open("inventario.txt", "w") as archivo:
        for producto in listProductos:
            proveedor = producto['proveedor']
            linea = f"{producto['codigo']},{producto['nombre']},{producto['marca']},{producto['precio']},{producto['existencias']},{proveedor['codigoProveedor']},{proveedor['nombreProveedor']},{proveedor['paisProveedor']}\n"
            archivo.write(linea)
    print("Productos guardados en archivo exitosamente")
    system("pause")

def cargarInventario(listProductos):
    system("cls")
    listProductos.clear() 
    try:
        with open("inventario.txt", "r") as archivo:
            for linea in archivo:
                campos = linea.strip().split(',')
                if len(campos) == 8:
                    producto = {
                        'codigo': int(campos[0]),
                        'nombre': campos[1],
                        'marca': campos[2],
                        'precio': float(campos[3]),
                        'existencias': int(campos[4]),
                        'proveedor': {
                            'codigoProveedor': int(campos[5]),
                            'nombreProveedor': campos[6],
                            'paisProveedor': campos[7]
                        }
                    }
                    listProductos.append(producto)
        print("Productos cargados exitosamente")

    except ValueError:
        print(f"Error al cargar el archivo de inventario")
    system("pause")



