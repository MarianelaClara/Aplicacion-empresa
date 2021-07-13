from tkinter import *
from tkinter import ttk 

class Formulario_contacto():
       
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.frame, text = "Teléfono:").place(relx = 0.02, rely = 0.04, relheight = 0.15)
        tel = ttk.Entry(self.frame)
        tel.place(relx = 0.19 , rely = 0.045, relwidth = 0.75, relheight = 0.11)
        
        ttk.Label(self.frame, text = "Móvil:").place(relx = 0.04, rely = 0.31, relheight = 0.15)
        mov = ttk.Entry(self.frame)
        mov.place(relx = 0.19, rely = 0.325, relwidth = 0.75, relheight = 0.11)

        ttk.Label(self.frame, text = "Persona de contacto:").place(relx = 0.02, rely = 0.58, relheight = 0.15)
        personaC = ttk.Entry(self.frame)
        personaC.place(relx = 0.35, rely = 0.595, relwidth = 0.59, relheight = 0.11)
        
        ttk.Label(self.frame, text = "E-Mail:").place(relx = 0.04, rely = 0.85, relheight = 0.15)
        Email = ttk.Entry(self.frame)
        Email.place(relx = 0.19, rely = 0.855, relwidth = 0.75, relheight = 0.11)
    
        return [tel, mov, personaC, Email]



