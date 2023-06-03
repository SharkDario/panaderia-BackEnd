#from abc import ABC, abstractmethod
from baseDeDatos import baseDeDatos as bd
from datetime import datetime
import mysql.connector

class Remito():
    def __init__(self, numeroRemito, fechaEmisionRemito, idProveedor, new=None):
        # alta del remito
        if new is None:
            cone = bd.abrir()
            datos = (numeroRemito, fechaEmisionRemito, idProveedor)
            nAtrib = 3  # cantidad de campos o atributos
            nombreAtrib = "numeroRemito, fechaEmisionRemito, idProveedor"
            bd.alta(cone, datos, "remitoproveedor", nombreAtrib, nAtrib)

    @staticmethod
    def obtenerId(exId):
        # exId (tupla) en este caso seria el valor del DNI
        cone = bd.abrir()
        consultaId = bd.consulta(cone, exId, ("numeroRemito", ), "remitoproveedor", "idRemito")
        # cadena = str(consultaId)
        # numId = ''.join([c for c in cadena if c.isdigit()])
        # numId = int(numId)
        numId = consultaId[0][0] # Obtener el primer elemento del resultado
        numId = int(numId)  
        return numId
        # return self.idRemito

    @classmethod
    def obtenerRemito(cls, numeroRemito):
        cone = bd.abrir()
        tupla = bd.consulta(cone, (numeroRemito, ), ("numeroRemito", ), "remitoproveedor", "*")
        tupla = tupla[0]
        idRemito = tupla[0]
        numeroRemito = tupla[1]
        fechaEmisionRemito = tupla[2]
        idProveedor = tupla[3]
        return cls(idRemito, numeroRemito, fechaEmisionRemito, idProveedor, True)
fecha = datetime.strptime("2023-05-02", '%Y-%m-%d') 
remito = Remito(2345, fecha, 1)
cone = bd.abrir()
ad = bd.consulta(cone, (2345, ), ("numeroRemito", ), "remitoproveedor", "*")
if ad:
    ad = ad[0]
    print(ad)
else:
    print("El remito no existe")


tuplaRemito= 2345
tuplaRemito = (tuplaRemito, )
idRemito = Remito.obtenerId(tuplaRemito)

print(f"ID del remito: {idRemito}")


# hacer remito
