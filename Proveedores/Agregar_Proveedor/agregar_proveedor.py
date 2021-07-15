from tkinter import *
from tkinter import ttk 
from Proveedores.Agregar_Proveedor.formulario_empresa import *
from Proveedores.Agregar_Proveedor.formulario_domicilio import *
from Proveedores.Agregar_Proveedor.formulario_datos_bancarios import *
from Proveedores.Agregar_Proveedor.formulario_contacto import *
from Proveedores.Agregar_Proveedor.formulario_observaciones import *
from Proveedores.Agregar_Proveedor.mostrar_treeview import *

def borrar(l1, l2, l3, l4, l5):
    l = l1 + l2 + l3 + l4 

    for x in l:
        if(x.get() != ""):
            x.delete(0, END)
    
    if(l5[0].get('1.0', END) != ""):
        l5[0].delete("1.0","end")

class Agregar_proveedor():
       
    def __init__(self, frame1, frame0):
        self.frame1 = frame1
        self.frame0 = frame0
        self.create_widgets()

    def create_widgets(self):
        menu1 = LabelFrame(self.frame1, text = "EMPRESA", background = "#4B4C56", foreground = "#ECECEF")
        menu1.place(relx = 0.03, rely = 0.02, relwidth = 0.45, relheight = 0.30)
        
        menu2 = LabelFrame(self.frame1, text = "DOMICILIO", background = "#4B4C56", foreground = "#ECECEF")
        menu2.place(relx = 0.03, rely = 0.35, relwidth = 0.45, relheight = 0.30)
        
        menu3 = LabelFrame(self.frame1, text = "DATOS BANCARIOS", background = "#4B4C56", foreground = "#ECECEF")
        menu3.place(relx = 0.03, rely = 0.68, relwidth = 0.45, relheight = 0.30)
        
        menu4 = LabelFrame(self.frame1, text = "CONTACTO", background = "#4B4C56", foreground = "#ECECEF")
        menu4.place(relx = 0.52, rely = 0.02, relwidth = 0.45, relheight = 0.42)

        menu5 = LabelFrame(self.frame1, text = "OBSERVACIONES", background = "#4B4C56", foreground = "#ECECEF")
        menu5.place(relx = 0.52, rely = 0.46, relwidth = 0.45, relheight = 0.4)

        formulario_empresa = Formulario_empresa(menu1)
        l1 = formulario_empresa.devolver_valores()
        formulario_domicilio = Formulario_domicilio(menu2)
        l2 = formulario_domicilio.devolver_valores()
        formulario_datos_bancarios = Formulario_datos_bancarios(menu3)
        l3 = formulario_datos_bancarios.devolver_valores()
        formulario_contacto = Formulario_contacto(menu4)
        l4 = formulario_contacto.devolver_valores()
        formulario_observaciones = Formulario_observaciones(menu5)
        l5 = formulario_observaciones.devolver_valores()
        
        b = ttk.Button(self.frame1, text = "Borrar todo", command = lambda:borrar(l1, l2, l3, l4, l5))
        b.place(relx = 0.52, rely = 0.90, relwidth = 0.1, relheight = 0.08)

        proveedor = Posible_proveedor(self.frame0)
        g = ttk.Button(self.frame1, text = "Guardar", command = lambda:proveedor.controlar(l1, l2, l3, l4, l5))
        g.place(relx = 0.891, rely = 0.90, relwidth = 0.08, relheight = 0.08)
