class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True

    def obtener_titulo(self):
        return self.info[0]

    def obtener_autor(self):
        return self.info[1]

    def mostrar(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.info[0]} - {self.info[1]} | {self.categoria} | ISBN: {self.isbn} | {estado}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros(self):
        if not self.libros_prestados:
            print("No tiene libros prestados")
        else:
            for libro in self.libros_prestados:
                print(libro.mostrar())


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.ids_usuarios = set()

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado")
        else:
            print("El ID ya existe")

    def baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            if libro.disponible:
                libro.disponible = False
                usuario.prestar_libro(libro)
                print("Libro prestado correctamente")
            else:
                print("El libro no está disponible")

    def devolver_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            libro.disponible = True
            usuario.devolver_libro(libro)
            print("Libro devuelto")

    def buscar_titulo(self, titulo):
        for libro in self.libros.values():
            if titulo.lower() in libro.obtener_titulo().lower():
                print(libro.mostrar())

    def buscar_autor(self, autor):
        for libro in self.libros.values():
            if autor.lower() in libro.obtener_autor().lower():
                print(libro.mostrar())

    def buscar_categoria(self, categoria):
        for libro in self.libros.values():
            if categoria.lower() in libro.categoria.lower():
                print(libro.mostrar())


biblioteca = Biblioteca()

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "9780307474728")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "9788420412146")
libro3 = Libro("1984", "George Orwell", "Distopía", "9780451524935")
libro4 = Libro("El principito", "Antoine de Saint-Exupéry", "Fábula", "9780156012195")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)

usuario1 = Usuario("Carlos Mendoza", "U001")
usuario2 = Usuario("Ana Torres", "U002")

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

biblioteca.prestar_libro("9780451524935", "U001")
biblioteca.prestar_libro("9780156012195", "U002")

print("Libros de Carlos:")
usuario1.listar_libros()

print("Buscar por autor Orwell:")
biblioteca.buscar_autor("Orwell")

biblioteca.devolver_libro("9780451524935", "U001")

print("Libros de Carlos después de devolver:")
usuario1.listar_libros()