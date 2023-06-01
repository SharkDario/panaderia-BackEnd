from abc import ABC, abstractmethod
# from baseDeDatos import abrir, consulta, modificarAtrib
from baseDeDatos import baseDeDatos as bd
import mysql.connector
# clase abstracta


class Persona(ABC):

    def __init__(self, DNI, nombre, CUIL_CUIT, domicilio, telefono):
        self.DNI = DNI
        self.nombre = nombre
        self.CUIL_CUIT = CUIL_CUIT
        self.domicilio = domicilio
        self.telefono = telefono

    def modificarPerso(self, nombreT, valorA, elec):
        datos = (valorA, self.DNI)
        # nombreT puede ser "usuarios", "clientes", "proveedores"
        # idP puede ser "idUsuario", "idCliente", "idProveedor"
        # elec puede ser "nombre" o "domicilio" o "telefono"
        cone = bd.abrir()
        bd.modificarAtrib(cone, datos, nombreT, elec, "DNI")

    def obtenerPerso(self, nombreT, elec, dni):
        # elec puede ser "DNI", "nombre", "CUIL_CUIT", "domicilio", o "telefono"
        # dni debe ser tupla con el valor del dni (44444444, )
        cone = bd.abrir()
        return bd.consulta(cone, dni, ("DNI", ), nombreT, elec)

    @staticmethod
    @abstractmethod
    def obtenerId(exId):
        pass
