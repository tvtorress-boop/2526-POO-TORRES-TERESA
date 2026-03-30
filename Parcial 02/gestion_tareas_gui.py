import tkinter as tk
ventana = tk.Tk()
ventana.title("Gestion de Tareas")
ventana.geometry("400x400")
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)
lista_tareas = tk.Listbox(ventana, width=40, height=10)
lista_tareas.pack(pady=10)
def añadir_tarea(event=None):
    tarea = entrada.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)
def completar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        texto = lista_tareas.get(seleccion)
        lista_tareas.delete(seleccion)
        lista_tareas.insert(seleccion, "✔ "+ texto)
def eliminar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)
btn_añadir = tk.Button(ventana, text="Añadir", command=añadir_tarea)
btn_añadir.pack(pady=5)
btn_completar = tk.Button(ventana, text="Completar", command=completar_tarea)
btn_completar.pack(pady=5)
btn_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_tarea)
btn_eliminar.pack(pady=5)
ventana.bind("<Return>", añadir_tarea)   # Enter
ventana.bind("c", completar_tarea)   # tecla c
ventana.bind("<Delete>", eliminar_tarea) # Delete
ventana.bind("<Escape>", lambda e:ventana.destroy()) # salir
ventana.mainloop()
