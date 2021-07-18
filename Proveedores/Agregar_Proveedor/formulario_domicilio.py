from tkinter import *
from tkinter import ttk 
from tkinter.font import Font

class Formulario_domicilio():
       
    def __init__(self, frame, posx, posy, ancho, alto):
        self.frame = frame
        self.posx = posx
        self.posy = posy
        self.ancho = ancho
        self.alto = alto
        self.create_widgets()

    def create_widgets(self):

        cuadro = LabelFrame(self.frame, text = "DOMICILIO", background = "#4B4C56", foreground = "#ECECEF")
        cuadro.place(relx = self.posx, rely = self.posy, relwidth = self.ancho, relheight = self.alto)

        ttk.Label(cuadro, text = "Domicilio:").place(relx = 0.02, rely = 0.07, relheight = 0.15)
        self.domicilio = ttk.Entry(cuadro)
        self.domicilio.place(relx = 0.19 , rely = 0.07, relwidth = 0.7, relheight = 0.15)
        
        ttk.Label(cuadro, text = "Código postal:").place(relx = 0.02, rely = 0.425, relheight = 0.15)
        self.codigo_postal = ttk.Entry(cuadro)
        self.codigo_postal.place(relx = 0.24, rely = 0.425, relwidth = 0.14, relheight = 0.15)

        ttk.Button(cuadro, text = "Buscar").place(relx = 0.40, rely = 0.41, relwidth = 0.13, relheight = 0.2)

        ttk.Label(cuadro, text = "Ciudad:").place(relx = 0.55, rely = 0.425, relheight = 0.15)
        self.ciudad = ttk.Entry(cuadro)
        self.ciudad.place(relx = 0.68, rely = 0.425, relwidth = 0.3, relheight = 0.15)

        ttk.Label(cuadro, text = "Provincia:").place(relx = 0.02, rely = 0.78, relheight = 0.15)
        self.provincia = ttk.Entry(cuadro)
        self.provincia.place(relx = 0.19, rely = 0.78, relwidth = 0.35, relheight = 0.15)
        
        ttk.Label(cuadro, text = "País:").place(relx = 0.57, rely = 0.78, relheight = 0.15)
        self.pais = ttk.Entry(cuadro)
        self.pais.place(relx = 0.68, rely = 0.78, relwidth = 0.3, relheight = 0.15)

    def devolver_valores(self):
        return [self.domicilio, self.codigo_postal, self.provincia, self.ciudad, self.pais]