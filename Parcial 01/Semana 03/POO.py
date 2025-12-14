# Programación Orientada a Objetos (POO)
# Ejemplo: Gestión de un estudiante

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show_info(self):
        print("Nombre:", self.name)
        print("Calificación:", self.grade)

    def passed(self):
        if self.grade >= 7:
            print("Estado: Aprobado")
        else:
            print("Estado: Reprobado")

# Crear objeto
student1 = Student("Luis", 8)

# Uso de métodos
student1.show_info()
student1.passed()
