from tkinter import *
from tkinter import ttk 
from Proveedores.form_empresa import *
from Proveedores.form_domicilio import *
from Proveedores.form_datos_bancarios import *
from Proveedores.form_contacto import *
from Proveedores.form_observaciones import *
from Proveedores.style import estilo

def borrar(l1, l2, l3, l4, l5):
    l = l1 + l2 + l3 + l4 

    for x in l:
        if(x.get() != ""):
            x.delete(0, END)
    
    if(l5[0].get('1.0', END) != ""):
        l5[0].delete("1.0","end")

def agregarProv(frame):

    menu1 = ttk.LabelFrame(frame, text = "Empresa")
    menu1.place(relx = 0.03, rely = 0.02, relwidth = 0.45, relheight = 0.30)
    
    menu2 = ttk.LabelFrame(frame, text = "Domicilio")
    menu2.place(relx = 0.03, rely = 0.35, relwidth = 0.45, relheight = 0.30)
    
    menu3 = ttk.LabelFrame(frame, text = "Datos bancarios")
    menu3.place(relx = 0.03, rely = 0.68, relwidth = 0.45, relheight = 0.30)
    
    menu4 = ttk.LabelFrame(frame, text = "Contacto")
    menu4.place(relx = 0.52, rely = 0.02, relwidth = 0.45, relheight = 0.42)

    menu5 = ttk.LabelFrame(frame, text = "Observaciones")
    menu5.place(relx = 0.52, rely = 0.46, relwidth = 0.45, relheight = 0.4)

    dic1 = cuadro1(menu1)
    dic2 = cuadro2(menu2)
    dic3 = cuadro3(menu3)
    dic4 = cuadro4(menu4)
    dic5 = cuadro5(menu5)
    
    b = ttk.Button(frame, text = "Borrar todo", style='W.TButton', command = lambda:borrar(dic1.get("borrar"), dic2.get("borrar"), dic3.get("borrar"), dic4.get("borrar"), dic5.get("borrar")))
    b.place(relx = 0.52, rely = 0.90, relwidth = 0.1, relheight = 0.08)

    ttk.Button(frame, text = "Guardar", style='W.TButton').place(relx = 0.891, rely = 0.90, relwidth = 0.08, relheight = 0.08)
    
    

    