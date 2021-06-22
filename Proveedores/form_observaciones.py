from tkinter import *
from tkinter import ttk 
from Proveedores.style import *

def cuadro5(menu5):

    observaciones = Text(menu5, highlightcolor='#DFD6D8')
    observaciones.place(relx = 0.02, rely = 0.03, relwidth = 0.96, relheight = 0.93)
    
    datos = {"guardar": [observaciones], "borrar": [observaciones]}

    return datos