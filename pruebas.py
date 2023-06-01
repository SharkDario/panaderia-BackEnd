try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry

def example1():
    def print_sel():
        print(cal.selection_get())

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

def example2():
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)

root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')

ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
ttk.Button(root, text='DateEntry', command=example2).pack(padx=10, pady=10)

root.mainloop()
#import tkinter as tk
#from tkinter import font
#root = tk.Tk()
#for font in font.families():
#    print(font)

#num = "677.76"
#print(num.isdigit())

"""
System
8514oem
Fixedsys
Terminal
Modern
Roman
Script
Courier
MS Serif
MS Sans Serif
Small Fonts
Untitled1
DarioFont
Marlett
Arial
Arabic Transparent
Arial Baltic
Arial CE
Arial CYR
Arial Greek
Arial TUR
Arial Black
Bahnschrift Light
Bahnschrift SemiLight
Bahnschrift
Bahnschrift SemiBold
Bahnschrift Light SemiCondensed
Bahnschrift SemiLight SemiConde
Bahnschrift SemiCondensed
Bahnschrift SemiBold SemiConden
Bahnschrift Light Condensed
Bahnschrift SemiLight Condensed
Bahnschrift Condensed
Bahnschrift SemiBold Condensed
Calibri
Calibri Light
Cambria
Cambria Math
Candara
Candara Light
Comic Sans MS
Consolas
Constantia
Corbel
Corbel Light
Courier New
Courier New Baltic
Courier New CE
Courier New CYR
Courier New Greek
Courier New TUR
Ebrima
Franklin Gothic Medium
Gabriola
Gadugi
Georgia
Impact
Ink Free
Javanese Text
Leelawadee UI
Leelawadee UI Semilight
Lucida Console
Lucida Sans Unicode
Malgun Gothic
@Malgun Gothic
Malgun Gothic Semilight
@Malgun Gothic Semilight
Microsoft Himalaya
Microsoft JhengHei
@Microsoft JhengHei
Microsoft JhengHei UI
@Microsoft JhengHei UI
Microsoft JhengHei Light
@Microsoft JhengHei Light
Microsoft JhengHei UI Light
@Microsoft JhengHei UI Light
Microsoft New Tai Lue
Microsoft PhagsPa
Microsoft Sans Serif
Microsoft Tai Le
Microsoft YaHei
@Microsoft YaHei
Microsoft YaHei UI
@Microsoft YaHei UI
Microsoft YaHei Light
@Microsoft YaHei Light
Microsoft YaHei UI Light
@Microsoft YaHei UI Light
Microsoft Yi Baiti
MingLiU-ExtB
@MingLiU-ExtB
PMingLiU-ExtB
@PMingLiU-ExtB
MingLiU_HKSCS-ExtB
@MingLiU_HKSCS-ExtB
Mongolian Baiti
MS Gothic
@MS Gothic
MS UI Gothic
@MS UI Gothic
MS PGothic
@MS PGothic
MV Boli
Myanmar Text
Nirmala UI
Nirmala UI Semilight
Palatino Linotype
Sans Serif Collection
Segoe Fluent Icons
Segoe MDL2 Assets
Segoe Print
Segoe Script
Segoe UI
Segoe UI Black
Segoe UI Emoji
Segoe UI Historic
Segoe UI Light
Segoe UI Semibold
Segoe UI Semilight
Segoe UI Symbol
Segoe UI Variable Small Light
Segoe UI Variable Small Semilig
Segoe UI Variable Small
Segoe UI Variable Small Semibol
Segoe UI Variable Text Light
Segoe UI Variable Text Semiligh
Segoe UI Variable Text
Segoe UI Variable Text Semibold
Segoe UI Variable Display Light
Segoe UI Variable Display Semil
Segoe UI Variable Display
Segoe UI Variable Display Semib
SimSun
@SimSun
NSimSun
@NSimSun
SimSun-ExtB
@SimSun-ExtB
Sitka Small
Sitka Small Semibold
Sitka Text
Sitka Text Semibold
Sitka Subheading
Sitka Subheading Semibold
Sitka Heading
Sitka Heading Semibold
Sitka Display
Sitka Display Semibold
Sitka Banner
Sitka Banner Semibold
Sylfaen
Symbol
Tahoma
Times New Roman
Times New Roman Baltic
Times New Roman CE
Times New Roman CYR
Times New Roman Greek
Times New Roman TUR
Trebuchet MS
Verdana
Webdings
Wingdings
Yu Gothic
@Yu Gothic
Yu Gothic UI
@Yu Gothic UI
Yu Gothic UI Semibold
@Yu Gothic UI Semibold
Yu Gothic Light
@Yu Gothic Light
Yu Gothic UI Light
@Yu Gothic UI Light
Yu Gothic Medium
@Yu Gothic Medium
Yu Gothic UI Semilight
@Yu Gothic UI Semilight
HoloLens MDL2 Assets
Agency FB
Algerian
Book Antiqua
Arial Narrow
Arial Rounded MT Bold
Baskerville Old Face
Bauhaus 93
Bell MT
Bernard MT Condensed
Bodoni MT
Bodoni MT Black
Bodoni MT Condensed
Bodoni MT Poster Compressed
Bookman Old Style
Bradley Hand ITC
Britannic Bold
Berlin Sans FB
Berlin Sans FB Demi
Broadway
Brush Script MT
Bookshelf Symbol 7
Californian FB
Calisto MT
Castellar
Century Schoolbook
Centaur
Century
Chiller
Colonna MT
Cooper Black
Copperplate Gothic Bold
Copperplate Gothic Light
Curlz MT
Dubai
Dubai Light
Dubai Medium
Elephant
Engravers MT
Eras Bold ITC
Eras Demi ITC
Eras Light ITC
Eras Medium ITC
Felix Titling
Forte
Franklin Gothic Book
Franklin Gothic Demi
Franklin Gothic Demi Cond
Franklin Gothic Heavy
Franklin Gothic Medium Cond
Freestyle Script
French Script MT
Footlight MT Light
Garamond
Gigi
Gill Sans MT
Gill Sans MT Condensed
Gill Sans Ultra Bold Condensed
Gill Sans Ultra Bold
Gloucester MT Extra Condensed
Gill Sans MT Ext Condensed Bold
Century Gothic
Goudy Old Style
Goudy Stout
Harlow Solid Italic
Harrington
Haettenschweiler
High Tower Text
Imprint MT Shadow
Informal Roman
Blackadder ITC
Edwardian Script ITC
Kristen ITC
Jokerman
Juice ITC
Kunstler Script
Wide Latin
Lucida Bright
Lucida Calligraphy
Lucida Fax
Lucida Handwriting
Lucida Sans
Lucida Sans Typewriter
Magneto
Maiandra GD
Matura MT Script Capitals
Mistral
Modern No. 20
Monotype Corsiva
MT Extra
Niagara Engraved
Niagara Solid
OCR A Extended
Old English Text MT
Onyx
MS Outlook
Palace Script MT
Papyrus
Parchment
Perpetua
Perpetua Titling MT
Playbill
Poor Richard
Pristina
Rage Italic
Ravie
MS Reference Sans Serif
MS Reference Specialty
Rockwell Condensed
Rockwell
Rockwell Extra Bold
Script MT Bold
Showcard Gothic
Snap ITC
Stencil
Tw Cen MT
Tw Cen MT Condensed
Tw Cen MT Condensed Extra Bold
Tempus Sans ITC
Viner Hand ITC
Vivaldi
Vladimir Script
Wingdings 2
Wingdings 3
Leelawadee
Microsoft Uighur
Cascadia Code ExtraLight
Cascadia Code Light
Cascadia Code SemiLight
Cascadia Code
Cascadia Code SemiBold
Cascadia Mono ExtraLight
Cascadia Mono Light
Cascadia Mono SemiLight
Cascadia Mono
Cascadia Mono SemiBold
PYTHON (multiparadigma, interpretado, tipado dinámico, multiplataforma) 

●	Es un lenguaje de programación multiparadigma, es decir, se pueden utilizar diferentes tipos de desarrollo (modular, orientada a objetos, imperativo).
●	Es interpretado, por lo tanto, no necesita ser compilado antes de ejecutarlo, pues utiliza un intérprete que lee y ejecuta el código fuente directamente. (proceso de desarrollo más rápido y sencillo)
●	Posee un tipado dinámico, pues no se debe especificar que tipo de variable se va a almacenar, puesto que se almacena el valor y el lenguaje ya lo reconoce.
●	Es multiplataforma a nivel a sistema operativo, ya que las aplicaciones que se crean pueden correrse o ejecutarse en cualquier sistema operativo.

LAS INSTRUCCIONES (COMANDOS, ÓRDENES)
●	Apariencia diferente en lenguajes de programación diferentes
●	Existen algunas funciones básicas que se presentan en casi todo lenguaje:
○	Entrada: recibir datos del teclado, o un archivo u otro aparato.
○	Salida: obtener resultados por pantalla.
○	Matemáticas: Ejecutar operaciones básicas de matemáticas como la adición y la multiplicación.
○	Operaciones condicionales: Probar la veracidad de alguna condición y ejecutar una secuencia de instrucciones apropiada.
○	Operaciones de repetición: Ejecutar alguna acción repetidas veces, normalmente con alguna variación.
DEPURACIÓN (DEBUGGING)

●	Errores sintácticos.
○	Condiciona la ejecución del programa.
○	El término sintaxis se refiere a la estructura de cualquier programa y a las reglas de esa estructura.
○	Se visualiza un mensaje de error y se aborta la ejecución.
●	Errores en el tiempo de ejecución.
○	No aparece hasta que se ejecuta el programa.
○	También llamados excepciones.
●	Errores semánticos.
○	Que el programa de un resultado no esperado de acuerdo a los requerimientos.
○	También llamados errores de lógica. 

sintáctico -> (**tiempo de ejecución**) -> semántico

TIPOS DE DATOS 
●	Números
○	Enteros (int)
○	Flotantes (float)
●	Cadenas de caracteres (tipos string str)
●	Booleanos
○	True
○	False
OPERADORES RELACIONALES
 
OPERADORES DE ASIGNACIÓN
●	Permiten asignar un valor a una variable
●	+= → suma a la variable del lado izquierdo el valor del lado derecho
●	-=  → resta a la variable del lado izquierdo el valor del lado derecho
●	*=  → multiplica a la variable del lado izquierdo el valor del lado derecho


LAS ESTRUCTURAS DE CONTROL (Programación)

SENTENCIAS DE CONTROL IF
●	Usadas para tomar decisiones
●	Permiten evaluar una operación lógica
●	Su resultado será verdadero o falso (True o False)
BUCLES DE REPETICIÓN WHILE
●	Realizan múltiples iteraciones dependiendo del resultado de una expresión lógica
●	Su resultado será verdadero o falso (True o False)
BUCLES FOR
●	Permite iterar sobre una secuencia (como una lista) y ejecutar un bloque de código repetidamente para cada elemento.
TIPOS DE DATOS COMPLEJOS
●	Tuplas.
●	Listas.
●	Diccionarios.

EXCEPCIONES - MANEJO DE ERRORES

Al programar en Python algunas veces podemos anticipar errores de ejecución, incluso en un programa sintáctica y lógicamente correcto, pueden llegar a haber errores causados por entrada de datos inválidos o inconsistencias predecibles. 
Para ellos se pueden usar los bloques try y except para manejar estos errores como excepciones. 

SINTAXIS DE TRY Y EXCEPT EN PYTHON

Empecemos por entender la sintaxis de las declaraciones try y except en Python. La sintaxis básica es la siguiente:

try:
	# Código a ejecutar
	# Pero podría haber errores en este bloque
except <tipo de error>:
	# Haz esto para manejar la excepción
	# El bloque except se ejecutará si el bloque try lanza un error
else:
# Esto se ejecutará si el bloque try se ejecuta sin errores  
finally:
	# Este bloque se ejecutará siempre
Veamos el uso de cada uno de estos bloques:
●	El bloque try es el bloque con las sentencias que se quiere ejecutar. Sin embargo, podrían llegar a haber errores de ejecución  y el bloque se dejará de ejecutarse.
●	El bloque except se ejecutará cuando el bloque try falle debido a un error. Este bloque contiene sentencias que generalmente nos dan un contexto de lo que salió mal en el bloque try.
●	Se debe mencionar el tipo de error que se espera, como una excepción dentro del bloque except dentro de <tipo de error>. 
●	Se puede usar except sin especificar el <tipo de error> (pero no se sabrá el tipo de error que pueda ocurrir)
Cuando se ejecute el código dentro del bloque try, existe la posibilidad de que ocurran diferentes errores.
1.	Exception: Captura cualquier tipo de excepción genérica. Es recomendable colocar este bloque al final de los bloques except para capturar cualquier excepción no especificada anteriormente. 
2.	TypeError: Captura excepciones relacionadas con operaciones o tipos de datos incorrectos. 
3.	ValueError: Captura excepciones cuando un valor es de un tipo correcto pero tiene un valor incorrecto. 
4.	ZeroDivisionError: Captura excepciones cuando se intenta dividir entre cero. 
5.	FileNotFoundError: Captura excepciones cuando no se puede encontrar un archivo. 
6.	IndexError: Captura excepciones cuando se intenta acceder a un índice fuera de rango en una lista o secuencia.

●	El bloque else se ejecutará solo si el bloque try se ejecuta sin errores. Esto puede ser útil cuando quieras continuar el código del bloque try. Por ejemplo, si abres un archivo en el bloque try, podrías leer su contenido dentro del bloque else.
●	El bloque finally siempre es ejecutado sin importar que pase en los otros bloques, esto puede ser útil cuando quieras liberar recursos después de la ejecución de un bloque de código  (try, except o else ).
Nota: Los bloques else y finally son opcionales. En muchos casos puedes solo ocupar el bloque try para tratar de ejecutar algo y capturar los errores como excepciones  en el bloque except.
LISTAS

Una lista es una secuencia ordenada de objetos de distintos tipos. Se construyen poniendo los elementos entre corchetes [ ] separados por comas. Se caracterizan por tener un orden, contener elementos de distintos tipos y ser mutables, es decir, pueden alterarse durante la ejecución de un programa.  
*secuencia ordenada de variables de distintos tipos
*mutable
*se construye [], separados por comas
●	Colección de datos de cualquier tipo.
●	Secuencia de valores.
●	Sus valores son llamados elementos o ítems.
●	También conocido en otros lenguajes como arrays o arreglos de datos.
●	Una lista puede ser alterada.

CREACIÓN DE LISTAS MEDIANTE LA FUNCIÓN LIST ()

Otra forma de crear listas es mediante la función list().  

list(c) : Crea una lista con los elementos de la secuencia o colección c. Se pueden indicar los elementos separados por comas, mediante una cadena, o mediante una colección de elementos iterables.


ACCESO A ELEMENTOS DE UNA LISTA

Se utilizan los mismos operadores de acceso que para cadenas de caracteres.  
●	nombres[i]: Devuelve el elemento de la lista nombre con el índice i. 
El índice del primer elemento de la lista es 0. 
SUBLISTAS

nombres[i:j:k]: Devuelve la sublista desde el elemento de nombres con el índice i hasta el elemento anterior al índice j, tomando elementos cada k (es el paso o saltos con los que toma los elementos).   – sublista = nombres[1:5:2]

Si "i" se omite, se asume que comienza en el índice cero.
Si "j" se omite, se asume que se detiene en el final de la lista.
Si "k" se omite, se asume que se toma cada elemento (k=1).
Algunos ejemplos para ilustrar su uso:
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Devuelve [2, 4, 6, 8]
print(l[2:9:2])
# Devuelve [0, 3, 6, 9]
print(l[::3])
# Devuelve [9, 7, 5, 3]
print(l[-1:-8:-2])

palabras = ["hola", "mundo", "soy", "un", "asistente", "virtual"]
# Devuelve ["mundo", "un"]
print(palabras[1:5:2])
# Devuelve ["asistente", "un", "hola"]
print(palabras[-2::-2])
# Devuelve ["virtual", "un", "mundo", "hola"]
print(palabras[::-1])



OPERACIONES QUE NO MODIFICAN UNA LISTA

●	len(nombres): Devuelve el número de elementos de la lista nombres.  
●	min(nombres): Devuelve el mínimo elemento de la lista nombres siempre que los datos sean comparables.  
●	max(nombres): Devuelve el máximo elemento de la lista nombres siempre que los datos sean comparables.  
●	sum(nombres): Devuelve la suma de los elementos de la lista l, siempre que los datos se puedan sumar.  
●	dato in nombres: Devuelve True si el dato pertenece a la lista nombres y False en caso contrario.  
●	nombres.index(dato): Devuelve la posición que ocupa en la lista nombre el primer elemento con valor dato.  
●	nombres.count(dato): Devuelve el número de veces que el valor dato está contenido en la lista nombre.  
●	all(nombres): Devuelve True si todos los elementos de la lista nombres son True y False en caso contrario.  
●	any(nombres): Devuelve True si algún elemento de la lista nombres es True y False en caso contrario. 
#DATO in Lista
numeros = [1, 3, 5, 7, 9]
# Devuelve True porque 5 está en la lista "numeros"
print(5 in numeros)
# Devuelve False porque 2 no está en la lista "numeros"
print(2 in numeros)
# Devuelve True porque la lista "numeros" no está vacía
print(bool(numeros))
# Devuelve False porque la lista "vacia" está vacía
vacia = []
print(bool(vacia))



OPERACIONES QUE MODIFICAN UNA LISTA

●	nombres1 + nombres2: Crea una nueva lista concatenando los elementos de la listas nombres1 + nombres2. 
●	nombres.append(dato): Añade dato al final de la lista nombres.  
●	nombres.extend(sequencia): Añade los datos de sequencia que puede ser otra lista, tupla o cadena al final de la lista nombre. 
●	nombres.insert(índice, dato): Inserta dato en la posición índice de la lista nombres y desplaza los elementos una posición a partir de la posición índice.  
●	nombres.remove(dato): Elimina el primer elemento con valor dato en la lista nombres y desplaza los que están por detrás de él una posición hacia delante.  
●	nombres.pop([índice]): Devuelve el dato en la posición índice y lo elimina de la lista nombres, desplazando los elementos por detrás de él una posición hacia delante.  PERMITE GUARDAR EL ELEMENTO BORRADO
●	nombres.clear(): borra toda la lista.
●	nombres.sort(): Ordena los elementos de la lista nombres de acuerdo al orden predefinido, siempre que los elementos sean comparables.  
●	nombres.reverse(): invierte el orden de los elementos de la lista nombres.
●	nombres.extend(otra lista): Añade los elementos de otra lista al final de la lista nombres.
●	del frutas([índice]): Se utiliza para eliminar un elemento específico de una lista.
●	nombres.remove(“marcelo”): permite eliminar un elemento haciendo referencia al elemento y no a la posición.
●	nombres.index(valor): se utiliza para obtener el índice de la primera aparición de un elemento específico valor en una lista.
●	sorted(nombres):  se utiliza para ordenar una secuencia (como una lista, tupla o cadena) en orden ascendente. - sorted(nombres, reverse= True) -> ordenado de modo descendente

OPERACIONES DE STRING DE LISTAS

●	print(nombreCompleto.upper()): imprime todo en mayúscula
●	print(nombreCompleto.lower()): imprime todo en minúscula
●	print(nombreCompleto.capitaliza()): imprime la primera en mayúscula
●	print(nombreCompleto.tittle()): imprime en mayúscula la primera letra de cada palabra en la cadena
●	print(nombreCompleto.strip()): imprime sin espacios en blanco antes y después de la cadena
●	print(nombreCompleto.lstrip()): imprime sin espacios en blanco antes de la cadena
●	print(nombreCompleto.rstrip()): imprime sin espacios en blanco después de la cadena
●	print(nombreCompleto.find(“fi”)): buscar una subcadena dentro de otra cadena, localiza el número de posición de esa subcadena. SIRVE PARA BUSCAR UN @ DENTRO DE UN CORREO ELECTRÓNICO.
●	print(nombreCompleto.replace(“wa”, “pa”)): reemplaza una subcadena por otra subcadena dentro de una cadena.
●	print(“wa” in nombres): devuelve un booleano en el caso de que esa subcadena está dentro.
●	print (“@” not in nombres): retorna un booleano dependiendo de la existencia

FUNCIONES IMPORTADAS

import math
●	print(abs(-75,3) #retorna el valor absoluto
●	print(round(75.7)) #retorna el valor redondeado
●	print(math.ceil(75,8)) #retorna el entero superior más cercano
●	print(math.floor(75,89)) #retorna el entero inferior más cercano
●	print(math.pow(2,3)) #eleva un número (2) a una potencia (3)
●	print(math.ceil(75,8)) #retorna el entero superior más cercano
●	print(math.sqrt(9)) #retorna la raíz cuadrada de un número


CONVERSIÓN DE TIPOS 

numero1 = 10
numero2 = 20

print(str(numero1)+str(numero2))

print(float(numero1)+float(numero2))

print(int(numero1)+int(numero2))

print(bool(“”)) #devuelve falso
print(bool(0)) #devuelve falso
print(bool(None)) #devuelve falso
print(bool([]))

print(bool(“pepe”)) #devuelve verdadero
print(bool(“ “)) #devuelve verdadero – porque tiene espacio

FUNCIONES

Una función es un fragmento de código con un nombre asociado que realiza una serie de tareas y devuelve un valor. 

A los fragmentos de código que tienen un nombre asociado y no devuelven valores se les suele llamar procedimientos. 

Además de ayudarnos a programar y depurar dividiendo el programa en partes las funciones también permiten reutilizar código. 

En Python las funciones se declaran de la siguiente forma:

def mi_funcion(param1, param2):
    print param1
    print param2

mi_funcion(variable1, variable2)

Es decir, la palabra clave def seguida del nombre de la función y entre paréntesis los argumentos separados por comas. A continuación, en otra línea, indentado y después de los dos puntos tendríamos las líneas de código que conforman el código a ejecutar por la función. 

TUPLA
Es una colección ordenada e inmutable de elementos del mismo o diferente tipo. 
Es similar a una lista, pero a diferencia de las listas, las tuplas no pueden modificarse una vez creadas. 
Se representan utilizando paréntesis () y los elementos dentro de una tupla están separados por comas.

No se pueden agregar, eliminar o modificar elementos individuales de una tupla.

print(mi_tupla[0])  # Imprime el primer elemento de la tupla: 1
print(mi_tupla[3])  # Imprime el cuarto elemento de la tupla: "Hola"

DICCIONARIO
Es una estructura de datos que permite almacenar y organizar datos de manera flexible.

Los diccionarios utilizan claves y valores. 
Un diccionario se define mediante llaves {} y contiene una colección de pares clave-valor. 
Cada clave se asocia con un valor específico. Las claves deben ser únicas dentro de un diccionario, pero los valores pueden repetirse.

diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "México"}

Se puede acceder a los valores de un diccionario utilizando sus claves.

tup1 = ('h', 'e', 'l', 'l', 'o')
def tuplaTocadena(tup1):
    cad = ""
    longi = len(tup1)
    for i in range(longi):
        if (i == 0):
            cad = f"({tup1[0]}, "
        elif (i == longi-1):
            cad = cad + f"{tup1[-1]})"
        else:
            cad = cad + f"{tup1[i]}, "
    return cad


print(tuplaTocadena(tup1))

print(bool(""))
print(bool(0))
print(bool(None))
# n = int(input("Ingrese un número entero: "))
# if n > 1:
#    print(f"El numero {n} es mayor a 1")
# else:
#    print(f"El numero {n} es menor o igual a 1")
lista = [7, 7, 8, 9]
num = 9
# num = lista + num
# print(lista[2])

lista2 = [5, "anto", lista]
lista2[0] = 7
lista2[2].append(9)

# print(lista2[2])

acum = 0
# for elemento in lista:
#    acum = acum + elemento
acum = sum(lista)
prom = acum / (len(lista))
# print(f"Promedio: {prom} - Minimo: {min(lista)} - Maximo: {max(lista)}")

# dato = int(input("Ingrese su nota: "))
# if dato in lista:
#    print(f"Existe {dato} en la lista")
# else:
#    print(f"No existe {dato} en la lista")

# print(lista.count(7))
lista3 = [6, 700, 7, 9, 10]
listaN = ["anto", "dario", "azul"]
indice = listaN.index("anto")
print(indice)
varListaOrdenada = sorted(lista3)
lista3.sort()
# lista3.reverse()
# lista3.sort(reverse=True)
print(lista3)
del lista3[0]
print(lista3)
lista3.remove(700)
print(lista3)
# print(lista3[0])
# elem3 = lista3.pop(3)
# print(lista3[0])
# lista4 = lista + lista3
# print(lista)
# print(lista3)
# print(lista4)
# print(lista2)
anto = {'nombre': "anto", 'color': "lila", 'edad': 21}
print(anto['nombre'])

listaDePerso = []
listaDePerso.append(anto)
dario = {'nombre': "dario", 'color': "azul", 'edad': 24}
listaDePerso.append(dario)

for perso in listaDePerso:
    print(f"Nombre: {perso['nombre']}")

diccioP = {'nombre': "dario", 'color': "azul", 'edad': 24}
if diccioP in listaDePerso:
    print("Existe la persona en la lista")
else:
    print("No existe")

tupla = ()


def fSuma(a, b):
    suma = a + b
    return suma


sumados = fSuma(30, 50)

palabras = ["hola", "mundo", "soy", "un", "asistente", "virtual"]
# Devuelve ["mundo", "un"]
print(palabras[1:5:2])
listNum = [4, 5, 3]
sorted(listNum)
print(listNum)
listNum.sort()
print(listNum)

productos = {}
# codigo = "10101010"
# producto = {'Nombre':"chipa",'Precio':300,'Stock':400}


def agregarProducto(productos):
    bande = True
    while (bande):
        try:
            codigo = int(input("Ingrese el codigo del producto: "))
            if (codigo not in productos):
                bande = False
            else:
                print("Error. Codigo ya existente.")
        except ValueError:
            print("Error. Debe ser un numero entero.")
    nombre = input("Ingrese el nombre del producto: ")
    bande = True
    while (bande):
        try:
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock del producto: "))
            bande = False
        except ValueError:
            print("Error. Deben ser numeros.")
    producto = {'Nombre': nombre, 'Precio': precio, 'Stock': stock}
    productos[codigo] = producto


def mostrarProductos(productos):
    for clave, producto in productos.items():
        print(
            f"Codigo: {clave} - Nombre: {producto['Nombre']} - Precio: {producto['Precio']} - Stock: {producto['Stock']}")

# productos.keys() productos.values()


agregarProducto(productos)
print(productos)
agregarProducto(productos)
mostrarProductos(productos)


def fBuscarEnLista(lista, letra):
    listaLetra = []
    letra = letra.upper()
    for elem in lista:
        elemAux = elem['descripcion'].upper()
        if len(elemAux) >= len(letra):
            bande = True
            for i in range(len(letra)):
                if (elemAux[i] != letra[i]):
                    bande = False
            if (bande):
                listaLetra.append(elem)
    return listaLetra

# conduc = ["dario", "diana", "gabriel"]
# distan = [40, 30, 60]
# listaCD = [["dario", 40], ["diana", 30], ["gabriel", 60]]
# listaOrdenadaAZ = sorted(listaCD, key=lambda i: (i[0]))

# mybox = ['cables', 'headphones', 'USB']
# item1, item2, item3 = mybox
# primero, *nouUsado, ultimo = mybox

# *string, = 'PythonIsTheBest'
# string
# ['P', 'y', 't', 'h', 'o', 'n', 'I', 's', 'T', 'h', 'e', 'B', 'e', 's', 't']
"""