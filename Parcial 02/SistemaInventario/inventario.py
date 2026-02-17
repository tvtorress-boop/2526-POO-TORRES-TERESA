from producto import Producto

# Clase Inventario
# Gestiona una lista de productos y los guarda en un archivo

class Inventario:
    def __init__(self):
        # Lista donde se guardan los productos
        self.productos = []
        self.archivo = "inventario.txt"
        self.cargar_desde_archivo()

    def añadir_producto(self, producto):
        # Verifica que el ID sea único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: el ID ya existe.")
                return

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto añadido correctamente y guardado en archivo.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado y archivo actualizado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)

                self.guardar_en_archivo()
                print("Producto actualizado y guardado en archivo.")
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

    # ====== MANEJO DE ARCHIVOS ======

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(
                        f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    )
        except PermissionError:
            print("Error: no se pudo escribir en el archivo de inventario.")

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    idp, nombre, cantidad, precio = linea.strip().split(",")
                    producto = Producto(idp, nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
        except FileNotFoundError:
            # Si no existe el archivo, se crea vacío
            open(self.archivo, "w").close()
        except Exception:
            print("Error al leer el archivo de inventario.")
