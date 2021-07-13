from tkinter import *
from menu import *
from style import *

def porciento(x,y):
    return (x*y)//100

def main():
    root = Tk()

    root.wm_title("App")
    ancho = root.winfo_screenwidth()
    alto = root.winfo_screenheight()
    x = porciento(80,ancho)
    y = porciento(80,alto)
    root.wm_geometry(str(x) + "x" + str(y))
    root.wm_resizable(height = 0, width = 0)
    estilo(root)

    app = Ventana(x, y) 

    root.mainloop()

if __name__ == "__main__":
    main()