from tkinter import *
from tkinter import ttk 

def cuadro2(menu2):

    ttk.Label(menu2, text = "Domicilio:").place(relx = 0.02, rely = 0.07, relheight = 0.15)
    domicilio = ttk.Entry(menu2)
    domicilio.place(relx = 0.19 , rely = 0.07, relwidth = 0.7, relheight = 0.15)
    
    ttk.Label(menu2, text = "Código postal:").place(relx = 0.02, rely = 0.425, relheight = 0.15)
    codPostal = ttk.Entry(menu2)
    codPostal.place(relx = 0.24, rely = 0.425, relwidth = 0.14, relheight = 0.15)

    ttk.Button(menu2, text = "Buscar").place(relx = 0.40, rely = 0.41, relwidth = 0.13, relheight = 0.2)

    ttk.Label(menu2, text = "Ciudad:").place(relx = 0.55, rely = 0.425, relheight = 0.15)
    ciudad = ttk.Entry(menu2)
    ciudad.place(relx = 0.68, rely = 0.425, relwidth = 0.3, relheight = 0.15)

    ttk.Label(menu2, text = "Provincia:").place(relx = 0.02, rely = 0.78, relheight = 0.15)
    provincia = ttk.Entry(menu2)
    provincia.place(relx = 0.19, rely = 0.78, relwidth = 0.35, relheight = 0.15)
    
    ttk.Label(menu2, text = "País:").place(relx = 0.57, rely = 0.78, relheight = 0.15)
    pais = ttk.Entry(menu2)
    pais.place(relx = 0.68, rely = 0.78, relwidth = 0.3, relheight = 0.15)

    return [domicilio, codPostal, provincia, ciudad, pais]