import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# Crear ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")
# Frame para lista de eventos
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)
# Frame para ingresar datos
frame_datos = tk.Frame(ventana)
frame_datos.pack(pady=10)
# Frame para botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)
# Crear tabla de eventos
tabla = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripcion"), show="headings")
tabla.heading("Fecha", text="Fecha")
tabla.heading("Hora", text="Hora")
tabla.heading("Descripcion", text="Descripcion")
tabla.pack()
# Labels
tk.Label(frame_datos, text="Fecha:").grid(row=0, column=0)
tk.Label(frame_datos, text="Hora:").grid(row=1, column=0)
tk.Label(frame_datos, text="Descripcion:").grid(row=2, column=0)
#Entradas
entrada_fecha = tk.Entry(frame_datos)
entrada_hora = tk.Entry(frame_datos)
entrada_descripcion = tk.Entry(frame_datos)
entrada_fecha.grid(row=0, column=1)
entrada_hora.grid(row=1, column=1)
entrada_descripcion.grid(row=2, column=1)
def agregar_evento():
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()
    if fecha == "" or hora == "" or descripcion == "":
        messagebox.showerror("Error", "Complete todos los campos")
    else:
        tabla.insert("", "end", values=(fecha,hora,descripcion))
        entrada_fecha.delete(0, tk.END)
        entrada_hora.delete(0, tk.END)
        entrada_descripcion.delete(0, tk.END)
def eliminar_evento():
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showerror("Error", "Seleccione un evento")
    else:
        confirmar = messagebox.askyesno("Confirmar", "¿Eliminar evento?")
        if confirmar:
            tabla.delete(seleccion)
boton_agregar = tk.Button(frame_botones, text="Agregar evento", command=agregar_evento)
boton_agregar.grid(row=0, column=0, padx=10)
boton_eliminar = tk.Button(frame_botones, text="Eliminar evento", command=eliminar_evento)
boton_eliminar.grid(row=0, column=1, padx=10)
boton_salir = tk.Button(frame_botones, text="Salir", command=ventana.quit)
boton_salir.grid(row=0, column=2, padx=10)
ventana.mainloop()