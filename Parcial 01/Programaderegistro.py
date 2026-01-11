"""
Programa: Registro básico de un colegio
Descripción: Gestiona información básica de un estudiante.
"""

# Datos del estudiante
student_id = 1            # integer
student_name = "Teresa Torres" # string
student_average = 8.5     # float
is_enrolled = True        # boolean

# Mostrar información
def show_student():
    print("ID:", student_id)
    print("Nombre:", student_name)
    print("Promedio:", student_average)
    print("Matriculado:", is_enrolled)

# Verificar aprobación
def is_approved(average):
    return average >= 7.0

# Ejecución
show_student()

if is_approved(student_average):
    print("Estado: Aprobado")
else:
    print("Estado: Reprobado")
