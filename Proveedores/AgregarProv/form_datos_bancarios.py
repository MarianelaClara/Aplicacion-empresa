from tkinter import *
from tkinter import ttk 

def validacionBanco(input):
    if input.isdigit():
        return True
    elif input == "":
        return True
    else:
        return False

def limitador(entry_text, nro):
    if len(entry_text.get()) > 0:
        #donde esta el :5 limitas la cantidad de caracteres
        entry_text.set(entry_text.get()[:nro])

def cuadro3(menu3):
    
    one = StringVar()
    two = StringVar()
    three = StringVar()
    four = StringVar()
    banco = StringVar()

    reg = menu3.register(validacionBanco)

    ttk.Label(menu3, text = "C.C.C:").place(relx = 0.02, rely = 0.2, relheight = 0.15)
    uno = ttk.Entry(menu3, textvariable = one)
    one.trace("w", lambda *args: limitador(one, 4))
    uno.place(relx = 0.14 , rely = 0.2, relwidth = 0.08, relheight = 0.15)
    uno.config(validate = "key", validatecommand = (reg, '%P'))

    dos = ttk.Entry(menu3, textvariable = two)
    two.trace("w", lambda *args: limitador(two, 3))
    dos.place(relx = 0.23 , rely = 0.2, relwidth = 0.08, relheight = 0.15)
    dos.config(validate = "key", validatecommand = (reg, '%P'))

    tres = ttk.Entry(menu3, textvariable = three)
    three.trace("w", lambda *args: limitador(three, 1))
    tres.place(relx = 0.32 , rely = 0.2, relwidth = 0.05, relheight = 0.15)
    tres.config(validate = "key", validatecommand = (reg, '%P'))

    cuatro = ttk.Entry(menu3, textvariable = four)
    four.trace("w", lambda *args: limitador(four, 4))
    cuatro.place(relx = 0.38 , rely = 0.2, relwidth = 0.2, relheight = 0.15)
    cuatro.config(validate = "key", validatecommand = (reg, '%P'))

    ttk.Button(menu3, text = "Otros datos").place(relx = 0.6, rely = 0.18, relwidth = 0.2, relheight = 0.2)

    ttk.Label(menu3, text = "Banco:").place(relx = 0.02, rely = 0.65, relheight = 0.15)
    banc = ttk.Entry(menu3, textvariable = banco)
    banc.place(relx = 0.15 , rely = 0.65, relwidth = 0.7, relheight = 0.15)

    datos = {"guardar": [one, two, three, four, banco], "borrar": [uno, dos, tres, cuatro, banc]}

    return datos