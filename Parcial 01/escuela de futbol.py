class Jugador:
    """
    Clase que representa a un jugador inscrito
    en una escuela de fútbol.
    """

    def __init__(self, nombre, edad, posicion):
        """
        Constructor:
        Se ejecuta cuando se crea el objeto Jugador.
        Inicializa los datos del jugador.
        """
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        print(f"Jugador inscrito: {self.nombre}, {self.edad} años, posición {self.posicion}")

    def entrenar(self):
        """Simula una sesión de entrenamiento"""
        print(f"{self.nombre} está entrenando como {self.posicion}.")

    def jugar_partido(self):
        """Simula que el jugador participa en un partido"""
        print(f"{self.nombre} está jugando el partido.")

    def __del__(self):
        """
        Destructor:
        Se ejecuta cuando el objeto es eliminado
        o cuando el programa finaliza.
        """
        print(f"El jugador {self.nombre} ha sido retirado de la escuela de fútbol.")


# Programa principal
if __name__ == "__main__":
    jugador1 = Jugador("Anthony Benavides", 19, "Delantero")

    jugador1.entrenar()
    jugador1.jugar_partido()

    # El destructor se ejecuta automáticamente al finalizar el programa
