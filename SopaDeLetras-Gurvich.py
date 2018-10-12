from random import randrange, shuffle
from math import sqrt, ceil
#Constantes
ABECEDARIO = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z")
LARGOABC = len(ABECEDARIO)

#Tipo de dato
"""
Representamos un tablero de Sopa de letras con Listas de Listas (matriz)
Un string representa un caracter en la sopa y los espacios vacios son 0 (Int)
Las listas dentro representan columnas, los indices de sus elementos representan las posicion Y, con Y invertido (Positivos hacia abajo)
Contando desde 0
Por ej, la posicion (4,3) = tablero[2][1] = 8
tablero = [[1,2,3],[4,5,6],[7,8,9]] -> 1 4 7
                                       2 5 8
                                       3 6 9
"""
"""
La lista de palabras puede tomar forma de:
-Lista de strings con cada string siendo una palabra (Con todos los caracteres en mayuscula)
-Lista de listas, cada lista interior contiene la palabra original y una tupla para cada letra
En las tuplas se especifica la coordenada X,Y donde se coloco y el valor que tenia anteriormente
La lista puede ser una mezcla de las 2
Por ej:
P1 = ["TATETI","SUDOKU","SOPA","DE","LETRAS"]
P2 = [["TATETI",(0,0,0),(0,1,0),(0,2,"D"),(0,3,0),(0,4,"K"),(0,5,0)],"SUDOKU","SOPA","DE","LETRAS"]
"""

def totalCaracteres(lista):
    """
    Representamos palabras con strings y su largo con Ints
    totalCaracteres : List(Str) -> Int
    totalCaracteres recibe una lista de palabras y devuelve la suma total de todos sus caracteres
    Ejemplos:
    totalCaracteres(["Perro","gato","cobayo"]) => 15
    totalCaracteres([]) => 0
    """
    sum = 0
    for i in lista:
        sum += len(i)
    return sum

def totalCaracteresTest():
    assert totalCaracteres(["Perro","gato","cobayo"]) == 15
    assert totalCaracteres([]) == 0
totalCaracteresTest()

def largoPalabraMasLarga(lista):
    """
    Representamos palabras con strings y su largo con Ints
    largoPalabraMasLarga : List(Str) -> Int
    largoPalabraMasLarga recibe una lista de palabras, devuelve el largo de la palabra mas larga
    Ejemplos:
    largoPalabraMasLarga(["Perro","gato","Encefalograma"]) => 13
    largoPalabraMasLarga([]) => 0
    """
    largo = 0
    for i in lista:
        if len(i) > largo:
            largo = len(i)
    return largo

def largoPalabraMasLargaTest():
    assert largoPalabraMasLarga(["Perro","gato","Encefalograma"]) == 13
    assert largoPalabraMasLarga([]) == 0
largoPalabraMasLargaTest()

def rellenarTablero(tablero):
    """
    Se utilizan letras de la constante ABECEDARIO
    rellenarTablero : List(List(Str | Int)) -> List(List(Str))
    rellenarTablero recibe un tablero de Sopa de letras incompleto y llena los espacios vacios (0) con letras al azar del ABECEDARIO
    """
    Nfilas = len(tablero)
    Ncolumnas = len(tablero[0])
    for y in range(Nfilas):
        for x in range(Ncolumnas):
            if tablero[y][x] == 0:
                posletra = randrange(LARGOABC)
                letra = ABECEDARIO[posletra]
                tablero[y][x] = letra
    return tablero

def revertir(str):
    """
    revertir : Str -> Str
    revertir recibe un string, devuelve el string invertido
    Ejemplos:
    revertir("hola") => "aloh"
    revertir("Electroencefalografista") => "atsifargolafecneortcelE"
    revertir("") => ""
    """
    nuevoStr = ""
    for i in str:
        nuevoStr = i + nuevoStr
    return nuevoStr

def revertirTest():
    assert revertir("hola") == "aloh"
    assert revertir("Electroencefalografista") == "atsifargolafecneortcelE"
    assert revertir("") == ""
revertirTest()

