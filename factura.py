#from abc import ABC, abstractmethod
from baseDeDatos import baseDeDatos as bd
from datetime import datetime
import mysql.connector

class Factura():
    def __init__(self, numeroFactura, fechaEmisionFactura, idTipoFactura, precioTotal, idMedioPago, idCliente, idUsuario, new=None):
        # alta de la factura
        if new is None:
            cone = bd.abrir()
            datos = (numeroFactura, fechaEmisionFactura, idTipoFactura, precioTotal, idMedioPago, idCliente, idUsuario)
            nAtrib = 7  # cantidad de campos o atributos
            nombreAtrib = "numeroFactura, fechaEmisionFactura, idTipoFactura, precioTotal, idMedioPago, idCliente, idUsuario"
            bd.alta(cone, datos, "factura", nombreAtrib, nAtrib)

    @staticmethod
    def obtenerId(exId):
        # exId (tupla) en este caso seria el valor del DNI
        cone = bd.abrir()
        consultaId = bd.consulta(cone, exId, ("numeroFactura", "idTipoFactura"), "factura", "idFactura")
        # cadena = str(consultaId)
        # numId = ''.join([c for c in cadena if c.isdigit()])
        # numId = int(numId)
        numId = consultaId[0][0]
        numId = int(numId)  # Extraer el primer elemento de la primera tupla en el resultado
        return numId
        # return self.idFactura

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
        return cls(idFactura, numeroFactura, fechaEmisionFactura, idTipoFactura, precioTotal, idMedioPago, idCliente, idUsuario, True)

    def detalleFactura(self, cantidad, precioUnitario, idFactura, idProducto):
        cone = bd.abrir()
        datos = (cantidad, precioUnitario, idFactura, idProducto)
        nombreA = "cantidad, precioUnitario, idFactura, idProducto"
        bd.alta(cone, datos, "detallefactura", nombreA, 4)

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
'''



# hacer remito