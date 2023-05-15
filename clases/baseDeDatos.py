import mysql.connector
class baseDeDatos():
    @staticmethod
    def abrir():
      conexion = mysql.connector.connect(host="localhost",
                                           user="root",
                                           passwd="",
                                           database="bd1")
      return conexion
