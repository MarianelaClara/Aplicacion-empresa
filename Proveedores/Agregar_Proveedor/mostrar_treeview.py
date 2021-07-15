from tkinter import *
from tkinter import ttk 
from Proveedores.Ver_Proveedores.ver_proveedor import *
from Errores.excepciones import *
from Errores.errores import *
from Proveedores.bd_proveedores import *

lista_entries = []

def controlar_campos_obligatorios(campo1, campo2, campo3):
    global lista_entries

    if(campo1.get() == '' or campo2.get() == '' or campo3.get() == ''):

        if (campo1.get() == ''):
            lista_entries = lista_entries + [campo1]
        if (campo2.get() == ''):
            lista_entries = lista_entries + [campo2]
        if(campo3.get() == ''):
            lista_entries = lista_entries + [campo3]

        raise CampoObligatorio()

def controlar_proveedor_existente(campo_id, proveedor):
    global lista_entries
    dato = proveedor.buscar_proveedor(campo_id.get())
    if(dato):
        lista_entries = [campo_id]
        raise ProveedorYaExistente()

def controlar_id_fiscal(lista_desplegable, campo_id_fiscal):
    global lista_entries
    id_fiscal = campo_id_fiscal.get()
    if(lista_desplegable == 'D.N.I'):
        if(len(id_fiscal) != 10 or id_fiscal[2] != '.' or id_fiscal[6] != '.' or 
            (not(id_fiscal[0:1] + id_fiscal[3:5] + id_fiscal[7:9]).isnumeric())):
            lista_entries = [campo_id_fiscal]
            raise ErrorDeSintaxis()

    if(lista_desplegable == 'C.U.I.T'):
        if(len(id_fiscal) != 13 or id_fiscal[2] != '-' or id_fiscal[11] != '-' or 
            (not(id_fiscal[0:1] + id_fiscal[3:10] + id_fiscal[12]).isnumeric())):
            lista_entries = [campo_id_fiscal]
            raise ErrorDeSintaxis()

def controlar_campo_numerico(campo_numerico):
    global lista_entries
    posibles_numeros = campo_numerico.get()
    if(not(posibles_numeros == '')):
        if(not((posibles_numeros.strip()).isnumeric())):
            lista_entries = [campo_numerico]
            raise TipoDeDatoNoValido()

def controlar_email(campo_email):
    global lista_entries
    email = campo_email.get()
    if(email):
        if(email.find("@") == -1):
            lista_entries = [campo_email]
            raise ErrorDeSintaxis()

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

def reponer_estilos(lista):
    for entry in lista_entries:
        entry.configure(style = 'TEntry')

class Posible_proveedor(Mostrar_proveedores):
   
    def __init__(self, frame0):
        Mostrar_proveedores.__init__(self, frame0)
        self.error = Error()

    def controlar(self, f1, f2, f3, f4, f5):
        global lista_entries
        reponer_estilos(lista_entries)
        lista_entries = []
        try:
            controlar_campos_obligatorios(f1[1], f1[2], f1[3])
            controlar_proveedor_existente(f1[1], self.proveedor)
            controlar_id_fiscal(f1[0].get(), f1[1])
            controlar_campo_numerico(f4[1])
            controlar_campo_numerico(f4[0])
            controlar_email(f4[3])
            lista_actualizada = poner_NULL(f2 + f3 + f4 + f5)

            self.proveedor.insertar_proveedor(f1[1].get(), f1[2].get(), f1[3].get(), lista_actualizada[0], 
            lista_actualizada[1], lista_actualizada[2], lista_actualizada[3], lista_actualizada[4], lista_actualizada[5], 
            lista_actualizada[6], lista_actualizada[7], lista_actualizada[8], lista_actualizada[9],
            lista_actualizada[10], lista_actualizada[11])

            self.mostrar_proveedor()

        except TipoDeDatoNoValido:
            self.error.mostrar(lista_entries, 'TipoDeDatoNoValido')
        except ErrorDeSintaxis:
            self.error.mostrar(lista_entries, 'ErrorDeSintaxis')
        except ProveedorYaExistente:
            self.error.mostrar(lista_entries, 'ProveedorYaExistente')
        except CampoObligatorio:
            self.error.mostrar(lista_entries, 'CampoObligatorio')

    
