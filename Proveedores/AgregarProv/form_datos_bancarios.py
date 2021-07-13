from tkinter import *
from tkinter import ttk 

class Formulario_datos_bancarios():
       
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.frame, text = "C.C.C:").place(relx = 0.02, rely = 0.2, relheight = 0.15)
        uno = ttk.Entry(self.frame)
        uno.place(relx = 0.14 , rely = 0.2, relwidth = 0.7, relheight = 0.15)
        
        ttk.Label(self.frame, text = "Banco:").place(relx = 0.02, rely = 0.65, relheight = 0.15)
        banco = ttk.Entry(self.frame)
        banco.place(relx = 0.14 , rely = 0.65, relwidth = 0.7, relheight = 0.15)

        return [uno, banco]