from abc import ABC, abstractmethod
from persona import Persona
from baseDeDatos import baseDeDatos as bd
import mysql.connector

class Cliente(Persona):
    def __init__(self, nombreCliente, CUIL_CUIT,	DNI, telefonoCliente, domicilioCliente, new=None):
        super().__init__(nombreCliente, CUIL_CUIT, DNI, telefonoCliente, domicilioCliente)
        #self.idCliente = idCliente
        # alta del cliente
        if (new is None):
            cone = bd.abrir()
            datos = (nombreCliente, CUIL_CUIT,	DNI, telefonoCliente, domicilioCliente)
            nAtrib = 5        #cantidad de campos o atributos
            nombreAtrib = "nombreCliente, CUIL_CUIT, DNI, telefonoCliente, domicilioCliente"
            bd.alta(cone, datos, "clientes", nombreAtrib, nAtrib)

    @staticmethod
    def obtenerId(exId):
        # exId (tupla) en este caso seria el valor del DNI
        cone = bd.abrir()
        consultaId = bd.consulta(cone, exId, ("DNI", ), "clientes", "idCliente")
        # cadena = str(consultaId)
        # numId = ''.join([c for c in cadena if c.isdigit()])
        # numId = int(numId)
        numId, = consultaId[0]
        numId = int(numId)
        return numId
        # return self.idCliente

    @classmethod
    def obtenerProveedor(cls, DNI):
        cone = bd.abrir()
        tupla = bd.consulta(cone, (DNI, ), ("DNI", ), "clientes", "*")
        tupla = tupla[0]
        idCliente = tupla[0]
        nombreCliente = tupla[1]
        CUIL_CUIT = tupla[2]
        DNI = tupla[3]
        telefonoCliente = tupla[4]
        domicilioCliente = tupla [5]
        return cls(idCliente, nombreCliente, CUIL_CUIT, DNI, telefonoCliente, domicilioCliente, True)

cliente = Cliente("Brenda", "27458963125", 45896312, "3704546716", "republica")
cone = bd.abrir()
ad = bd.consulta(cone, (45896312, ), ("DNI", ), "clientes", "*")
print(ad)
ad = ad[0]


tuplaDNI = 45896312
tuplaDNI = (tuplaDNI, )
idCliente = Cliente.obtenerId(tuplaDNI)


print(f"ID del cliente: {idCliente}")


# hacer remito
