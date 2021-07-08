from tkinter import *
from tkinter import ttk 

def verProv(frame):
    tv = ttk.Treeview(frame, columns = ("col1", "col2", "col3", "col4", "col5"))

    tv.column("#0", width = 7)
    tv.column("col1", width = 80, anchor = CENTER)
    tv.column("col2", width = 80, anchor = CENTER)
    tv.column("col3", width = 80, anchor = CENTER)
    tv.column("col4", width = 80, anchor = CENTER)
    tv.column("col5", width = 80, anchor = CENTER)
    
    tv.heading("#0", text = "Código", anchor = CENTER)
    tv.heading("col1", text = "Nombre fiscal", anchor = CENTER)
    tv.heading("col2", text = "Nombre comercial", anchor = CENTER)
    tv.heading("col3", text = "Móvil", anchor = CENTER)
    tv.heading("col4", text = "E-mail", anchor = CENTER)
    tv.heading("col5", text = "C.U.I.T.", anchor = CENTER)
    
    tv.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.9)