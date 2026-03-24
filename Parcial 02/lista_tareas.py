import tkinter as tk
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)
lista_tareas = tk.Listbox(ventana, width=40, height=10)
lista_tareas.pack(pady=10)
def añadir_tarea():
    tarea = entrada.get()
    if tarea!="":
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)
def completar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        tarea = lista_tareas.get(seleccion)
        lista_tareas.delete(seleccion)
        lista_tareas.insert(seleccion, "✔ " + tarea)
def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        tarea = lista_tareas.delete(seleccion)
btn_agregar = tk.Button(ventana, text="Añadir Tarea", command=añadir_tarea)
btn_agregar.pack(pady=5)
btn_completar = tk.Button(ventana, text="Marcar como Completada", command=completar_tarea)
btn_completar.pack(pady=5)
btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)
entrada.bind("<Return>", lambda event: añadir_tarea())
lista_tareas.bind("<Double-Button-1>", lambda event: completar_tarea())
ventana.mainloop()
