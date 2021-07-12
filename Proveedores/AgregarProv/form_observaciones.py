from tkinter import *
from tkinter import ttk 

def cuadro5(menu5):

    observaciones = Text(menu5, highlightcolor='#BDBDC5', background = "#C5C5CD", selectbackground="#6868B5", selectforeground = "black")
    observaciones.place(relx = 0.02, rely = 0.03, relwidth = 0.96, relheight = 0.93)
    
    return [observaciones]