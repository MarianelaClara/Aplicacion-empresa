CREATE TABLE Proveedores  (
   Id INT NOT NULL AUTO_INCREMENT,
   IdFiscal VARCHAR(30) NOT NULL,
   NomFiscal VARCHAR(100) NOT NULL,
   NomComercial VARCHAR(100) NOT NULL,
   Domicilio VARCHAR(80),
   CodPostal VARCHAR(10),
   Pais VARCHAR(30),
   Provincia VARCHAR(30),
   Ciudad VARCHAR(30),
   CCC  VARCHAR(50),
   Banco VARCHAR(30),
   Telefono INT(30),
   Movil INT(30),
   PersContacto VARCHAR(30),
   EAplicacionMail VARCHAR(80),
   Observaciones VARCHAR(200),
   PRIMARY KEY(Id)
)
;