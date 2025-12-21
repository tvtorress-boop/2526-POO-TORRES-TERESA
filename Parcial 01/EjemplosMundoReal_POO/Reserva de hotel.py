# Sistema de Reservas de Hotel usando POO

class Habitacion:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio
        self.disponible = True

    def reservar(self):
        self.disponible = False


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        print(f"\nHabitaciones del hotel {self.nombre}:")
        for h in self.habitaciones:
            estado = "Disponible" if h.disponible else "Ocupada"
            print(f"Habitación {h.numero} - {estado} - ${h.precio}")


# Uso del sistema
hotel = Hotel("Hotel Central")

hab1 = Habitacion(101, 30)
hab2 = Habitacion(102, 40)

hotel.agregar_habitacion(hab1)
hotel.agregar_habitacion(hab2)

hab1.reservar()
hotel.mostrar_habitaciones()