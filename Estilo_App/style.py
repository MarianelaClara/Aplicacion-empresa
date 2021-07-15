from tkinter import *
from tkinter import ttk 

def estilo(root):
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
 
    style.configure('TButton', background = '#6D6767', foreground = 'white')
    style.map('TButton', background=[('active', '#807878')])

    style.configure('TMessagebox', foreground = "red")
