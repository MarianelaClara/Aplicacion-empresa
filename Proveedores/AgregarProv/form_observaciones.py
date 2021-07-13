from tkinter import *
from tkinter import ttk 

class Formulario_observaciones():
       
    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()

    def create_widgets(self):
        observaciones = Text(self.frame, highlightcolor='#BDBDC5', background = "#C5C5CD", selectbackground="#6868B5", selectforeground = "black")
        observaciones.place(relx = 0.02, rely = 0.03, relwidth = 0.96, relheight = 0.93)
        
        return [observaciones]