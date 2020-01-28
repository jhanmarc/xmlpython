
from xml.dom import minidom
# inicializar para el xml
docXML = minidom.parse("productos.xml")

# datos especificos
nombre = docXML.getElementsByTagName("Nombre") [0]
print(nombre.firstChild.data)

# list de productos
listproductos = docXML.getElementsByTagName("Producto")


for producto in listproductos:
    sid = producto.getAttribute("id")
    nombre = producto.getElementsByTagName("NombreProducto")[0]
    descr = producto.getElementsByTagName("Descripcion")[0]
    precio = producto.getElementsByTagName("Precio")[0]
    disponible = producto.getElementsByTagName("Disponible")[0]

    print("id : " + sid)
    print("Nombre: " + nombre.firstChild.data)
    print("Descripcion: " + descr.firstChild.data)
    print("Precio: " + precio.firstChild.data)
    print("Disponible: " + disponible.firstChild.data)
    print("")
