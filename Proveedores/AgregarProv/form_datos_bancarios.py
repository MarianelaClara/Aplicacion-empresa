from tkinter import *
from tkinter import ttk 

def cuadro3(menu3):
    
    ttk.Label(menu3, text = "C.C.C:").place(relx = 0.02, rely = 0.2, relheight = 0.15)
    uno = ttk.Entry(menu3)
    uno.place(relx = 0.14 , rely = 0.2, relwidth = 0.7, relheight = 0.15)
    
    ttk.Label(menu3, text = "Banco:").place(relx = 0.02, rely = 0.65, relheight = 0.15)
    banco = ttk.Entry(menu3)
    banco.place(relx = 0.14 , rely = 0.65, relwidth = 0.7, relheight = 0.15)

    return [uno, banco]