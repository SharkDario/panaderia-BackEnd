#from abc import ABC, abstractmethod
from baseDeDatos import baseDeDatos as bd
from datetime import datetime
import mysql.connector

class Factura():
    def __init__(self, numeroFactura, fechaEmisionFactura, idTipoFactura, precioTotal, idMedioPago, idCliente, idUsuario, new=None):
        self.numeroFactura = numeroFactura
        self.fechaEmisionFactura = fechaEmisionFactura
        self.idTipoFactura = idTipoFactura
        self.precioTotal = precioTotal
        self.idMedioPago = idMedioPago
        self.idCliente = idCliente
        self.idUsuario = idUsuario
        # alta de la factura
        if new is None:
            cone = bd.abrir()
            datos = (numeroFactura, fechaEmisionFactura, idTipoFactura, precioTotal, idMedioPago, idCliente, idUsuario)
            nAtrib = 7  # cantidad de campos o atributos
            nombreAtrib = "numeroFactura, fechaEmisionFactura, idTipoFactura, precioTotal, idMedioPago, idCliente, idUsuario"
            bd.alta(cone, datos, "factura", nombreAtrib, nAtrib)

    @staticmethod
    def obtenerId(exId):
        # exId (tupla) en este caso seria el valor del numero de factura y el idTipoFactura
        cone = bd.abrir()
        consultaId = bd.consulta(cone, exId, ("numeroFactura", "idTipoFactura"), "factura", "idFactura")
        # cadena = str(consultaId)
        # numId = ''.join([c for c in cadena if c.isdigit()])
        # numId = int(numId)
        try:
            numId, = consultaId[0] #tupla
            numId = int(numId) 
        except IndexError:
            numId = -1
        return numId
        # return self.idFactura

    @staticmethod
    def recuperarNumeros(idTipo):
        cone = bd.abrir()
        #print(idTipo)
        consulta = bd.recuperarTodosEspecifico(cone, "factura", "numeroFactura", "idTipoFactura", (idTipo, ))
        #print(consulta)
        return consulta

    @staticmethod
    def recuperarFechaEspecifica(fechaIni, fechaFin):
        cone = bd.abrir()
        cursor = cone.cursor()
        datos = (fechaIni, fechaFin)
        sql = f"select * from factura where fechaEmisionFactura>=%s and fechaEmisionFactura<=%s"
        cursor.execute(sql, datos)
        consulta = cursor.fetchall()
        cone.close()
        return consulta

    def actualizarTotal(self, precioT, idF):
        cone = bd.abrir()
        bd.modificarAtrib(cone, (precioT, idF), "factura", "precioTotal", "idFactura")

    @classmethod
    def obtenerFactura(cls, numeroFactura, idTipoFactura):
        cone = bd.abrir()
        tupla = bd.consulta(cone, (numeroFactura, idTipoFactura), ("numeroFactura","idTipoFactura"), "factura", "*")
        tupla = tupla[0]
        idFactura = tupla[0]
        numeroFactura = tupla[1]
        fechaEmisionFactura = tupla[2]
        idTipoFactura = tupla[3]
        precioTotal = tupla[4]
        idMedioPago = tupla [5]
        idCliente = tupla[6]
        idUsuario = tupla[7]
        return cls(numeroFactura, fechaEmisionFactura, idTipoFactura, precioTotal, idMedioPago, idCliente, idUsuario, True)

    def detalleFactura(self, cantidad, precioUnitario, idFactura, idProducto):
        cone = bd.abrir()
        datos = (cantidad, precioUnitario, idFactura, idProducto)
        nombreA = "cantidad, precioUnitario, idFactura, idProducto"
        bd.alta(cone, datos, "detallefactura", nombreA, 4)

    @staticmethod
    def obtenerDetalle(idF):
        cone = bd.abrir()
        consultaD = bd.consulta(cone, (idF, ), ("idFactura", ), "detallefactura", "*")
        return consultaD

"""
fecha = datetime.strptime("2023-05-02", '%Y-%m-%d') 
factura = Factura(12345, fecha, 1, 1200, 1, 2, 4)
detallefactura = factura.detalleFactura(10, 200, 9, 1)  # Llamar al método detalleRemito

cone = bd.abrir()

if cone:
    print("La inserción se realizó correctamente.")
else:
    print("La inserción falló.")
'''
#numeroFactura, fechaEmisionFactura, idTipoFactura, precioTotal, idMedioPago, idCliente, idUsuario, new=None
fecha = datetime.strptime("2023-05-02", '%Y-%m-%d') 
factura = Factura(12345, fecha, 1, 1200, 1, 2, 4)
cone = bd.abrir()
ad = bd.consulta(cone, (12345, 1), ("numeroFactura", "idTipoFactura"), "factura", "*")
if ad:
    ad = ad[0]
    print(ad)
else:
    print("La factura no existe")


tuplaFactura = (12345, 1)
tuplaFactura = tuple(map(int, tuplaFactura))  # Convertir los valores a tipo int
idFactura = Factura.obtenerId(tuplaFactura)



print(f"ID de la factura: {idFactura}")
"""



# hacer remito