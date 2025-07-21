import tkinter as tk
from tkinter import ttk, messagebox

# Lista para guardar las asignaturas
asignaturas = []
id_counter = 1  # Para asignar IDs únicos


def crear_asignatura():
    global id_counter
    nombre = entry_nombre.get()
    creditos = entry_creditos.get()

    if not nombre or not creditos:
        messagebox.showwarning("Campos vacíos", "Completa todos los campos")
        return

    asignaturas.append({"id": id_counter, "nombre": nombre, "creditos": creditos})
    id_counter += 1
    mostrar_asignaturas()
    limpiar_campos()

def mostrar_asignaturas():
    for row in tree.get_children():
        tree.delete(row)
    for asignatura in asignaturas:
        tree.insert("", "end", values=(asignatura["id"], asignatura["nombre"], asignatura["creditos"]))

def actualizar_asignatura():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selección requerida", "Selecciona una asignatura para actualizar")
        return

    index = tree.index(selected[0])
    nombre = entry_nombre.get()
    creditos = entry_creditos.get()

    if not nombre or not creditos:
        messagebox.showwarning("Campos vacíos", "Completa todos los campos")
        return

    asignaturas[index]["nombre"] = nombre
    asignaturas[index]["creditos"] = creditos
    mostrar_asignaturas()
    limpiar_campos()

def eliminar_asignatura():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selección requerida", "Selecciona una asignatura para eliminar")
        return

    index = tree.index(selected[0])
    del asignaturas[index]
    mostrar_asignaturas()
    limpiar_campos()

def seleccionar_asignatura(event):
    selected = tree.selection()
    if selected:
        index = tree.index(selected[0])
        asignatura = asignaturas[index]
        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(0, asignatura["nombre"])
        entry_creditos.delete(0, tk.END)
        entry_creditos.insert(0, asignatura["creditos"])

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_creditos.delete(0, tk.END)

# Interfaz
root = tk.Tk()
root.title("Interfaz de Asignaturas")


tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Créditos:").grid(row=1, column=0, padx=5, pady=5)
entry_creditos = tk.Entry(root)
entry_creditos.grid(row=1, column=1, padx=5, pady=5)

# Botones
tk.Button(root, text="Crear", command=crear_asignatura).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="Actualizar", command=actualizar_asignatura).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Eliminar", command=eliminar_asignatura).grid(row=2, column=2, padx=5, pady=5)


columns = ("ID", "Nombre", "Créditos")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

tree.bind("<<TreeviewSelect>>", seleccionar_asignatura)

root.mainloop()
