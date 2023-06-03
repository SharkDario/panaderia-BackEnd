from abc import ABC, abstractmethod
from articulo import Articulo
from datetime import datetime
from baseDeDatos import baseDeDatos as bd
import mysql.connector


class MateriaPrima(Articulo):
    def __init__(self, nombre, descripcion, precioUnitario, stock, stockMinimo, new=None):
        # stock minimo debe ser mayor que 0
        super().__init__(nombre, descripcion, precioUnitario, stock, stockMinimo)
        # alta de la materia prima
        if (new is None):
            cone = bd.abrir()
            datos = (nombre, descripcion, precioUnitario, stock, stockMinimo)
            nAtrib = 5
            nombreAtrib = "nombreMateriaPrima, descripcionMateriaPrima, precioUnitarioMateriaPrima, stockMateriaPrima, stockMinimoMateriaPrima"
            bd.alta(cone, datos, "materiasprimas", nombreAtrib, nAtrib)

    @staticmethod
    def obtenerId(nombre):
        # exId (tupla) en este caso seria el valor del nombre de la materia prima
        cone = bd.abrir()
        consultaId = bd.consulta(cone, nombre, ("nombreMateriaPrima", ), "materiasprimas", "idMateriaPrima")
        # cadena = str(consultaId)
        # numId = ''.join([c for c in cadena if c.isdigit()])
        # numId = int(numId)
        try:
            numId, = consultaId[0]
            numId = int(numId)
        except IndexError:
            numId = -1
        return numId
        # return self.idUsuario

    @staticmethod
    def recuperarNombres():
        cone = bd.abrir()
        consulta = bd.recuperarTodos(cone, "materiasprimas", "nombreMateriaPrima")
        return consulta

    @staticmethod 
    def recuperarNombresStockMinimo():
        cone = bd.abrir()
        consulta = bd.recuperarTodos(cone, "materiasprimas", "nombreMateriaPrima, descripcionMateriaPrima, stockMinimoMateriaPrima, stockMateriaPrima", " where stockMinimoMateriaPrima>=stockMateriaPrima")
        return consulta
    
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

#print(MateriaPrima.obtenerId(("Huevo", )))
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

#cone = bd.abrir()
#consulta = bd.recuperarTodos(cone, "materiasprimas", "nombreMateriaPrima", " where stockMinimoMateriaPrima>=stockMateriaPrima")
#print(consulta)
