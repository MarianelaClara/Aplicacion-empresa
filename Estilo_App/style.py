from tkinter import *
from tkinter import ttk 

def estilo(root):

    #Estilo aplicacion.
    style = ttk.Style(root)
    style.theme_use('clam')
    root.configure(background = '#43444D')

    style.configure('TNotebook', background ='#43444D', foreground = 'white')
    style.configure('TNotebook.Tab', background ='#43444D', foreground = 'white')

    style.map('TNotebook.Tab', 
    background = [('selected', '#43444D'), ('active','#43444D')],
    foreground = [('selected', 'white'), ('active','white')])

    style.configure('TFrame', background = '#43444D')

    style.configure('TLabel', background = '#4B4C56', foreground = '#D9D9DB')

    style.configure('TEntry', fieldbackground = '#C5C5CD', selectforeground = 'black', selectbackground = '#6868B5')

    style.map('TCombobox', fieldbackground=[('readonly','#6D6767')])
    style.map('TCombobox', selectbackground=[('readonly', '#6D6767')])
    style.map('TCombobox', selectforeground=[('readonly', 'white')])
    style.map('TCombobox', foreground=[('readonly', 'white')])
 
    style.configure('TButton', background = '#6D6767', foreground = 'white', anchor = 'center')
    style.map('TButton', background=[('active', '#807878')])

    #Estilo para errores.
    style.configure('Error.TEntry',  foreground = 'black', fieldbackground = '#D67460')

    #Estilo para el cartel de eliminar un proveedor.
    style.configure('Cartel.TButton', background = '#C3C5C9', foreground = 'black')
    style.map('Cartel.TButton',background=[('active', '#CCCED1')])