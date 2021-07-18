from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter.font import Font

def porciento(x,y):
    return (x*y)//100

class Messageboxs():
    def __init__(self, frame):
        self.frame = frame

    def crear_cartel(self, mensaje, titulo, tipo):
        messagebox = Toplevel(self.frame)
        messagebox.title(titulo)
        font_texto_cartel = Font(size = 9)
        ancho = self.frame.winfo_screenwidth()
        alto = self.frame.winfo_screenheight()
        
        if(tipo == "warning"):
            #Centro el cartel de aviso.
            x = porciento(24, ancho)
            y = porciento(17, alto)
            mover1 = (ancho - x)//2
            mover2 = (alto - y)//2
            messagebox.geometry('%dx%d+%d+%d' % (x, y, mover1, mover2))
            messagebox.resizable(height = 0, width = 0)

            #Coloco imagen de aviso.
            load = Image.open('/home/marianela/Desktop/ArHard/Proveedores/Ver_Proveedores/Image/warning.png')
            imagen = ImageTk.PhotoImage(load)
            mepic = Label(messagebox, image = imagen)
            mepic.image = imagen
            mepic.place(rely = 0.2, relx = 0.04)

            #Texto del cartel.
            mensaje_error = Label(messagebox, text = mensaje, font = font_texto_cartel)
            mensaje_error.place(rely = 0.32, relx = 0.20)

            #Boton del cartel
            aceptar = ttk.Button(messagebox, text = "Aceptar",style = "Cartel.TButton", command = lambda:self.cerrar_cartel(messagebox))
            aceptar.place(relx = 0.7, rely = 0.65, relheight = 0.235, relwidth = 0.25)

        #Fijo la ventana de error hasta que la cierren.

    def cerrar_cartel(self, messagebox):
        messagebox.destroy()

    