def palabraIncluida(palabra,lista):
    """
    Representamos una palabra con un string
    palabraIncluida : List(Str) List(List(Str)) -> Bool
    palabraIncluida recibe una palabra y una lista de palabras, devuelve True si la palabra (o su inversa) se encuentra en la lista o incluida dentro de otra palabra
    Ejemplos:
    palabraIncluida("ola",["arena","mar","ola","playa"]) => True
    palabraIncluida("no",["yo","tu","el","nosotros","vosotros","ellos"]) => True
    palabraIncluida("True",[]) => False
    palabraIncluida("comer",["fisurar","remocar","limpiar"]) => True
    """
    for i in lista:
        if palabra in i:
            return True
        if revertir(palabra) in i:
            return True
    return False

def palabraIncluidaTest():
    assert palabraIncluida("ola",["arena","mar","ola","playa"]) == True
    assert palabraIncluida("no",["yo","tu","el","nosotros","vosotros","ellos"]) == True
    assert palabraIncluida("True",[]) == False
    assert palabraIncluida("comer",["fisurar","remocar","limpiar"]) == True
palabraIncluidaTest()

def eliminaIncluidos(lista):
    """
    Representamos palabras con Strings
    eliminaIncluidos : List(Str) -> List(Str)
    eliminaIncluidos recibe una lista de palabras (solo strings)
    Devuelve la lista sin las palabras repetidas o que se incluyen dentro de otras
    Ejemplos:
    eliminaIncluidos(["ola","arena","mar","ola","hola","playa"]) => ["arena","mar","hola","playa"]
    eliminaIncluidos(["comer","fisurar","remocar","limpiar"]) => ["fisurar","remocar","limpiar"]
    eliminaIncluidos(["chau","tirar","saludar"]) => ["chau","tirar","saludar"]
    """
    for palabra in lista:
        i = lista.index(palabra)
        resto = lista[:i] + lista[i+1:]
        if palabraIncluida(palabra,resto):
            lista = resto
    return lista

def eliminaIncluidosTest():
    assert eliminaIncluidos(["ola","arena","mar","ola","hola","playa"]) == ["arena","mar","hola","playa"]
    assert eliminaIncluidos(["comer","fisurar","remocar","limpiar","remo"]) == ["fisurar","remocar","limpiar"]
    assert eliminaIncluidos(["chau","tirar","saludar"]) == ["chau","tirar","saludar"]
eliminaIncluidosTest()

def generaTablero(n):
    """
    generaTablero : Int -> List(List(Int))
    generaTablero recibe un numero natural N, devuelve una matriz de NxN con todos sus elementos 0
    Ejemplos:
    generaTablero(3) => [[0,0,0],[0,0,0],[0,0,0]]
    generaTablero(1) => [[0]]
    generaTablero(4) => [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    """
    tablero = [[0 for x in range(n)] for i in range(n)]
    return tablero

def generaTableroTest():
    assert generaTablero(3) == [[0,0,0],[0,0,0],[0,0,0]]
    assert generaTablero(1) == [[0]]
    assert generaTablero(4) == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
generaTableroTest()

def generaListaPalabras():
    lista = []
    n = int(input("Ingrese la cantidad total de palabras: "))
    contador = 1
    while contador <= n:
        palabra = input("Ingrese la palabra n°" + str(contador) + ": ")
        lista += [palabra]
        contador += 1
    for i in lista:
        p = lista.index(i)
        lista[p] = i.upper()
    return lista

def faltaPoner(palabras):
    """
    faltaPoner : List(Str) | List(List(Str | Tuple(Int))) -> Bool
    faltaPoner recibe una lista palabras y devuelve True si aun quedan palabras por colocar
    (si en la lista principal hay strings)
    Ejemplos:
    faltaPoner(["PERRO","GATO","PAJARO"]) => True
    faltaPoner([["PERRO",(1,2),(3,1)],"GATO","PAJARO"]) => True
    faltaPoner([["PERRO",(1,2),(3,1)],["GATO",(3,1),(4,5)],["PAJARO",(6,7),(9,8)]]) => False
    """
    for i in palabras:
        if type(i) == str:
            return True
    return False

