from tkinter import *
from tkinter import ttk 



def cuadro1(menu1):

    nomFis = StringVar()
    nomCom = StringVar()
    idFis = StringVar()

    ttk.Label(menu1, text = "Identificación fiscal:").place(relx = 0.02, rely = 0.07, relheight = 0.15)
    opciones = ["C.U.I.T", "D.N.I"]
    lista_desplegable = ttk.Combobox(menu1,state = 'readonly', justify='center')
    
    lista_desplegable['values'] = opciones
    lista_desplegable.current(0)
    lista_desplegable.place(relx = 0.35, rely = 0.07, relwidth = 0.2, relheight = 0.15)
    
    id_fiscal = ttk.Entry(menu1, textvariable = idFis)
    id_fiscal.place(relx = 0.6, rely = 0.07, relwidth = 0.3, relheight = 0.15)

    ttk.Label(menu1, text = "Nombre fiscal:").place(relx = 0.02, rely = 0.425, relheight = 0.15)
    nom_fiscal = ttk.Entry(menu1, textvariable = nomFis)
    nom_fiscal.place(relx = 0.26, rely = 0.425, relwidth = 0.3, relheight = 0.15)

    ttk.Label(menu1, text = "Nombre comercial:").place(relx = 0.02, rely = 0.78, relheight = 0.15)
    nom_comer = ttk.Entry(menu1, textvariable = nomCom)
    nom_comer.place(relx = 0.31, rely = 0.78, relwidth = 0.3, relheight = 0.15)
        
    datos = {"guardar": [lista_desplegable, idFis, nomFis, nomCom], "borrar": [id_fiscal, nom_fiscal, nom_comer]}

    return datos