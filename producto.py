from abc import ABC, abstractmethod
from articulo import Articulo
from datetime import datetime
from baseDeDatos import baseDeDatos as bd
import mysql.connector


class Producto(Articulo):
    def __init__(self, nombre, descripcion, precioUnitario, stock, stockMinimo, new=None):
        # stock minimo debe ser mayor que 0
        super().__init__(nombre, descripcion, precioUnitario, stock, stockMinimo)
        # alta del producto
        if (new is None):
            cone = bd.abrir()
            datos = (nombre, descripcion, precioUnitario, stock, stockMinimo)
            nAtrib = 5
            nombreAtrib = "nombreProducto, descripcionProducto, precioUnitarioProducto, stockProducto, stockMinimoProducto"
            bd.alta(cone, datos, "productos", nombreAtrib, nAtrib)

    @staticmethod
    def bajaProducto(idProd):
        cone = bd.abrir()
        bd.baja(cone, (idProd, ), ("idProducto", ), "productos")

    def fabricacion(self, idMateria, Cant):
        cone0 = bd.abrir()
        idProducto = Producto.obtenerId((self.nombre, ))
        datosC = (idProducto, idMateria)
        idF = bd.consulta(cone0, datosC, ("idProducto","idMateriaPrima"), "fabricacion", "idFabricacion")
        if(idF==[]):
            cone = bd.abrir()
            datos = (idProducto, idMateria, Cant)
            nombreA = "idProducto, idMateriaPrima, CantidadMateriaPrima"
            bd.alta(cone, datos, "fabricacion", nombreA, 3)
        else:
            return True

    def recuperarMateriasPrimas(self, idPro):
        cone = bd.abrir()
        # atributoS el atributo en especifico o atributos que se quieren conseguir en formato cadena
        # Por ejemplo: idUsuario  ;  idUsuario, CUIL_CUIT
        # dDatos = tupla con los datos necesarios - en el caso de usuario es solo DNI
        consulta = bd.consulta(cone, (idPro, ), ("idProducto", ), "fabricacion", "idMateriaPrima, CantidadMateriaPrima")
        return consulta

    @staticmethod
    def obtenerId(nombre):
        # exId (tupla) en este caso seria el valor del nombre de la materia prima
        cone = bd.abrir()
        consultaId = bd.consulta(cone, nombre, ("nombreProducto", ), "productos", "idProducto")
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
        consulta = bd.recuperarTodos(cone, "productos", "nombreProducto")
        return consulta

    @staticmethod 
    def recuperarNombresDesPUStock():
        cone = bd.abrir()
        consulta = bd.recuperarTodos(cone, "productos", "nombreProducto, descripcionProducto, precioUnitarioProducto, stockProducto")
        return consulta

    @staticmethod 
    def recuperarNombresStockMinimo():
        cone = bd.abrir()
        consulta = bd.recuperarTodos(cone, "productos", "nombreProducto, descripcionProducto, stockMinimoProducto, stockProducto", " where stockMinimoProducto>=stockProducto")
        return consulta
   
    @classmethod
    def obtenerPro(cls, nombre, tuplaV=None):
        cone = bd.abrir()
        tupla = bd.consulta(cone, (nombre, ), ("nombreProducto", ), "productos", "*")
        tupla = tupla[0]
        descripcion = tupla[2]
        precioU = tupla[3]
        stock = tupla[4]
        stockM = tupla[5]
        if(tuplaV==True):
            return tupla
        else:
            return cls(nombre, descripcion, precioU, stock, stockM, True)

#fechaV = datetime.strptime('5/25/25', '%m/%d/%y')
#producto1 = Producto("Chipa", "en kg", 300, 60, fechaV, 10)

#producto1 = Producto.obtenerPro("Chipa")
#print(f"{producto1.nombre} - {producto1.descripcion} - {producto1.precioU}")
#print(f'ID {Producto.obtenerId(("Chipa", ))}')

