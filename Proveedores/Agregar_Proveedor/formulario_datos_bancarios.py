from tkinter import *
from tkinter import ttk 

class Formulario_datos_bancarios():
       
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.frame, text = "C.C.C:").place(relx = 0.02, rely = 0.2, relheight = 0.15)
        self.CCC = ttk.Entry(self.frame)
        self.CCC.place(relx = 0.14 , rely = 0.2, relwidth = 0.7, relheight = 0.15)
        
        ttk.Label(self.frame, text = "Banco:").place(relx = 0.02, rely = 0.65, relheight = 0.15)
        self.banco = ttk.Entry(self.frame)
        self.banco.place(relx = 0.14 , rely = 0.65, relwidth = 0.7, relheight = 0.15)

    def devolver_valores(self):
        return [self.CCC, self.banco]