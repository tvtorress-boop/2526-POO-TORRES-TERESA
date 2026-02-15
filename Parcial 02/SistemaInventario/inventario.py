from producto import Producto

# Clase Inventario
# Gestiona una lista de productos

class Inventario:
    def __init__(self):
        # Lista donde se guardan los productos
        self.productos = []

    def añadir_producto(self, producto):
        # Verifica que el ID sea único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: el ID ya existe.")
                return
        self.productos.append(producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                encontrados.append(p)

        if not encontrados:
            print("No se encontraron productos.")
        else:
            for p in encontrados:
                print(p)

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)
