from tkinter import *
from tkinter import ttk 

class Formulario_empresa():
       
    def __init__(self, frame, posx, posy, ancho, alto, tipo):
        self.frame = frame
        self.posx = posx
        self.posy = posy
        self.ancho = ancho
        self.alto = alto
        self.tipo = tipo
        self.create_widgets()

    def create_widgets(self):
        cuadro = LabelFrame(self.frame, text = "EMPRESA", background = "#4B4C56", foreground = "#ECECEF")
        cuadro.place(relx = self.posx, rely = self.posy, relwidth = self.ancho, relheight = self.alto)
        
        ttk.Label(cuadro, text = "Identificación fiscal:").place(relx = 0.02, rely = 0.07, relheight = 0.15)

        self.lista_desplegable = ttk.Combobox(cuadro, state = 'readonly', justify='center')

        self.id_fiscal = ttk.Entry(cuadro)
        
        if (self.tipo == 'p'):
            opciones = ["C.U.I.T", "D.N.I"]
            self.lista_desplegable.place(relx = 0.35, rely = 0.07, relwidth = 0.2, relheight = 0.15)
            self.id_fiscal.place(relx = 0.6, rely = 0.07, relwidth = 0.35, relheight = 0.15)
        else:
            opciones = ["C.U.I.T", "NIF/IVA (NIF operador intercomunitario)", "Documento oficial de  identificacion expedido por el territorio de residencia", 
            "Pasaporte",
            "Certificado de residencia fiscal", "Otro documento probatorio"]
            self.lista_desplegable.configure(style = 'Cliente.TCombobox')
            self.lista_desplegable.place(relx = 0.32, rely = 0.07, relwidth = 0.35, relheight = 0.15)
            self.id_fiscal.place(relx = 0.69, rely = 0.07, relwidth = 0.3, relheight = 0.15)
  
        self.lista_desplegable['values'] = opciones
        self.lista_desplegable.current(0)

        ttk.Label(cuadro, text = "Nombre fiscal:").place(relx = 0.02, rely = 0.425, relheight = 0.15)
        self.nombre_fiscal = ttk.Entry(cuadro)
        self.nombre_fiscal.place(relx = 0.26, rely = 0.425, relwidth = 0.35, relheight = 0.15)

        ttk.Label(cuadro, text = "Nombre comercial:").place(relx = 0.02, rely = 0.78, relheight = 0.15)
        self.nombre_comercial = ttk.Entry(cuadro)
        self.nombre_comercial.place(relx = 0.31, rely = 0.78, relwidth = 0.35, relheight = 0.15)

    def devolver_valores(self):  
        return [self.lista_desplegable, self.id_fiscal, self.nombre_fiscal, self.nombre_comercial]