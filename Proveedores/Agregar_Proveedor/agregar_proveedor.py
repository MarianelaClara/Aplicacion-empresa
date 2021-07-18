from tkinter import *
from tkinter import ttk 
from Formularios.formulario_empresa import *
from Formularios.formulario_domicilio import *
from Formularios.formulario_datos_bancarios import *
from Formularios.formulario_contacto import *
from Formularios.formulario_observaciones import *
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

        formulario_empresa = Formulario_empresa(self.frame1, 0.03, 0.02, 0.45, 0.30, 'p')
        l1 = formulario_empresa.devolver_valores()
        formulario_domicilio = Formulario_domicilio(self.frame1, 0.03, 0.35, 0.45, 0.30)
        l2 = formulario_domicilio.devolver_valores()
        formulario_datos_bancarios = Formulario_datos_bancarios(self.frame1, 0.03, 0.68, 0.45, 0.30)
        l3 = formulario_datos_bancarios.devolver_valores()
        formulario_contacto = Formulario_contacto(self.frame1, 0.52, 0.02, 0.45, 0.42)
        l4 = formulario_contacto.devolver_valores()
        formulario_observaciones = Formulario_observaciones(self.frame1, 0.52, 0.46, 0.45, 0.4)
        l5 = formulario_observaciones.devolver_valores()
        
        b = ttk.Button(self.frame1, text = "Borrar todo", command = lambda:borrar(l1, l2, l3, l4, l5))
        b.place(relx = 0.52, rely = 0.90, relwidth = 0.1, relheight = 0.08)

        proveedor = Posible_proveedor(self.frame0)
        g = ttk.Button(self.frame1, text = "Guardar", command = lambda:proveedor.controlar(l1, l2, l3, l4, l5))
        g.place(relx = 0.891, rely = 0.90, relwidth = 0.08, relheight = 0.08)
