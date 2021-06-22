from tkinter import *
from tkinter import ttk 

def estilo(root):
    style = ttk.Style(root)
    style.theme_use('clam')
    
    style.configure('TNotebook', background ='#DFD6D8', foreground = 'white')
    style.configure('TNotebook.Tab', background ='#6A6767', foreground = 'white')

    style.map('TNotebook.Tab', 
    background = [('selected', '#525050'), ('active','#6D6767')],
    foreground = [('selected', 'white'), ('active','white')])

    style.configure('TFrame', background = '#DFD6D8')

    style.configure('TLabel', foreground = '#3D3B3B', background = '#DFD6D8')

    style.configure('TEntry', foreground = 'black', background = '#DFD6D8', state = NORMAL)

    style.map('TCombobox', fieldbackground=[('readonly','#998E8E')])
    style.map('TCombobox', selectbackground=[('readonly', '#998E8E')])
    style.map('TCombobox', selectforeground=[('readonly', 'white')])
    style.map('TCombobox', foreground=[('readonly', 'white')])
 
    style.configure('TButton', background = '#998E8E', foreground = 'white')

    style.configure('W.TButton', background='#6D6767')
    style.map('W.TButton', background=[('active', '#807878')])

  

    