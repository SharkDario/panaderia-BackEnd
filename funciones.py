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
