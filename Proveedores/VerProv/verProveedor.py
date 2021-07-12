from tkinter import *
from tkinter import ttk 
from Proveedores.BDProveedores import *

def verProv(frame):
    global tv
    tv = ttk.Treeview(frame, columns = ("col1", "col2", "col3", "col4", "col5"))

    tv.column("#0", width = 7, anchor = CENTER)
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

    proveedor = Proveedores()
    datos = proveedor.consultar_proveedores()
    for row in datos:
        tv.insert("", END, text = row[0], values = (row[1], row[2], row[3], row[4], row[5], row[6], row[7],
        row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]))