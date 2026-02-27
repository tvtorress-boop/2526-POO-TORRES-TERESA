import json
import os

# =========================
# Clase Producto
# =========================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Conversión a diccionario (para JSON)
    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )


# =========================
# Clase Inventario
# =========================
class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.productos = {}  # Diccionario {id: Producto}
        self.archivo = archivo
        self.cargar_inventario()

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = self.productos.get(id_producto)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("\nINVENTARIO")
        for p in self.productos.values():
            print(
                f"ID: {p.get_id()} | "
                f"Nombre: {p.get_nombre()} | "
                f"Cantidad: {p.get_cantidad()} | "
                f"Precio: ${p.get_precio()}"
            )

    # =========================
    # Archivos
    # =========================
    def guardar_inventario(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(
                {id_: p.to_dict() for id_, p in self.productos.items()},
                f,
                indent=4
            )
        print("Inventario guardado en archivo.")

    def cargar_inventario(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                for id_, prod_data in data.items():
                    self.productos[id_] = Producto.from_dict(prod_data)


# =========================
# Menú interactivo
# =========================
def menu():
    inventario = Inventario()

    while True:
        print("""
======== MENÚ INVENTARIO ========
1. Añadir producto
2. Eliminar producto
3. Actualizar producto
4. Buscar producto por nombre
5. Mostrar inventario
6. Guardar y salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto(Producto(id_p, nombre, cantidad, precio))

        elif opcion == "2":
            id_p = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID del producto: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            inventario.actualizar_producto(
                id_p,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            for p in resultados:
                print(f"{p.get_id()} - {p.get_nombre()}")

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            inventario.guardar_inventario()
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida.")


# =========================
# Programa principal
# =========================
if __name__ == "__main__":
    menu()