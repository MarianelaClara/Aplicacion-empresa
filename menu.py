from tkinter import *
from tkinter import ttk
from Proveedores.agregarProveedor import agregarProv
from Proveedores.style import *

def porciento(x,y):
    return (x*y)//100

root = Tk()
root.title("App")
ancho = root.winfo_screenwidth()
alto = root.winfo_screenheight()
x = porciento(80,ancho)
y = porciento(80,alto)
root.geometry(str(x) + "x" + str(y))
root.resizable(height = 0, width = 0)
estilo(root)

# Crear el panel de pestañas.
notebook = ttk.Notebook()
notebook.pack(padx=10, pady=10, fill ="both")
       
frame0 = ttk.Frame(notebook, width = x, height = y)
frame0.pack(fill = "both")
frame1 = ttk.Frame(notebook, width = x, height = y)
frame1.pack(fill = "both")
      
notebook.add(frame0, text = "Ver proveedores")
notebook.add(frame1, text = "Agregar proveedor")

agregarProv(frame1)

root.mainloop()
