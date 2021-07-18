from tkinter import *
from tkinter import ttk 

class Formulario_datos_bancarios():
       
    def __init__(self, frame, posx, posy, ancho, alto):
        self.frame = frame
        self.posx = posx
        self.posy = posy
        self.ancho = ancho
        self.alto = alto
        self.create_widgets()

    def create_widgets(self):

        cuadro = LabelFrame(self.frame, text = "DATOS BANCARIOS", background = "#4B4C56", foreground = "#ECECEF")
        cuadro.place(relx = self.posx, rely = self.posy, relwidth = self.ancho, relheight = self.alto)

        ttk.Label(cuadro, text = "C.C.C:").place(relx = 0.02, rely = 0.2, relheight = 0.15)
        self.CCC = ttk.Entry(cuadro)
        self.CCC.place(relx = 0.14 , rely = 0.2, relwidth = 0.7, relheight = 0.15)
        
        ttk.Label(cuadro, text = "Banco:").place(relx = 0.02, rely = 0.65, relheight = 0.15)
        self.banco = ttk.Entry(cuadro)
        self.banco.place(relx = 0.14 , rely = 0.65, relwidth = 0.7, relheight = 0.15)

    def devolver_valores(self):
        return [self.CCC, self.banco]