from tkinter import *
from tkinter import ttk 
from Proveedores.Ver_Proveedores.ver_proveedor import *
from excepciones import *
from Proveedores.bd_proveedores import *
from tkinter import messagebox

def controlar_campos_obligatorios(campo1, campo2, campo3):
    if(campo1 == '' or campo2 == '' or campo3 == ''):
        raise CampoObligatorio()

def controlar_proveedor_existente(id):
    proveedor = Proveedores()
    dato = proveedor.buscar_proveedor(id)
    if(dato):
        raise ProveedorYaExistente()

def controlar_id_fiscal(lista_desplegable, id_fiscal):
    if(lista_desplegable == 'D.N.I'):
        if(len(id_fiscal) != 10 or id_fiscal[2] != '.' or id_fiscal[6] != '.' or 
            (not(id_fiscal[0:1] + id_fiscal[3:5] + id_fiscal[7:9]).isnumeric())):
            raise ErrorDeSintaxis()

    if(lista_desplegable == 'C.U.I.T'):
        if(len(id_fiscal) != 13 or id_fiscal[2] != '-' or id_fiscal[11] != '-' or 
            (not(id_fiscal[0:1] + id_fiscal[3:10] + id_fiscal[12]).isnumeric())):
            raise ErrorDeSintaxis()

def controlar_campo_numerico(campo):
    if(not(campo == '')):
        if(not(campo.isnumeric())):
            raise TipoDeDatoNoValido()

def controlar_Email(email):
    if(email):
        if(email.find("@") == -1):
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

class Mostrar_treeview(Ver_proveedor):

    def __init__(self, frame):
        Ver_proveedor.__init__(self, frame)

    def controlar(self, l1, l2, l3, l4, l5):
        lista_desplegable = l1[0].get()
        id_fiscal = l1[1].get()
        nombre_fiscal = l1[2].get()
        nombre_comercial = l1[3].get()
        
        try:
            controlar_campos_obligatorios(id_fiscal, nombre_fiscal, nombre_comercial)
            controlar_proveedor_existente(id_fiscal)
            controlar_id_fiscal(lista_desplegable, id_fiscal)
            controlar_campo_numerico(l4[0].get(), l4[1].get())
            controlar_email(l4[3].get())
            lista_actualizada = poner_NULL(l2 + l3 + l4 + l5)

            proveedor.insertar_proveedor(id_fiscal, nombre_fiscal, nombre_comercial, lista_actualizada[0], 
            lista_actualizada[1], lista_actualizada[2], lista_actualizada[3], lista_actualizada[4], lista_actualizada[5], 
            lista_actualizada[6], lista_actualizada[7], lista_actualizada[8], lista_actualizada[9],
            lista_actualizada[10], lista_actualizada[11])

            self.llenar_datos()

        except TipoDeDatoNoValido:
            messagebox.showerror(message="Sintaxis incorrecta, use números.", title="Error")
        except ErrorDeSintaxis:
            messagebox.showerror(message="Error de sintaxis.", title="Error")
        except ProveedorYaExistente:
            messagebox.showerror(message="El proveedor ya existe.", title="Error")
        except CampoObligatorio:
            messagebox.showerror(message="Falta llenar un campo obligatorio.", title="Error")

    