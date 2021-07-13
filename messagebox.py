from tkinter import *
from tkinter import ttk 

def porciento(x,y):
    return (x*y)//100

class Messagebox():
    def __init__(self, frame):
        self.frame = frame
    
    def create_widgets(self, mensaje, titulo):
        messagebox = Toplevel(self.frame)
        messagebox.title(titulo)
        ancho = self.frame.winfo_screenwidth()
        alto = self.frame.winfo_screenheight()
        x = porciento(25, ancho)
        y = porciento(25, alto)
        messagebox.geometry(str(x) + "x" + str(y))
        messagebox.resizable(height = 0, width = 0)





