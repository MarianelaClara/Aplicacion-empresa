from tkinter import ttk

class Ventana():
       
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.create_widgets()
        

    def create_widgets(self):
        notebook = ttk.Notebook()
        notebook.pack(padx=10, pady=10, fill ="both")
            
        frame0 = ttk.Frame(notebook, width = self.x, height = self.y)
        frame0.pack(fill = "both")
        frame1 = ttk.Frame(notebook, width = self.x, height = self.y)
        frame1.pack(fill = "both")

        notebook.add(frame0, text = "Ver proveedores")
        notebook.add(frame1, text = "Agregar proveedor")
            
     
