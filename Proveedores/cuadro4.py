from tkinter import *
from tkinter import ttk 
from Proveedores.style import *

def cuadro4(menu4):

    telefono = StringVar()
    movil = StringVar()
    persCont = StringVar()
    mail = StringVar()

    ttk.Label(menu4, text = "Teléfono:").place(relx = 0.02, rely = 0.04, relheight = 0.15)
    tel = ttk.Entry(menu4, textvariable = telefono)
    tel.place(relx = 0.19 , rely = 0.045, relwidth = 0.75, relheight = 0.11)
    
    ttk.Label(menu4, text = "Móvil:").place(relx = 0.04, rely = 0.31, relheight = 0.15)
    mov = ttk.Entry(menu4, textvariable = movil)
    mov.place(relx = 0.19, rely = 0.325, relwidth = 0.75, relheight = 0.11)

    ttk.Label(menu4, text = "Persona de contacto:").place(relx = 0.02, rely = 0.58, relheight = 0.15)
    personaC = ttk.Entry(menu4, textvariable = persCont)
    personaC.place(relx = 0.35, rely = 0.595, relwidth = 0.59, relheight = 0.11)
    
    ttk.Label(menu4, text = "E-Mail:").place(relx = 0.04, rely = 0.85, relheight = 0.15)
    Email = ttk.Entry(menu4, textvariable = mail)
    Email.place(relx = 0.19, rely = 0.855, relwidth = 0.75, relheight = 0.11)
    
    datos =  {"guardar": [telefono, movil, persCont, mail], "borrar": [tel, mov, personaC, Email]}

    return datos