from tkinter import *
from tkinter import ttk 

class Formulario_contacto():
       
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.frame, text = "Teléfono:").place(relx = 0.02, rely = 0.04, relheight = 0.15)
        self.telefono = ttk.Entry(self.frame)
        self.telefono.place(relx = 0.19 , rely = 0.045, relwidth = 0.75, relheight = 0.11)
        
        ttk.Label(self.frame, text = "Móvil:").place(relx = 0.04, rely = 0.31, relheight = 0.15)
        self.movil = ttk.Entry(self.frame)
        self.movil.place(relx = 0.19, rely = 0.325, relwidth = 0.75, relheight = 0.11)

        ttk.Label(self.frame, text = "Persona de contacto:").place(relx = 0.02, rely = 0.58, relheight = 0.15)
        self.persona_contacto = ttk.Entry(self.frame)
        self.persona_contacto.place(relx = 0.35, rely = 0.595, relwidth = 0.59, relheight = 0.11)
        
        ttk.Label(self.frame, text = "E-Mail:").place(relx = 0.04, rely = 0.85, relheight = 0.15)
        self.Email = ttk.Entry(self.frame)
        self.Email.place(relx = 0.19, rely = 0.855, relwidth = 0.75, relheight = 0.11)
    
    def devolver_valores(self):
        return [self.telefono, self.movil, self.persona_contacto, self.Email]



