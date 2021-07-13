from tkinter import *
from tkinter import ttk 

class Formulario_domicilio():
       
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.frame, text = "Domicilio:").place(relx = 0.02, rely = 0.07, relheight = 0.15)
        self.domicilio = ttk.Entry(self.frame)
        self.domicilio.place(relx = 0.19 , rely = 0.07, relwidth = 0.7, relheight = 0.15)
        
        ttk.Label(self.frame, text = "Código postal:").place(relx = 0.02, rely = 0.425, relheight = 0.15)
        self.codigo_postal = ttk.Entry(self.frame)
        self.codigo_postal.place(relx = 0.24, rely = 0.425, relwidth = 0.14, relheight = 0.15)

        ttk.Button(self.frame, text = "Buscar").place(relx = 0.40, rely = 0.41, relwidth = 0.13, relheight = 0.2)

        ttk.Label(self.frame, text = "Ciudad:").place(relx = 0.55, rely = 0.425, relheight = 0.15)
        self.ciudad = ttk.Entry(self.frame)
        self.ciudad.place(relx = 0.68, rely = 0.425, relwidth = 0.3, relheight = 0.15)

        ttk.Label(self.frame, text = "Provincia:").place(relx = 0.02, rely = 0.78, relheight = 0.15)
        self.provincia = ttk.Entry(self.frame)
        self.provincia.place(relx = 0.19, rely = 0.78, relwidth = 0.35, relheight = 0.15)
        
        ttk.Label(self.frame, text = "País:").place(relx = 0.57, rely = 0.78, relheight = 0.15)
        self.pais = ttk.Entry(self.frame)
        self.pais.place(relx = 0.68, rely = 0.78, relwidth = 0.3, relheight = 0.15)

    def devolver_valores(self):
        return [self.domicilio, self.codigo_postal, self.provincia, self.ciudad, self.pais]