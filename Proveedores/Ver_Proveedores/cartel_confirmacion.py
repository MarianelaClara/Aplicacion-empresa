from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter.font import Font

def porciento(x,y):
    return (x*y)//100

class Cartel_confirmacion():
    def __init__(self, frame, mensaje, titulo, argumentos, funcion):
        self.frame = frame
        self.mensaje = mensaje
        self.titulo = titulo
        self.argumentos = argumentos
        self.funcion = funcion
        self.destruir = False

    def crear_cartel(self):
        self.messagebox = Toplevel(self.frame)
        self.messagebox.title(self.titulo)
        font_texto_cartel = Font(size = 9)
        ancho = self.frame.winfo_screenwidth()
        alto = self.frame.winfo_screenheight()

        #Centro el cartel.
        x = porciento(25, ancho)
        y = porciento(20, alto)
        mover1 = (ancho - x)//2
        mover2 = (alto - y)//2
        self.messagebox.geometry('%dx%d+%d+%d' % (x, y, mover1, mover2))
        self.messagebox.resizable(height = 0, width = 0)

        #Coloco imagen de aviso.
        load = Image.open('/home/marianela/Desktop/ArHard/Proveedores/Ver_Proveedores/Image/pregunta.png')
        imagen = ImageTk.PhotoImage(load)
        mepic = Label(self.messagebox, image = imagen)
        mepic.image = imagen
        mepic.place(rely = 0.2, relx = 0.03)

        #Texto del cartel.
        mensaje_error = Label(self.messagebox, text = self.mensaje, font = font_texto_cartel)
        mensaje_error.place(rely = 0.27, relx = 0.19)

        #Botones del cartel.
        no = ttk.Button(self.messagebox, text = "No",style = "Cartel.TButton", command = self.messagebox.destroy)
        no.place(relx = 0.1, rely = 0.7, relheight = 0.183, relwidth = 0.25)
        si = ttk.Button(self.messagebox, text = "Si", style = "Cartel.TButton", command = lambda: [self.funcion(*self.argumentos), self.messagebox.destroy()])   
        si.place(relx = 0.65, rely = 0.7, relheight = 0.183, relwidth = 0.25)
           
        #Fijo la ventana de error hasta que la cierren.
        self.messagebox.grab_set()



