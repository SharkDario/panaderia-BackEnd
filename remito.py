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
    
    def detalleRemito(self, cantidad, fechaEntregaProducto, idRemito, idMateriaPrima, idTipoEstadoMateriaPrima):
        cone = bd.abrir()
        datos = (cantidad, fechaEntregaProducto, idRemito, idMateriaPrima, idTipoEstadoMateriaPrima)
        nombreA = "cantidad, fechaEntregaProducto, idRemito, idMateriaPrima, idTipoEstadoMateriaPrima"
        bd.alta(cone, datos, "detalleremitoproveedor", nombreA, 5)
        # ...

        # Actualizar el stock de materia prima
        stockActual = bd.consulta(cone, (idMateriaPrima, ), ("idMateriaPrima", ), "materiasprimas", "stockMateriaPrima")
        stockActual = stockActual[0][0]  # Obtener el stock actual

        nuevoStock = stockActual + cantidad

        stockDatos = (nuevoStock, idMateriaPrima)
        stockAtributos = "stockMateriaPrima = %s"
        bd.actualizar(cone, stockDatos, stockAtributos, "materiasprimas", "idMateriaPrima")
        
# Consultar el stock de materia prima después de la actualización
cone = bd.abrir()
stockDespues = bd.consulta(cone, (1,), ("idMateriaPrima",), "materiasprimas", "stockMateriaPrima")
stockDespues = stockDespues[0][0]  # Obtener el nuevo stock actualizado
stockActual = bd.consulta(cone, (idMateriaPrima, ), ("idMateriaPrima", ), "materiasprimas", "stockMateriaPrima")
     

# Imprimir el stock antes y después de la actualización
print("Stock antes de la actualización:", stockActual)
print("Stock después de la actualización:", stockDespues)

bd.cerrar(cone)

# ...


#if cone:
    #print("La inserción se realizó correctamente.")
#else:
    #print("La inserción falló.")
