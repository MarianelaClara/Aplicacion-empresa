from tkinter import *
from tkinter import ttk 
from Proveedores.bd_proveedores import *
from Proveedores.Ver_Proveedores.cartel import *
from Proveedores.Ver_Proveedores.cartel_confirmacion import *         
class Modificar_treeview():

    proveedor = Proveedores()

    def __init__(self, frame):
        self.frame = frame
        self.create_widgets()
        self.llenar_datos()

    def create_widgets(self):  
        frame_treeview = ttk.Frame(self.frame)
        frame_treeview.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.8)
        
        self.tv = ttk.Treeview(frame_treeview, columns = ("col1", "col2", "col3", "col4", "col5"))
        
        self.tv.column("#0", width = 7, anchor = CENTER)
        self.tv.column("col1", width = 80, anchor = CENTER)
        self.tv.column("col2", width = 80, anchor = CENTER)
        self.tv.column("col3", width = 80, anchor = CENTER)
        self.tv.column("col4", width = 80, anchor = CENTER)
        self.tv.column("col5", width = 80, anchor = CENTER)
        
        self.tv.heading("#0", text = "Código", anchor = CENTER)
        self.tv.heading("col1", text = "Nombre fiscal", anchor = CENTER)
        self.tv.heading("col2", text = "Nombre comercial", anchor = CENTER)
        self.tv.heading("col3", text = "Móvil", anchor = CENTER)
        self.tv.heading("col4", text = "E-mail", anchor = CENTER)
        self.tv.heading("col5", text = "D.N.I./C.U.I.T.", anchor = CENTER)
        
        self.tv.place(relwidth = 0.98, relheight = 1)

        #Scrollbar
        barra = ttk.Scrollbar(frame_treeview, orient = VERTICAL)
        barra.place(relx = 0.98, relwidth = 0.02, relheight = 1)
        self.tv.config(yscrollcommand = barra.set)
        barra.config(command = self.tv.yview)

        #Boton para borrar un proveedor
        boton_borrar = ttk.Button(self.frame, text = "Borrar", command = self.borrar_proveedor)
        boton_borrar.place(relx = 0.05, rely = 0.89, relheight = 0.08)

    def llenar_datos(self): #Se cargan en el Treeview los datos de proveedores anteriormente guardados.
        datos = self.proveedor.consultar_proveedores()
        for row in datos:
            self.tv.insert("", END, text = row[0], values = (row[2], row[3], row[12], row[14], row[1]))
    
    def mostrar_proveedor(self):
        for item in self.tv.get_children():
            self.tv.delete(item)
        self.llenar_datos()

    def borrar_proveedor(self):
        seleccionado = self.tv.focus()
        cartel = Messageboxs(self.frame)
        clave = self.tv.item(seleccionado, 'text')

        if(clave == ''):
            cartel.crear_cartel("Debes seleccionar un proveedor primero.", "Eliminar", "warning")
        else:
            valores = self.tv.item(seleccionado, 'values')
            mensaje = "Deseas eliminar el proveedor seleccionado?\n Con nombre comercial:\n" + valores[1]  
            cartel_confirmacion = Cartel_confirmacion(self.frame, mensaje, "Pregunta", [clave], self.proveedor.eliminar_proveedor)
            cartel_confirmacion.crear_cartel()

        
