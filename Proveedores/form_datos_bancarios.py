from tkinter import *
from tkinter import ttk 
from Proveedores.style import *

def cuadro3(menu3):
    
    one = StringVar()
    two = StringVar()
    three = StringVar()
    four = StringVar()
    banco = StringVar()
    
    ttk.Label(menu3, text = "C.C.C:").place(relx = 0.02, rely = 0.2, relheight = 0.15)
    uno = ttk.Entry(menu3, textvariable = 1)
    uno.place(relx = 0.14 , rely = 0.2, relwidth = 0.08, relheight = 0.15)
    dos = ttk.Entry(menu3, textvariable = 2)
    dos.place(relx = 0.23 , rely = 0.2, relwidth = 0.08, relheight = 0.15)
    tres = ttk.Entry(menu3, textvariable = 3)
    tres.place(relx = 0.32 , rely = 0.2, relwidth = 0.05, relheight = 0.15)
    cuatro = ttk.Entry(menu3, textvariable = 4)
    cuatro.place(relx = 0.38 , rely = 0.2, relwidth = 0.2, relheight = 0.15)
    ttk.Button(menu3, text = "Otros datos").place(relx = 0.6, rely = 0.18, relwidth = 0.2, relheight = 0.2)

    ttk.Label(menu3, text = "Banco:").place(relx = 0.02, rely = 0.65, relheight = 0.15)
    banc = ttk.Entry(menu3, textvariable = banco)
    banc.place(relx = 0.15 , rely = 0.65, relwidth = 0.7, relheight = 0.15)

    datos = {"guardar": [one, two, three, four, banco], "borrar": [uno, dos, tres, cuatro, banc]}

    return datos