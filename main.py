import tkinter as tk
from tkinter import messagebox
 
def agregar():
    nombre = entrada.get()
 
    if nombre == "":
        messagebox.showwarning("Escribe un nombre.")
        return
 
    lista.insert(tk.END, nombre)
    entrada.delete(0, tk.END)
    contador.config(text=f"Total: {lista.size()}")
 
def eliminar():
    try:
        seleccion = lista.curselection()[0]
        lista.delete(seleccion)
        contador.config(text=f"Total: {lista.size()}")
    except:
        messagebox.showerror("Error", "Ningun elemento seleccionado.")
 

ventana = tk.Tk()
ventana.title("Sistema de Usuarios")
ventana.geometry("650x450")
ventana.configure(bg="#1E1E2F")
ventana.resizable(False, False)
 
titulo = tk.Label(
    ventana,
    text="📋 Sistema de Usuarios",
    font=("Segoe UI", 22, "bold"),
    bg="#1E1E2F",
    fg="white"
)
titulo.pack(pady=20)
 
frame = tk.Frame(ventana, bg="#2C2F48", bd=2, relief="ridge")
frame.pack(padx=20, pady=10, fill="both", expand=True)
 
 
tk.Label(
    frame,
    text="Nombre:",
    font=("Segoe UI", 12),
    bg="#2C2F48",
    fg="white"
).pack(pady=(15,5))
 
entrada = tk.Entry(
    frame,
    font=("Segoe UI", 12),
    width=30,
    bd=0,
    justify="center"
)
entrada.pack()
 
 
frame_botones = tk.Frame(frame, bg="#2C2F48")
frame_botones.pack(pady=15)
 
boton_agregar = tk.Button(
    frame_botones,
text="Agregar",
bg="#00C853",
fg="white",
font=("Segoe UI", 11, "bold"),
 width=12, relief="flat", command=agregar)
boton_agregar.grid(row=0, column=0, padx=10)
 
boton_eliminar = tk.Button(
    frame_botones,
    text="Eliminar",
    bg="#D50000",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=12,
    relief="flat",
    command=eliminar
)
boton_eliminar.grid(row=0, column=1, padx=10)
 
 
lista = tk.Listbox(
    frame,
    font=("Segoe UI", 12),
    width=40,
    height=10,
    bg="#3A3D5C",
    fg="white", background="#00BCD4",
    bd=0)
lista.pack(pady=10)
 
 
contador = tk.Label(
    frame,
    text="Total: 0",
    font=("Segoe UI", 11),
    bg="#2C2F48",
    fg="#006AFF"
)
contador.pack(pady=10)
 
ventana.mainloop() 