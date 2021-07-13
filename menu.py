from tkinter import ttk
from Proveedores.AgregarProv.agregarProveedor import *

class Ventana():
       
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.create_widgets()
        

    def create_widgets(self):
        notebook = ttk.Notebook()
        notebook.pack(padx=10, pady=10, fill ="both")
            
        pestaña0 = ttk.Frame(notebook, width = self.x, height = self.y)
        pestaña0.pack(fill = "both")
        pestaña1 = ttk.Frame(notebook, width = self.x, height = self.y)
        pestaña1.pack(fill = "both")

        notebook.add(pestaña0, text = "Ver proveedores")
        notebook.add(pestaña1, text = "Agregar proveedor")

        agregar_proveedor = AgregarProveedor(pestaña1)
            
     
