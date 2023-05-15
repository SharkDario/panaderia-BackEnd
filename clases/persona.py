from abc import ABC, abstractmethod
import mysql.connector

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
