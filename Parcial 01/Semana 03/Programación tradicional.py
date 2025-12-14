# Programación Tradicional

nota1 = 8
nota2 = 9
nota3 = 7

def promedio_tradicional(a, b, c):
    return (a + b + c) / 3

resultado_tradicional = promedio_tradicional(nota1, nota2, nota3)
print("Promedio (Tradicional):", resultado_tradicional)


# Programación Orientada a Objetos

class Alumno:
    def __init__(self, n1, n2, n3):
        self.nota1 = n1
        self.nota2 = n2
        self.nota3 = n3

    def promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

alumno = Alumno(8, 9, 7)
resultado_poo = alumno.promedio()
print("Promedio (POO):", resultado_poo)
