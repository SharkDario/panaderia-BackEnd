from abc import ABC, abstractmethod

#hola
class Persona(ABC):

    def inicializarPerso(self, dni, nombre, cuil, domi):
        self.dni = dni
        self.nombre = nombre
        self.cuil_cuit = cuil
        self.domicilio = domi

    def modificarPerso(self, valor, elec):
        if (elec == "N"):
            self.nombre = valor
        elif (elec == "D"):
            self.domicilio = valor

    def obtenerPerso(self, elec):
        if (elec == "D"):
            return self.dni
        elif (elec == "N"):
            return self.nombre
        elif (elec == "C"):
            return self.cuil_cuit
        elif (elec == "Do"):
            return self.domicilio

    @abstractmethod
    def obtenerId(self):
        pass


class Usuario(Persona, ABC):
    def inicializarUser(self, user, contra, tipo, dni, nombre, cuil, domi):
        super().inicializarPerso(dni, nombre, cuil, domi)
        self.user = user
        self.contra = contra
        self.tipo = tipo

    def modificarUser(self, valor, elec):
        if (elec == "U"):
            self.user = valor
        elif (elec == "C"):
            self.contra = valor

    def obtenerUser(self, elec):
        if (elec == "U"):
            return self.user
        elif (elec == "C"):
            return self.contra
        elif (elec == "T"):
            return self.tipo

    def iniciarSesion(self, userIng, contraIng):
        if ((self.user == userIng) & (self.user == contraIng)):
            print("Login exitoso")
        else:
            print("Error. No ha podido ingresar.")


class Administrador(Usuario):
    def inicializarAdmin(self, user, contra, tipo, dni, nombre, cuil, domi, idAdmin):
        super().inicializarUser(user, contra, tipo, dni, nombre, cuil, domi)
        self.idAdmin = idAdmin

    def obtenerId(self):
        return self.idAdmin

    # def ConsultarEstadosDeIngresos GenerarReciboDeSueldo ConsultarPresupuesto

from baseDeDatos import abrir
class Personal(Usuario):
    def inicializarPersonal(self, user, contra, tipo, dni, nombre, cuil, domi, salario, puesto, idPerso):
        super().inicializarUser(user, contra, tipo, dni, nombre, cuil, domi)
        self.salario = salario
        self.puesto = puesto
        self.idPerso = idPerso

    def alta(self, datos):
        cone = abrir()
        cursor = cone.cursor()
        sql = "insert into usuario(idUsuario, DNI, CUIL/CUIT, nombre, domicilio, user, clave, idTipoUsuario) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        
    def modificarPersonal(self, valor, elec):
        if (elec == "S"):
            self.salario = valor
        elif (elec == "P"):
            self.puesto = valor

    def obtenerPersonal(self, elec):
        if (elec == "S"):
            return self.salario
        elif (elec == "P"):
            return self.puesto

    def obtenerId(self):
        return self.idPerso


class Cliente(Persona):
    def inicializarCliente(self, idCliente, dni, nombre, cuil, domi):
        super().inicializarPerso(dni, nombre, cuil, domi)
        self.idCliente = idCliente

    # def modificarCliente(self, valor, elec):
    #    if (elec == ""):
    #        self.
    #    elif (elec == ""):
    #        self.

    # def obtenerCliente(self, elec):
    #    if (elec == ""):
    #        return self.
    #    elif (elec == ""):
    #        return self.
    #    elif (elec == ""):
    #        return self.

    def obtenerId(self):
        return self.idCliente
