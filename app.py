from tkinter import *
from Notebook.ventana_principal import *
from Estilo_App.style import *

def porciento(x,y):
    return (x*y)//100

def main():
    root = Tk()

    root.wm_title("App")
    ancho = root.winfo_screenwidth()
    alto = root.winfo_screenheight()
    x = porciento(80,ancho)
    y = porciento(80,alto)

    #Centro la aplicacion.
    mover1 = (ancho - x)//2
    mover2 = (alto - y)//2
    root.geometry('%dx%d+%d+%d' % (x, y, mover1, mover2))

    root.wm_resizable(height = 0, width = 0)
    estilo(root)

    app = Ventana(x, y) 

    root.mainloop()

if __name__ == "__main__":
    main()