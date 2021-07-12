from tkinter import *
from tkinter import ttk 
from Proveedores.AgregarProv.form_empresa import *
from Proveedores.AgregarProv.form_domicilio import *
from Proveedores.AgregarProv.form_datos_bancarios import *
from Proveedores.AgregarProv.form_contacto import *
from Proveedores.AgregarProv.form_observaciones import *
from Proveedores.AgregarProv.borrarGuardar import *

def agregarProv(frame):
    menu1 = LabelFrame(frame, text = "EMPRESA", background = "#4B4C56", foreground = "#ECECEF")
    menu1.place(relx = 0.03, rely = 0.02, relwidth = 0.45, relheight = 0.30)
    
    menu2 = LabelFrame(frame, text = "DOMICILIO", background = "#4B4C56", foreground = "#ECECEF")
    menu2.place(relx = 0.03, rely = 0.35, relwidth = 0.45, relheight = 0.30)
    
    menu3 = LabelFrame(frame, text = "DATOS BANCARIOS", background = "#4B4C56", foreground = "#ECECEF")
    menu3.place(relx = 0.03, rely = 0.68, relwidth = 0.45, relheight = 0.30)
    
    menu4 = LabelFrame(frame, text = "CONTACTO", background = "#4B4C56", foreground = "#ECECEF")
    menu4.place(relx = 0.52, rely = 0.02, relwidth = 0.45, relheight = 0.42)

    menu5 = LabelFrame(frame, text = "OBSERVACIONES", background = "#4B4C56", foreground = "#ECECEF")
    menu5.place(relx = 0.52, rely = 0.46, relwidth = 0.45, relheight = 0.4)

    l1 = cuadro1(menu1)
    l2 = cuadro2(menu2)
    l3 = cuadro3(menu3)
    l4 = cuadro4(menu4)
    l5 = cuadro5(menu5)
    
    b = ttk.Button(frame, text = "Borrar todo", command = lambda:borrar(l1, l2, l3, l4, l5))
    b.place(relx = 0.52, rely = 0.90, relwidth = 0.1, relheight = 0.08)

    g = ttk.Button(frame, text = "Guardar", command = lambda:guardar(l1, l2, l3, l4, l5))
    g.place(relx = 0.891, rely = 0.90, relwidth = 0.08, relheight = 0.08)
    
    

    