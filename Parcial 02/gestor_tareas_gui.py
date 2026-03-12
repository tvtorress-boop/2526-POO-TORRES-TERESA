# Importamos la librería tkinter
import tkinter as tk
from tkinter import messagebox

# -------------------------------
# FUNCIONES DE LA APLICACIÓN
# -------------------------------

def agregar_tarea():
    """
    Esta función agrega una tarea escrita por el usuario
    en el campo de texto a la lista de tareas.
    """
    tarea = entrada_tarea.get()

    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Escribe una tarea primero")


def eliminar_tarea():
    """
    Elimina la tarea seleccionada en la lista.
    """
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except:
        messagebox.showwarning("Advertencia", "Selecciona una tarea")


def limpiar_lista():
    """
    Borra todas las tareas de la lista.
    """
    lista_tareas.delete(0, tk.END)


# -------------------------------
# VENTANA PRINCIPAL
# -------------------------------

ventana = tk.Tk()
ventana.title("Gestor de Tareas - TIC")
ventana.geometry("400x350")
ventana.config(bg="#E8F0FE")

# -------------------------------
# ETIQUETA TITULO
# -------------------------------

titulo = tk.Label(
    ventana,
    text="Lista de Tareas Rápidas",
    font=("Arial", 16, "bold"),
    bg="#E8F0FE"
)
titulo.pack(pady=10)

# -------------------------------
# FRAME PARA ENTRADA DE TEXTO
# -------------------------------

frame_entrada = tk.Frame(ventana, bg="#E8F0FE")
frame_entrada.pack(pady=5)

label_tarea = tk.Label(frame_entrada, text="Nueva tarea:", bg="#E8F0FE")
label_tarea.pack(side=tk.LEFT)

entrada_tarea = tk.Entry(frame_entrada, width=25)
entrada_tarea.pack(side=tk.LEFT, padx=5)

boton_agregar = tk.Button(
    frame_entrada,
    text="Agregar",
    command=agregar_tarea
)
boton_agregar.pack(side=tk.LEFT)

# -------------------------------
# LISTA DE TAREAS
# -------------------------------

frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)

scroll = tk.Scrollbar(frame_lista)

lista_tareas = tk.Listbox(
    frame_lista,
    width=40,
    height=10,
    yscrollcommand=scroll.set
)

scroll.config(command=lista_tareas.yview)

lista_tareas.pack(side=tk.LEFT)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# -------------------------------
# BOTONES DE ACCIÓN
# -------------------------------

frame_botones = tk.Frame(ventana, bg="#E8F0FE")
frame_botones.pack(pady=10)

boton_eliminar = tk.Button(
    frame_botones,
    text="Eliminar tarea",
    command=eliminar_tarea
)
boton_eliminar.pack(side=tk.LEFT, padx=5)

boton_limpiar = tk.Button(
    frame_botones,
    text="Limpiar lista",
    command=limpiar_lista
)
boton_limpiar.pack(side=tk.LEFT, padx=5)

# -------------------------------
# EJECUCIÓN DE LA APP
# -------------------------------

ventana.mainloop()