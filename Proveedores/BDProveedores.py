import pymysql

class Proveedores:

    def __init__(self):
        self.cnn = pymysql.connect(host="localhost", user="root", 
        passwd="nena123+", database="Aplicacion")

    def __str__(self):
        datos=self.consulta_paises()
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
    

    def buscar_proveedor(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM Proveedores WHERE IdFiscal = '{}'".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def insertar_proveedor(self, IdFiscal, NomFiscal, NomComercial, Domicilio, CodPostal, Pais, 
        Provincia, Ciudad, CCC, Banco, Telefono, Movil, PersContacto, EMail, Observaciones):

        cur = self.cnn.cursor()

        sql='''INSERT INTO Proveedores (IdFiscal, NomFiscal, NomComercial, Domicilio, CodPostal, Pais, 
        Provincia, Ciudad, CCC, Banco, Telefono, Movil, PersContacto, EMail, Observaciones) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''' 

        cur.execute(sql,(IdFiscal, NomFiscal, NomComercial, Domicilio, CodPostal, Pais, 
        Provincia, Ciudad, CCC, Banco, Telefono, Movil, PersContacto, EMail, Observaciones))
        
        self.cnn.commit()    
        cur.close()  



