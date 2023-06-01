from abc import ABC, abstractmethod
from articulo import Articulo
from datetime import datetime
from baseDeDatos import baseDeDatos as bd
import mysql.connector


class MateriaPrima(Articulo):
    def __init__(self, nombre, descripcion, precioUnitario, stock, fechaVencimiento, stockMinimo, new=None):
        # stock minimo debe ser mayor que 0
        super().__init__(nombre, descripcion, precioUnitario, stock, fechaVencimiento, stockMinimo)
        # alta de la materia prima
        if (new is None):
            cone = bd.abrir()
            datos = (nombre, descripcion, precioUnitario, stock, fechaVencimiento, stockMinimo)
            nAtrib = 6
            nombreAtrib = "nombreMateriaPrima, descripcionMateriaPrima, precioUnitarioMateriaPrima, stockMateriaPrima, fechaVencimientoMateriaPrima, stockMinimoMateriaPrima"
            bd.alta(cone, datos, "materiasprimas", nombreAtrib, nAtrib)

    @staticmethod
    def obtenerId(nombre):
        # exId (tupla) en este caso seria el valor del nombre de la materia prima
        cone = bd.abrir()
        consultaId = bd.consulta(cone, nombre, ("nombreMateriaPrima", ), "materiasprimas", "idMateriaPrima")
        # cadena = str(consultaId)
        # numId = ''.join([c for c in cadena if c.isdigit()])
        # numId = int(numId)
        numId, = consultaId[0]
        numId = int(numId)
        return numId
        # return self.idUsuario

    @classmethod
    def obtenerMat(cls, nombre, tuplaV=None):
        cone = bd.abrir()
        tupla = bd.consulta(cone, (nombre, ), ("nombreMateriaPrima", ), "materiasprimas", "*")
        tupla = tupla[0]
        descripcion = tupla[2]
        precioU = tupla[3]
        stock = tupla[4]
        fechaV = tupla[5]
        stockM = tupla[6]
        if(tuplaV==True):
            return tupla
        else:
            return cls(nombre, descripcion, precioU, stock, fechaV, stockM, True)

#fechaV = datetime.strptime('5/25/25', '%m/%d/%y')
#materiaP = MateriaPrima("Harina", "en kg", 300, 60, fechaV, 10)

#materiaH = MateriaPrima.obtenerMat("Harina")
#print(f"{materiaH.nombre} - {materiaH.descripcion} - {materiaH.precioU}")
#print(f'ID {MateriaPrima.obtenerId(("Harina", ))}')

#admi = Administrador(41111111, 20411111119, "Miguel Dario Coronel", "Calle anchoa", "3704259037", "Dario07", "morimayi")
# cone = bd.abrir()
# ad = bd.consulta(cone, (41111111, ), ("DNI", ), "usuarios", "*")
# print(ad)
# ad = ad[0]

