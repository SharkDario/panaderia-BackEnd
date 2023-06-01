from abc import ABC, abstractmethod
from usuario import Usuario
from baseDeDatos import baseDeDatos as bd
import mysql.connector


class Administrador(Usuario):
    def __init__(self, DNI, CUIL_CUIT, nombre, domicilio, telefono, user, clave, new=None):
        # 1 es tipo de usuario Administrador
        super().__init__(user, clave, 1, DNI, nombre, CUIL_CUIT, domicilio, telefono)
        #self.idUsuario = idUsuario
        # alta del administrador
        if (new is None):
            cone = bd.abrir()
            datos = (DNI, CUIL_CUIT, nombre, domicilio, telefono, user, clave, 1)
            nAtrib = 8
            nombreAtrib = "DNI, CUIL_CUIT, nombre, domicilio, telefono, usuario, clave, idTipoUsuario"
            bd.alta(cone, datos, "usuarios", nombreAtrib, nAtrib)

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

    def contratacion(self, fechaInicio, idAdmin, idEmpleado):
        #INSERT INTO contratacion (idContratacion, fechaInicioContratacion, fechaFinContratacion, idUsuarioAdmin, idUsuarioEmpleado)
        #VALUES (?, ?, ?, (SELECT idUsuario FROM usuarios WHERE idTipoUsuario = 1 LIMIT 1), (SELECT idUsuario FROM usuarios WHERE idTipoUsuario = 2 LIMIT 1));
        #tuplaT = ("usuarios", "contratacion")
        #tuplaId = ("idUsuario", "fechaInicioContratacion")
        cone = bd.abrir()
        datos = (fechaInicio, idAdmin, idEmpleado)
        nombreA = "fechaInicioContratacion, idUsuarioAdmin, idUsuarioEmpleado"
        bd.alta(cone, datos, "contratacion", nombreA, 3)
        #cone2 = bd.abrir()
        #bd.joinContratacion(cone2)

        """
        INSERT INTO contratacion (fechaInicioContratacion, idUsuarioAdmin, idUsuarioEmpleado)
        VALUES (?, ?, ?)
        SELECT contratacion.fechaInicioContratacion, usuariosAdmin.idUsuario, usuariosEmpleado.idUsuario
        FROM contratacion
        JOIN usuarios AS usuariosAdmin ON contratacion.idUsuarioAdmin = usuariosAdmin.idUsuario
        JOIN usuarios AS usuariosEmpleado ON contratacion.idUsuarioEmpleado = usuariosEmpleado.idUsuario;
        """

    @classmethod
    def obtenerAdmi(cls, DNI, tuplaV=None):
        cone = bd.abrir()
        tupla = bd.consulta(cone, (DNI, ), ("DNI", ), "usuarios", "*")
        tupla = tupla[0]
        #idUsuario = tupla[0]
        #DNI = tupla[1]
        CUIL_CUIT = tupla[2]
        nombre = tupla[3]
        domicilio = tupla[4]
        telefono = tupla[5]
        user = tupla[6]
        clave = tupla[7]
        if(tuplaV==True):
            return tupla
        else:
            return cls(DNI, CUIL_CUIT, nombre, domicilio, telefono, user, clave, True)


#admi = Administrador(41111111, 20411111119, "Miguel Dario Coronel", "Calle anchoa", "3704259037", "Dario07", "morimayi")
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