def faltaPonerTest():
    assert faltaPoner(["PERRO","GATO","PAJARO"]) == True
    assert faltaPoner([["PERRO",(1,2),(3,1)],"GATO","PAJARO"]) == True
    assert faltaPoner([["PERRO",(1,2),(3,1)],["GATO",(3,1),(4,5)],["PAJARO",(6,7),(9,8)]]) == False
faltaPonerTest()

def cualPoner(palabras):
    """
    cualPoner : List(Str) | List(List(Tuple(Int) | Str)) -> Tuple(Str | Int)
    cualPoner recibe una lista de palabras con al menos una no colocada en el tablero (no reemplazada por una lista de tuplas)
    Devuelve una tupla con la palabra y su indice en la lista
    Ejemplos:
    cualPoner(["PERRO","GATO","PAJARO"]) => ("PERRO",0)
    cualPoner(["PERRO",(1,2),(3,1)],"GATO","PAJARO"]) => ("GATO",1)
    cualPoner([["PERRO",(1,2),(3,1)],["GATO",(3,1),(4,5)],["PAJARO",(6,7),(9,8)]],"OSO") => ("OSO",3)
    """
    for i in palabras:
        if type(i) == str:
            indice = palabras.index(i)
            return (i,indice)

def cualPonerTest():
    assert cualPoner(["PERRO","GATO","PAJARO"]) == ("PERRO",0)
    assert cualPoner([["PERRO",(1,2),(3,1)],"GATO","PAJARO"]) == ("GATO",1)
    assert cualPoner([["PERRO",(1,2),(3,1)],["GATO",(3,1),(4,5)],["PAJARO",(6,7),(9,8)],"OSO"]) == ("OSO",3)
cualPonerTest()

def direccion():
    """
    Representamos direcciones con tuplas, horizontal = (1,0), vertical = (0,1) y diagonal = (1,1)
    direccion : -> tuple(Int)
    direccion devuelve, al ser llamada, una tupla que representa la direccion que tomara la palabra elegida al azar
    """
    a = randrange(3)
    if a == 0:
        return (1,0)
    elif a == 1:
        return (0,1)
    else:
        return (1,1)

def sentido(direccion):
    """
    Representamos sentido con un entero entre 0 y 1, 0 representa "normal" y 1 representa "invertido"
    sentido : tuple(Int) -> Int
    sentido recibe la direccion que tomara la palabra y un sentido al azar, a menos que su direccion sea diagonal, en ese caso devuelve "normal" = 0
    """
    if direccion == (1,1):
        return 0
    else:
        sent = randrange(2)
        return sent
assert sentido((1,1)) == 0

def lugares(tablero,direccion,palabra):
    """
    Representamos los lugares posibles con una lista de tuplas, cada tupla representa un par coordenado X,Y
    lugares : List(List(Int | Str)) Tuple(Int) Str -> List(Tuple(Int))
    lugares recibe el tablero, la direccion y la palabra
    Devuelve todas las posiciones donde la palabra puede empezar para asegurar entrar en el tablero
    Ejemplos:
    lugares(generaTablero(6),(1,1),"PERRO") => [(0,0),(0,1),(1,0),(1,1)]
    lugares(generaTablero(5),(1,0),"OLA") => [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5)]
    lugares(generaTablero(3),(0,1),"MANO") => []
    """
    anchoAlto = len(tablero)
    lpalabra = len(palabra)
    posibles = []
    if direccion == (1,0):
        maxX = anchoAlto - lpalabra + 1
        maxY = anchoAlto
    elif direccion == (0,1):
        maxX = anchoAlto
        maxY = anchoAlto - lpalabra + 1
    else:
        maxX = anchoAlto - lpalabra + 1
        maxY = anchoAlto - lpalabra + 1
    for x in range(maxX):
            for y in range(maxY):
                posibles += [(x,y)]
    return posibles

def lugaresTest():
    assert lugares(generaTablero(6),(1,1),"PERRO") == [(0,0),(0,1),(1,0),(1,1)]
    assert lugares(generaTablero(5),(1,0),"OLA") == [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(2,2),(2,3),(2,4)]
    assert lugares(generaTablero(3),(0,1),"MANO") == []
