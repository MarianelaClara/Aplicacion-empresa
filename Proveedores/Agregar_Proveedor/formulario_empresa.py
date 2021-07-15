from tkinter import *
from tkinter import ttk 

class Formulario_empresa():
       
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.frame, text = "Identificación fiscal:").place(relx = 0.02, rely = 0.07, relheight = 0.15)
        opciones = ["C.U.I.T", "D.N.I"]
        self.lista_desplegable = ttk.Combobox(self.frame, state = 'readonly', justify='center')
        
        self.lista_desplegable['values'] = opciones
        self.lista_desplegable.current(0)
        self.lista_desplegable.place(relx = 0.35, rely = 0.07, relwidth = 0.2, relheight = 0.15)
        
        self.id_fiscal = ttk.Entry(self.frame)
        self.id_fiscal.place(relx = 0.6, rely = 0.07, relwidth = 0.35, relheight = 0.15)

        ttk.Label(self.frame, text = "Nombre fiscal:").place(relx = 0.02, rely = 0.425, relheight = 0.15)
        self.nombre_fiscal = ttk.Entry(self.frame)
        self.nombre_fiscal.place(relx = 0.26, rely = 0.425, relwidth = 0.35, relheight = 0.15)

        ttk.Label(self.frame, text = "Nombre comercial:").place(relx = 0.02, rely = 0.78, relheight = 0.15)
        self.nombre_comercial = ttk.Entry(self.frame)
        self.nombre_comercial.place(relx = 0.31, rely = 0.78, relwidth = 0.35, relheight = 0.15)

    def devolver_valores(self):  
        return [self.lista_desplegable, self.id_fiscal, self.nombre_fiscal, self.nombre_comercial]