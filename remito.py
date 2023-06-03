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
        # exId (tupla) en este caso seria el valor del número de remito
        cone = bd.abrir()
        consultaId = bd.consulta(cone, exId, ("numeroRemito", ), "remitoproveedor", "idRemito")
        # cadena = str(consultaId)
        # numId = ''.join([c for c in cadena if c.isdigit()])
        # numId = int(numId)
        try:
            numId, = consultaId[0] # Obtener el primer elemento del resultado
            numId = int(numId)
        except IndexError:
            numId = -1
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
    
    def detalleRemito(self, cantidad, fechaEntregaProducto, idRemito, idMateriaPrima, idTipoEstadoMateriaPrima):
        cone = bd.abrir()
        datos = (cantidad, fechaEntregaProducto, idRemito, idMateriaPrima, idTipoEstadoMateriaPrima)
        nombreA = "cantidad, fechaEntregaProducto, idRemito, idMateriaPrima, idTipoEstadoMateriaPrima"
        bd.alta(cone, datos, "detalleremitoproveedor", nombreA, 5)

#fecha = datetime.strptime("2023-05-02", '%Y-%m-%d')
#remito = Remito(1, fecha, 1)  # Crear instancia de Remito
#detalleremito = remito.detalleRemito(10, fecha, 1, 1, 1)  # Llamar al método detalleRemito

#cone = bd.abrir()

#if cone:
#    print("La inserción se realizó correctamente.")
#else:
#    print("La inserción falló.")