lugaresTest()

def validarLugar(tablero,letra,pos):
    """
    Representamos posiciones con una tupla X,Y
    validarLugar : List(List(Int | Str)) Str Tuple(Int) -> Bool
    validarLugar recibe un tablero, una letra y una posicion, devuelve True si la letra se puede ubica,
    (La posicion es 0 o tiene la misma letra)
    Ejemplos:
    validarLugar(generaTablero(3),"A",(1,1)) => True
    validarLugar([["A","B","C"],[0,0,0],[0,0,0]],"C",(1,0)) => False
    """
    lugar = tablero[pos[0]][pos[1]]
    if letra == lugar or lugar == 0:
        return True
    return False

def validarLugarTest():
    assert validarLugar(generaTablero(3),"A",(1,1)) == True
    assert validarLugar([["A","B","C"],[0,0,0],[0,0,0]],"C",(0,1)) == False
validarLugarTest()

def validarPalabraLugar(tablero,posini,direccion,palabra):
    """
    Representamos posiciones con una tupla X,Y
    Representamos direccion con una tupla (0,1), (1,0) o (1,1)
    Representamos palabras con Strings y todos sus caracteres en mayúscula
    validarPalabraLugar : List(List(Int)) Tuple(Int) Tuple(Int) Str -> Bool
    validarPalabraLugar recibe un tablero, una posicion, una direccion y una palabra
    Devuelve True si se puede colocar la palabra con esas condiciones
    Ejemplos:
    validarPalabraLugar(generaTablero(5),(0,0),(1,0),"HOLA") => True
    validarPalabraLugar([["A","B","C"],[0,0,0],[0,0,0]],(0,2),(0,1),"OLA") => False
    """
    t = (posini[0],posini[1],direccion[0],direccion[1])
    for letra in palabra:
        if tablero[t[0]][t[1]] == 0 or tablero[t[0]][t[1]] == letra:
            t = (t[0]+t[2],t[1]+t[3],t[2],t[3])
        else:
            return False
    return True

def validarPalabraLugarTest():
    assert validarPalabraLugar(generaTablero(5),(0,0),(1,0),"HOLA") == True
    assert validarPalabraLugar([["A","B","C"],[0,0,0],[0,0,0]],(0,2),(0,1),"OLA") == False
validarPalabraLugarTest()

def ponerPalabras(tablero,palabras):
    """
    Representamos el tablero con una matriz NxN
    ponerPalabras : List(LIst(Int)) -> List(LIst(Int | Str))
    ponerPalabras recibe un tablero vacio (todos sus elementos son 0) y una lista de palabras, devuelve el tablero con las palabras colocadas
    """
    while faltaPoner(palabras):
        palabra = cualPoner(palabras)
        direccionP = direccion()
        sentidoP = sentido(direccionP)
        if sentidoP == 1:
            palabra = (revertir(palabra[0]),palabra[1]) #Revertimos la palabra en la tupla
            palabras[palabra[1]] = palabra[0] #Reemplazamos la palabra en la lista por la revertida
        Lugares = lugares(tablero,direccionP,palabra[0])
        shuffle(Lugares)
        for p in Lugares:
            v = validarLugar(tablero,palabra[0][0],p)

def generaSopa():
    palabras = generaListaPalabras()
    palabras = eliminaIncluidos(palabras)
    tamaño = totalCaracteres(palabras)
    tamaño = sqrt(tamaño)
    tamaño = ceil(tamaño)
    masLarga = largoPalabraMasLarga(palabras)
    if tamaño < masLarga:
        tamaño = masLarga
    tamaño = tamaño + 2 #Si sumar 2 no funciona, multiplicar por 2
    tablero = generaTablero(tamaño)
    ponerPalabras(tablero,palabras)
    tablero = rellenarTablero(tablero)
    return tablero

def main():
    print("Elija una opcion:")
    print("1- Generar sopa de letras\n2- Resolver sopa automaticamente")
    eleccion = int(input(""))
    if eleccion == 1:
        generaSopa()
    elif eleccion == 2:
        resuelveSopa()

def resuelveSopa():
    print("Yo mama so fat")