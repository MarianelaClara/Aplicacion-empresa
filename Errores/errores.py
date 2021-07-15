from tkinter import *
from tkinter import ttk 

class Error():
    def __init__(self):
        pass
    
    def mostrar(self, lista_entries, tipo_de_error):

        if (tipo_de_error == 'CampoObligatorio'):
            for entry in lista_entries:
                entry.insert(END, 'Campo obligatorio')
                entry.configure(style = 'Error.TEntry')
        else:
            lista_entries[0].delete(0, 'end')
            lista_entries[0].configure(style = 'Error.TEntry')

            if (tipo_de_error == 'ProveedorYaExistente'): 
                lista_entries[0].insert(END, 'El proveedor ya existe')    
            elif (tipo_de_error == 'ErrorDeSintaxis'):
                lista_entries[0].insert(END, 'Error de escritura')          
            else:
                lista_entries[0].insert(END, 'Tipos de datos incorrectos')

    
