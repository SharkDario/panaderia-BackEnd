from abc import ABC, abstractmethod
# from baseDeDatos import abrir, consulta, modificarAtrib
from baseDeDatos import baseDeDatos as bd
import mysql.connector
# clase abstracta


class Articulo(ABC):

    def __init__(self, nombre, descripcion, precioUnitario, stock, stockMinimo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precioU = precioUnitario
        self.stock = stock
        self.stockM = stockMinimo

    @staticmethod
    def modificarArti(nombreT, idP, valorA, valorId, elec):
        datos = (valorA, valorId)
        # nombreT puede ser "productos", "materiasprimas"
        # idP puede ser "idProducto", "idMateriaPrima"
        # elec puede ser "nombre", "descripcion", "precioUnitario", "stock", "fechaVencimiento", "stockMinimo"
        cone = bd.abrir()
        bd.modificarAtrib(cone, datos, nombreT, elec, idP)

    @staticmethod
    def obtenerAtrib(idPMP, cadenaT, tabla, atrib):
        #idPMP es el valor del id
        #cadenaT puede ser (idProducto, ) o (idMateriaPrima)
        #tabla puede ser productos o materiasprimas
        #atrib puede ser stockProducto o stockMateriaPrima o cualquier atributo
        cone = bd.abrir()
        consulta = bd.consulta(cone, idPMP, cadenaT, tabla, atrib)
        return consulta

    @staticmethod
    def obtenerArti(nombreT, elec, nombre, cad):
        # nombreT puede ser "productos", "materiasprimas"
        # idP puede ser "idProducto", "idMateriaPrima"
        # elec puede ser "descripcion", "precioUnitario", "stock", "fechaVencimiento", "stockMinimo"
        # nombre debe ser tupla con el valor del nombre ("Harina", )
        cone = bd.abrir()
        return bd.consulta(cone, nombre, (f"nombre{cad}", ), nombreT, elec)

    @staticmethod
    @abstractmethod
    def recuperarNombres():
        pass

    @staticmethod
    @abstractmethod
    def obtenerId(exId):
        pass
