import os
import subprocess

# ==========================================
# DASHBOARD ACADÉMICO - POO
# Proyecto: 2526-POO-TORRES-TERESA
# Estudiante: Teresa Valentina Torres
# ==========================================


def mostrar_codigo(ruta_script):
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            print("\n📄 CÓDIGO DEL SCRIPT\n")
            print(archivo.read())
            return True
    except Exception as e:
        print(f"⚠ Error al leer el archivo: {e}")
        return False


def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"⚠ Error al ejecutar el script: {e}")


def menu_principal():
    ruta_base = os.path.dirname(__file__)

    parciales = {
        '1': 'Parcial 01',
        '2': 'Parcial 02'
    }

    while True:
        print("\n==============================")
        print("📚 DASHBOARD - PROGRAMACIÓN OOP")
        print("==============================")
        print("1 - Parcial 01")
        print("2 - Parcial 02")
        print("0 - Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            print("👋 Saliendo del Dashboard.")
            break
        elif opcion in parciales:
            ruta_parcial = os.path.join(ruta_base, parciales[opcion])
            if os.path.exists(ruta_parcial):
                menu_carpetas(ruta_parcial)
            else:
                print("⚠ La carpeta no existe.")
        else:
            print("❌ Opción no válida.")


def menu_carpetas(ruta_parcial):
    items = os.listdir(ruta_parcial)

    while True:
        print(f"\n📁 CONTENIDO DE {os.path.basename(ruta_parcial)}")
        for i, item in enumerate(items, start=1):
            print(f"{i} - {item}")
        print("0 - Regresar")

        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            break

        try:
            index = int(opcion) - 1
            if 0 <= index < len(items):
                ruta_item = os.path.join(ruta_parcial, items[index])

                if os.path.isdir(ruta_item):
                    menu_scripts(ruta_item)
                elif ruta_item.endswith('.py'):
                    if mostrar_codigo(ruta_item):
                        ejecutar = input("¿Desea ejecutar el script? (1=Sí / 0=No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_item)
                else:
                    print("⚠ Archivo no compatible.")
            else:
                print("❌ Opción incorrecta.")
        except ValueError:
            print("❌ Ingrese un número válido.")


def menu_scripts(ruta_carpeta):
    scripts = [f for f in os.listdir(ruta_carpeta) if f.endswith('.py')]

    while True:
        print(f"\n🐍 SCRIPTS EN {os.path.basename(ruta_carpeta)}")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar")

        opcion = input("Seleccione un script: ")

        if opcion == '0':
            break

        try:
            index = int(opcion) - 1
            if 0 <= index < len(scripts):
                ruta_script = os.path.join(ruta_carpeta, scripts[index])
                if mostrar_codigo(ruta_script):
                    ejecutar = input("¿Desea ejecutar el script? (1=Sí / 0=No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)
            else:
                print("❌ Opción incorrecta.")
        except ValueError:
            print("❌ Ingrese un número válido.")


if __name__ == "__main__":
    menu_principal()