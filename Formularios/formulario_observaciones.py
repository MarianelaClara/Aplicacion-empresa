from tkinter import *
from tkinter import ttk 

class Formulario_observaciones():
       
    def __init__(self, frame, posx, posy, ancho, alto):
        self.frame = frame
        self.posx = posx
        self.posy = posy
        self.ancho = ancho
        self.alto = alto
        self.create_widgets()

    def create_widgets(self):

        cuadro = LabelFrame(self.frame, text = "OBSERVACIONES", background = "#4B4C56", foreground = "#ECECEF")
        cuadro.place(relx = self.posx, rely = self.posy, relwidth = self.ancho, relheight = self.alto)

        self.observaciones = Text(cuadro, highlightcolor='#BDBDC5', background = "#C5C5CD", selectbackground="#6868B5", selectforeground = "black")
        self.observaciones.place(relx = 0.02, rely = 0.03, relwidth = 0.96, relheight = 0.93)

    def devolver_valores(self):
        return [self.observaciones]