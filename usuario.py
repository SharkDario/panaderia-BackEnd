import mysql.connector
from abc import ABC, abstractmethod
# from baseDeDatos import abrir, consulta, modificarAtrib
from baseDeDatos import baseDeDatos as bd
from persona import Persona

# clase abstracta


class Usuario(Persona, ABC):
    def __init__(self, user, clave, idTipoUsuario, DNI, nombre, CUIL_CUIT, domicilio, telefono):
        super().__init__(DNI, nombre, CUIL_CUIT, domicilio, telefono)
        self.user = user
        self.clave = clave
        self.idTipoUsuario = idTipoUsuario

    def modificarUser(self, valorA, elec):
        cone = bd.abrir()
        datos = (valorA, self.DNI)
        # elec puede ser "usuario" o "clave"
        bd.modificarAtrib(cone, datos, "usuarios", elec, "DNI")

    def obtenerUser(self, elec, dni):
        # elec puede ser "usuario" o "clave" o "idTipoUsuario"
        # dni debe ser tupla con el valor del dni (44444444, )
        cone = bd.abrir()
        return bd.consulta(cone, dni, ("DNI", ), "usuarios", elec)

    @staticmethod
    def recuperarNombresUser():
        cone = bd.abrir()
        consulta = bd.recuperarTodos(cone, "usuarios", "usuario")
        return consulta

    @staticmethod
    def recuperarDNIs():
        cone = bd.abrir()
        consulta = bd.recuperarTodos(cone, "usuarios", "DNI")
        return consulta

    @staticmethod
    def iniciarSesion(userIng, claveIng):
        cone = bd.abrir()
        # userIng y claveIng juntas son una tupla
        # si el usuario y clave no coinciden con alguno guardado en la BD, entonces devuelve una lista vacia
        return bd.consulta(cone, (userIng, claveIng), ("usuario", "clave"), "usuarios", "*")
