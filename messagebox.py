from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk

def porciento(x,y):
    return (x*y)//100

class Messagebox():
    def __init__(self, frame):
        self.frame = frame
    
    def create_widgets(self, mensaje, titulo):

        #Creo la ventana de error y la dimensiono.
        messagebox = Toplevel(self.frame)
        messagebox.title(titulo)
        ancho = self.frame.winfo_screenwidth()
        alto = self.frame.winfo_screenheight()
        x = porciento(25, ancho)
        y = porciento(25, alto)
        messagebox.geometry(str(x) + "x" + str(y))
        messagebox.resizable(height = 0, width = 0)

        #Coloco imagen de error.
        load = Image.open('error.png')
        imagen = ImageTk.PhotoImage(load)
        mepic = Label(messagebox, image = imagen, borderwidth = 0)
        mepic.image = imagen
        mepic.grid(row = 0, column = 0, padx = 10)

        #Fijo la ventana de error hasta que la cierren.
        messagebox.grab_set()





