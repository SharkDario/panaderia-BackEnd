"""
from pantallaInicio import *

pLogin()
opcionIngresada = int(input("Seleccione una opción: "))

if (opcionIngresada == 1):
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su contraseña: ")
    if ((usuario == "BRENDA") & (clave == "1234")):
        pMenuAdministrador()
    else:
        pMenuPersonal("comprador")
else:
    print("AHORA REGISTRARSE!!!!!!!")
"""

#from curses.ascii import isdigit

class funciones():
    @staticmethod
    def nSToCad(n):
        cadS = ""  # cadena %s
        for i in range(n):
            if (i != n-1):
                cadS = cadS + "%s,"
            else:
                cadS = cadS + "%s"
        return cadS
    @staticmethod
    def ingDNI_CUIL(cuil, n, nombre='CUIL/CUIT'):
        mensaje = ""
        lista=[]
        if((len(cuil)!=n)|(cuil.isdigit()==False)):
            if(len(cuil)!=n):
                mensaje += f"El {nombre} debe contener {n} caracteres."
            if(cuil.isdigit()==False):
                mensaje += f"\nEl {nombre} debe contener sólo números, sin espacios ni puntos."
        if(mensaje==""):
            return cuil
        else:
            lista.append(mensaje)
            return lista
    @staticmethod
    def ingNombreMatPro(nombre, idMateria, cad):
        #obtiene el ID de la materia prima/producto, si es -1 quiere decir que no existe y el nombre es válido
        if(idMateria==-1):
            return nombre
        else:
            return [f"El nombre {cad} ya existe en la base de datos."]
    @staticmethod
    def ingNumPosi(num, cad):
        #para validar únicamente números positivos mayores a 0
        bande=True
        try:
            num = float(num)
            if(num<=0):
                bande=False
        except Exception:
            bande=False
        if(bande):
            return num
        else:
            return [f"{cad} debe ser mayor a 0."]

    @staticmethod
    def ingNum(num, cadena, n=-1):
        aux=""
        if(n==-1):
            n=len(num)
        else:
            aux=f"\n{cadena} debe contener máximo {n} números."
        mensaje = ""
        lista = []
        if ((num.isdigit()) & (len(num)<=n)):
            return num
        else:
            mensaje +=f"\n{cadena} debe contener sólo números, sin espacios ni puntos."+aux
            lista.append(mensaje)
            return lista
    @staticmethod
    def dniCuilComparar(dni, cuil):
        bande=False
        cuilCompa = cuil[2:-1]
        if(cuilCompa==dni):
            bande=True
        return bande
    @staticmethod
    def ingUser(user, usuarios):
        #usuarios = Usuario.recuperarNombresUser()
        #usuarios = usuarios[0]
        mensaje=""
        lista = []
        if(usuarios!=[]):
            for usuario in usuarios:
                if(user==usuario[0]):
                    mensaje = "El usuario ya existe en la base de datos."
        if(mensaje==""):
            return user
        else:
            lista.append(mensaje)
            return lista
    @staticmethod
    def ingDNI(dniIng, listaDni):
        #listaDni = Usuario.recuperarDNIs()
        #listaDni = listaDni[0]
        mensaje=""
        lista = []
        if(listaDni!=[]):
            #listaDni = listaDni[0]
            dniN = int(dniIng)
            for dni in listaDni:
                #print(tupla)
                #print(dni)
                if(dniN==dni[0]):
                    mensaje = "El DNI ya existe en la base de datos."
                    break
        if(mensaje==""):
            return dniIng
        else:
            lista.append(mensaje)
            return lista
    @staticmethod
    def ingClaveValida(clave1):
        bandeNum=False
        bandeMayus=False
        bandeNoEspacio=True
        mensaje=""
        for letra in clave1:
            if(letra.isdigit()):
                bandeNum=True
            if(letra.isupper()):
                bandeMayus=True
            if(letra.isspace()):
                bandeNoEspacio=False
        if(len(clave1)<8):
            mensaje+="\nLa contraseña debe contener al menos 8 carácteres."
        if(bandeNum==False):
            mensaje+="\nLa contraseña debe contener al menos un número."
        if(bandeMayus==False):
            mensaje+="\nLa contraseña debe contener al menos una mayúscula."
        if(bandeNoEspacio==False):
            mensaje+="\nLa contraseña no puede contener espacios en blanco."
        lista=[]
        if(mensaje!=""):
            lista.append(mensaje)
            return lista
        else:
            return clave1
    @staticmethod
    def ingClave(clave1, clave2, text="Las contraseñas no coinciden"):
        lista = []
        if(clave1==clave2):
            return clave1
        else:
            mensaje = f"{text}."
            lista.append(mensaje)
            return lista
    @staticmethod
    def recuperarIden():
        iden="478190"
        return iden

