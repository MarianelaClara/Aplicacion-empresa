from tkinter import *
from tkinter import ttk 

class Formulario1():
       
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.frame, text = "Identificación fiscal:").place(relx = 0.02, rely = 0.07, relheight = 0.15)
        opciones = ["C.U.I.T", "D.N.I"]
        lista_desplegable = ttk.Combobox(self.frame, state = 'readonly', justify='center')
        
        lista_desplegable['values'] = opciones
        lista_desplegable.current(0)
        lista_desplegable.place(relx = 0.35, rely = 0.07, relwidth = 0.2, relheight = 0.15)
        
        id_fiscal = ttk.Entry(self.frame)
        id_fiscal.place(relx = 0.6, rely = 0.07, relwidth = 0.3, relheight = 0.15)

        ttk.Label(self.frame, text = "Nombre fiscal:").place(relx = 0.02, rely = 0.425, relheight = 0.15)
        nombre_fiscal = ttk.Entry(self.frame)
        nombre_fiscal.place(relx = 0.26, rely = 0.425, relwidth = 0.3, relheight = 0.15)

        ttk.Label(self.frame, text = "Nombre comercial:").place(relx = 0.02, rely = 0.78, relheight = 0.15)
        nombre_comercial = ttk.Entry(self.frame)
        nombre_comercial.place(relx = 0.31, rely = 0.78, relwidth = 0.3, relheight = 0.15)
            
        return [lista_desplegable, id_fiscal, nombre_fiscal, nombre_comercial]