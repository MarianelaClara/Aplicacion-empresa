from tkinter import ttk
from Proveedores.Agregar_Proveedor.agregar_proveedor import *

class Notebook():
       
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

        ver_proveedor = Modificar_treeview(pestaña0)  
        agregar_proveedor = Agregar_proveedor(pestaña1, pestaña0)

            
     
