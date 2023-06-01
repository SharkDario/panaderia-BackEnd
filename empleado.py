from abc import ABC, abstractmethod
from datetime import datetime
from usuario import Usuario
from baseDeDatos import baseDeDatos as bd
import mysql.connector
from datetime import datetime


class Empleado(Usuario):
    def __init__(self, DNI, CUIL_CUIT, nombre, domicilio, telefono, user, clave, idTipoEmpleado, new=None):
        # 2 es tipo de usuario Empleado
        #Ejemplo: una fecha convertida a str: "2022-06-25 11:00:56.813000"
        #Ejemplo: (fechastr, '%d/%m/%Y/%H/%M')
        #dateObject=datetime.strptime(fechaStr, '%Y-%m-%d %H:%M:%S')
        super().__init__(user, clave, 2, DNI, nombre, CUIL_CUIT, domicilio, telefono)
        self.cargo=idTipoEmpleado
        if(idTipoEmpleado=="Repositor"):
            idTipoEmpleado=1
        elif(idTipoEmpleado=="Vendedor"):
            idTipoEmpleado=2
        else:
            idTipoEmpleado=3
        #self.idUsuario = idUsuario
        # alta del Empleado
        if (new==None):
            cone = bd.abrir()
            datos = (DNI, CUIL_CUIT, nombre, domicilio, telefono, user, clave, 2)
            nAtrib = 8
            nombreAtrib = "DNI, CUIL_CUIT, nombre, domicilio, telefono, usuario, clave, idTipoUsuario"
            bd.alta(cone, datos, "usuarios", nombreAtrib, nAtrib)
            tuplaDni = (DNI, )
            idUsuario = Empleado.obtenerId(tuplaDni)
            cone = bd.abrir()
            self.tipoDeEmpleado(idTipoEmpleado, idUsuario)
            #self.contratacion(idUsuario, fechaInicio)
    

    def tipoDeEmpleado(self, idTipoEmpleado, idUsuario):
        tuplaT = ("usuarios", "tipoUsuario")
        tuplaId = ("idTipoUsuario","idTipoEmpleado","idUsuario")
        datos = (idTipoEmpleado, idUsuario, 2)
        #dDatos = (idTipoEmpleado, idUsuario, 2)
        #tablas[0] - usuarios
        #tablas[1] - tipoUsuario
        #ides[0] - idTipoUsuario
        #ides[1] - idTipoEmpleado
        #ides[2] - idUsuario
        cone = bd.abrir()
        bd.join(cone, datos, tuplaT, tuplaId)

    @staticmethod
    def verFechaContratacion(idEmple):
        #consulta(cone, dDatos, cadenaT, tabla, atributoS)
        #idEmple debe ser tupla
        cone = bd.abrir()
        consultaFC = bd.consulta(cone, idEmple, ("idUsuarioEmpleado", ), "contratacion", "fechaInicioContratacion")
        return consultaFC

    @staticmethod
    def obtenerId(exId):
        # exId (tupla) en este caso seria el valor del DNI
        cone = bd.abrir()
        consultaId = bd.consulta(cone, exId, ("DNI", ), "usuarios", "idUsuario")
        # cadena = str(consultaId)
        # numId = ''.join([c for c in cadena if c.isdigit()])
        # numId = int(numId)
        numId, = consultaId[0]
        numId = int(numId)
        return numId
        # return self.idUsuario
    @staticmethod
    def obtenerDNIs():
        #idTipoUsuario
        cone = bd.abrir()
        #return bd.consulta(cone, (2, ), ("idTipoUsuario", ), "usuarios", "DNI")
        return bd.recuperarTodosEspecifico(cone, "usuarios", "DNI", "idTipoUsuario", (2, ))

    @classmethod
    def obtenerEmpleado(cls, listaDNIs, DNI, tuplaV=None):
        existe=False
        for dniL in listaDNIs:
            #print(f"{type(dniL)} - {dniL} - dnil")
            #print(f"{type(DNI)} - {DNI} - DNI")
            if(dniL==DNI):
                existe=True
                break
        if(existe):
            DNI = DNI[0]
            cone = bd.abrir()
            tupla = bd.consulta(cone, (DNI, ), ("DNI", ), "usuarios", "*")
            #print(tupla)
            tupla = tupla[0]
            #idUsuario = tupla[0]
            DNI = tupla[1]
            CUIL_CUIT = tupla[2]
            nombre = tupla[3]
            domicilio = tupla[4]
            telefono = tupla[5]
            user = tupla[6]
            clave = tupla[7]
            cone2 = bd.abrir()
            consultaTipo = bd.consultaJoin(cone2, (DNI, ))
            #print(consultaTipo)
            idTipoEmpleado = consultaTipo[0][0] #debo cambiarlo
            #fechaInicio = 9 #debo cambiarlo
            if(tuplaV==True):
                return tupla
            else:
                #DNI, CUIL_CUIT, nombre, domicilio, telefono, user, clave, idTipoEmpleado, fechaInicio, new=None
                return cls(DNI, CUIL_CUIT, nombre, domicilio, telefono, user, clave, idTipoEmpleado, True)
        else:
            return existe
#DNI, CUIL_CUIT, nombre, domicilio, telefono, user, clave, idTipoEmpleado, fechaInicio
#dateObject=datetime.strptime(fechaStr, '%Y-%m-%d %H:%M:%S')
#fecha = datetime.strptime("2023-5-25", '%Y-%m-%d')
#emple = Empleado(17171717, 20171717178, "Noeli Coro", "Inmi", 3704555555, "Dionel", "1567", 3, fecha)

# admi = Administrador("Dario07", "", 41111111, "Miguel Dario Coronel", 20411111119, "Calle anchoa", 1)
# cone = bd.abrir()
# ad = bd.consulta(cone, (41111111, ), ("DNI", ), "usuarios", "*")
# print(ad)
# ad = ad[0]


# tuplaDNI = 41111111
# tuplaDNI = (tuplaDNI, )
# idUser = Administrador.obtenerId(tuplaDNI)

# print(type(int(str(idUser[0]))))"(1,)"
# print(f"ID del usuario: {idUser}")
# ad = Administrador.obtenerAdmi(ad)
# ad.modificarUser("morimayi", idUser, "clave")
# contratar
# crear producto
# crear materia prima
# def ConsultarEstadosDeIngresos GenerarReciboDeSueldo ConsultarPresupuesto
