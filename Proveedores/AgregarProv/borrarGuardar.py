from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from Proveedores.BDProveedores import *

def borrar(l1, l2, l3, l4, l5):
    l = l1 + l2 + l3 + l4 

    for x in l:
        if(x.get() != ""):
            x.delete(0, END)
    
    if(l5[0].get('1.0', END) != ""):
        l5[0].delete("1.0","end")

def error():
    messagebox.showerror(message="Error", title="Error")
    return 0

def controlar_IdFiscal(listaDesplegable, idFiscal):
    if(listaDesplegable == 'D.N.I'):
        if(not(len(idFiscal) == 10 and idFiscal[2] == '.' and idFiscal[6] == '.')):
            error()
            if(not((idFiscal[0:1] + idFiscal[3:5] + idFiscal[7:9]).isnumeric())):
                error()
    else:
        if(not(len(idFiscal) == 13 and idFiscal[2] == '-' and idFiscal[11] == '-')):
            error()
            if(not((idFiscal[0:1] + idFiscal[3:10] + idFiscal[12]).isnumeric())):
                error()
    return 1

def controlar_Tel_Movil(telefono, movil):

    if(telefono == '' and movil == ''):
        return 1
    else:
        if(telefono.isnumeric() or movil.isnumeric()):
            return 1

    error()
    
def controlar_Email(email):
    if(email):
        if(email.find("@") == -1):
            error()
    return 1


def poner_NULL(lista):
    l = []
    largo = len(lista)
    for x in range(0, largo):
        if x != largo - 1:
            valor = lista[x].get()
            if(valor == ''):
                l = l + [None]
            else:
                l = l + [valor]
        else:
            valor = (lista[x].get("1.0", END))[0:len(valor) - 2]
            if(valor == ''):
                l = l + [None]
            else:
                l = l + [valor]

    return l

def guardar(l1, l2, l3, l4, l5):

    listaDesplegable = l1[0].get()
    idFiscal = l1[1].get()
    nomFiscal = l1[2].get()
    nomComer = l1[3].get()
    if(idFiscal and nomFiscal and nomComer): #Entrys obligatorios a llenar.
        proveedor = Proveedores()
        if(not(proveedor.buscar_proveedor(idFiscal))):
            if(controlar_IdFiscal(listaDesplegable, idFiscal)):
                if(controlar_Tel_Movil(l4[0].get(), l4[1].get())):
                    if(controlar_Email(l4[3].get())):
                        listaActualizada = poner_NULL(l2 + l3 + l4 + l5)
                        proveedor.insertar_proveedor(idFiscal, nomFiscal, nomComer, listaActualizada[0], listaActualizada[1], 
                        listaActualizada[2], listaActualizada[3], listaActualizada[4], listaActualizada[5], 
                        listaActualizada[6], listaActualizada[7], listaActualizada[8], listaActualizada[9],
                        listaActualizada[10], listaActualizada[11])
        else:
            error()                   
    else:
        error()