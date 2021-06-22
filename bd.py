import pymysql

connection = pymysql.connect(host="localhost",    # tu host, usualmente localhost
                     user="root",         # tu usuario
                     passwd="nena123+",  # tu password
                     db="aplicacion")        # el nombre de la base de datos

cursor = connection.cursor()


# Debes crear un objeto Cursor. Te permitirá
# ejecutar todos los queries que necesitas
