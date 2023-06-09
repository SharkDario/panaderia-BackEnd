from abc import ABC, abstractmethod
from persona import Persona
from baseDeDatos import baseDeDatos as bd
import mysql.connector

class Proveedor(Persona):
    def __init__(self, nombreProveedor, CUIL_CUIT, DNI, domicilioProveedor, telefonoProveedor, new=None):
        super().__init__(nombreProveedor, CUIL_CUIT, DNI, domicilioProveedor, telefonoProveedor)
        #self.idProveedor = idProveedor
        # alta del proveedor
        if (new is None):
            cone = bd.abrir()
            datos = (nombreProveedor, CUIL_CUIT, DNI, domicilioProveedor, telefonoProveedor)
            nAtrib = 5        #cantidad de campos o atributos
            nombreAtrib = "nombreProveedor, CUIL_CUIT, DNI, domicilioProveedor, telefonoProveedor"
            bd.alta(cone, datos, "proveedores", nombreAtrib, nAtrib)

    @staticmethod
    def bajaProveedor(idProv):
        cone = bd.abrir()
        bd.baja(cone, (idProv, ), ("idProveedor", ), "proveedores")

    @staticmethod
    def obtenerId(exId):
        # exId (tupla) en este caso seria el valor del DNI
        cone = bd.abrir()
        consultaId = bd.consulta(cone, exId, ("DNI", ), "proveedores", "idProveedor")
        # cadena = str(consultaId)
        # numId = ''.join([c for c in cadena if c.isdigit()])
        # numId = int(numId)
        try:
            numId, = consultaId[0]
            numId = int(numId)
        except IndexError:
            numId = -1
        return numId
        # return self.idProveedor

    @staticmethod
    def recuperarNombres():
        cone = bd.abrir()
        consulta = bd.recuperarTodos(cone, "proveedores", "nombreProveedor")
        return consulta

    @staticmethod
    def recuperarDNIs():
        cone = bd.abrir()
        consulta = bd.recuperarTodos(cone, "proveedores", "DNI")
        return consulta

    @classmethod
    def obtenerProveedor(cls, DNI):
        cone = bd.abrir()
        tupla = bd.consulta(cone, (DNI, ), ("DNI", ), "proveedores", "*")
        tupla = tupla[0]
        idProveedor = tupla[0]
        nombreProveedor = tupla[1]
        CUIL_CUIT = tupla[2]
        DNI = tupla[3]
        domicilioProveedor = tupla[5]
        telefonoProveedor = tupla [4]
        return cls(nombreProveedor, CUIL_CUIT, DNI, domicilioProveedor, telefonoProveedor, True)

# proveedor = Proveedor("Brenda", "27458963125", 45896312, "republica", "3704546716")
# cone = bd.abrir()
# ad = bd.consulta(cone, (45896312, ), ("DNI", ), "proveedores", "*")
# print(ad)
# ad = ad[0]


# tuplaDNI = 45896312
# tuplaDNI = (tuplaDNI, )
# idProveedor = Proveedor.obtenerId(tuplaDNI)


#print(f"ID del proveedor: {idProveedor}")


# hacer remito
