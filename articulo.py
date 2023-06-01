from abc import ABC, abstractmethod
# from baseDeDatos import abrir, consulta, modificarAtrib
from baseDeDatos import baseDeDatos as bd
import mysql.connector
# clase abstracta


class Articulo(ABC):

    def __init__(self, nombre, descripcion, precioUnitario, stock, fechaVencimiento, stockMinimo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precioU = precioUnitario
        self.stock = stock
        self.fechaV = fechaVencimiento
        self.stockM = stockMinimo

    def modificarArti(self, nombreT, idP, valorA, valorId, elec):
        datos = (valorA, valorId)
        # nombreT puede ser "productos", "materiasprimas"
        # idP puede ser "idProducto", "idMateriaPrima"
        # elec puede ser "nombre", "descripcion", "precioUnitario", "stock", "fechaVencimiento", "stockMinimo"
        cone = bd.abrir()
        bd.modificarAtrib(cone, datos, nombreT, elec, idP)

    def obtenerArti(self, nombreT, elec, nombre):
        # nombreT puede ser "productos", "materiasprimas"
        # idP puede ser "idProducto", "idMateriaPrima"
        # elec puede ser "descripcion", "precioUnitario", "stock", "fechaVencimiento", "stockMinimo"
        # nombre debe ser tupla con el valor del nombre ("Harina", )
        cone = bd.abrir()
        return bd.consulta(cone, nombre, ("nombre", ), nombreT, elec)

    @staticmethod
    @abstractmethod
    def obtenerId(exId):
        pass
