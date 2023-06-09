
class funciones(): #es una clase estática porque todas sus funciones lo son
    @staticmethod # convierte a una función en estática 
    def nSToCad(n): # se le pasa la cantidad de "%s" que necesitamos
        cadS = ""  # acumulador de la cadena
        for i in range(n): # recorre la cantidad de veces "n"
            if (i != n-1): # si todavia no es el final
                cadS = cadS + "%s," # annade %s,
            else:
                cadS = cadS + "%s" # annade %s
        return cadS #retorna la cadena con las %s - "%s, %s, %s"
    @staticmethod # convierte a una función en estática 
    def ingDNI_CUIL(cuil, n, nombre='CUIL/CUIT'): # verifica tanto si el cuil como el dni es valido
        mensaje = "" # se le pasa n por la cantidad de valores que tienen cuil-11 dni-8 
        lista=[]
        if((len(cuil)!=n)|(cuil.isdigit()==False)): # se verifica tanto la longitud como si es entero
            if(len(cuil)!=n): # si es distinto de 11 u 8, entonces dice que debe tener 11 u 8 caracteres
                mensaje += f"El {nombre} debe contener {n} caracteres."
            if(cuil.isdigit()==False): # si no es un num entero, entonces comenta el mensaje de abajo
                mensaje += f"\nEl {nombre} debe contener sólo números, sin espacios ni puntos."
        if(mensaje==""): # si el mensaje quedo vacio quiere decir que es un cuil o dni valido
            return cuil # entonces lo retorna
        else: # sino, entonces annade el mensaje a la lista y la retorna
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

