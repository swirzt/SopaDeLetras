from random import randrange, shuffle
from math import sqrt, ceil, floor
from sys import setrecursionlimit
#Constantes
ABECEDARIO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
LARGOABC = len(ABECEDARIO)
setrecursionlimit(1500)

#Tipo de dato
"""
Representamos un tablero de Sopa de letras con Listas de Listas (matriz)
Un string representa un caracter en la sopa y los espacios vacios son 0 (Int)
Las listas dentro representan filas, los indices de sus elementos representan las posicion X, y las filas el Y con Y invertido (Positivos hacia abajo)
Contando desde 0
Representamos un posicion como (y,x)
Por ej, la posicion (1,2) = tablero[1][2] = 6
tablero = [[1,2,3],[4,5,6],[7,8,9]] -> 1 2 3
                                       4 5 6
                                       7 8 9

Generamos el tablero en un archivo .txt de nombre sopagenerada. Las palabras usadas para generar dicha sopa se guardan en un archivo .txt de nombre listaPalabras
Para encontrar las palabras en una sopa, recibe el archivo sopagenerada.txt que contiene la sopa de letras, y el archivo listaPalabras.txt que contiene las palabras a buscar
Ambos archivos deben encontrarse en la carpeta donde se ejecuta el programa

En sopagenerada.txt se almacena la sopa de modo que cada linea representa una fila del tablero, las letras son todas mayusculas
En listaPalabras.txt se almacenan las palabras colocadas de modo que cada linea representa una palabra distinta, tambien en mayuscula

La lista de palabras puede tomar forma de:
-Lista de strings con cada string siendo una palabra (Con todos los caracteres en mayuscula)
-Lista de listas, cada lista interior contiene la palabra original y una tupla para cada letra
En las tuplas se especifica la coordenada X,Y donde se coloco y el valor que tenia anteriormente
La lista puede ser una mezcla de las 2
Por ej:
P1 = ["TATETI","SUDOKU","SOPA","DE","LETRAS"]
P2 = [["TATETI",(0,0,0),(0,1,0),(0,2,"T"),(0,3,0),(0,4,"T"),(0,5,0)],"SUDOKU","SOPA","DE","LETRAS"]
"""

def totalCaracteres(lista):
    """
    - Representamos palabras con strings y su largo con Ints
    - totalCaracteres : List(Str) -> Int
    - totalCaracteres recibe una lista de palabras y devuelve la suma total de todos sus caracteres
    - Ejemplos:
    - totalCaracteres(["Perro","gato","cobayo"]) => 15
    - totalCaracteres([]) => 0
    """
    sum = 0
    for palabra in lista:
        sum += len(palabra)
    return sum

def test_totalCaracteres():
    assert totalCaracteres(["Perro","gato","cobayo"]) == 15
    assert totalCaracteres([]) == 0

def largoPalabraMasLarga(lista):
    """
    - Representamos palabras con strings y su largo con Ints
    - largoPalabraMasLarga : List(Str) -> Int
    - largoPalabraMasLarga recibe una lista de palabras, devuelve el largo de la palabra mas larga
    - Ejemplos:
    - largoPalabraMasLarga(["Perro","gato","Encefalograma"]) => 13
    - largoPalabraMasLarga([]) => 0
    """
    largo = 0
    for palabra in lista:
        largo = max(largo,len(palabra))
    return largo

def test_largoPalabraMasLarga():
    assert largoPalabraMasLarga(["Perro","gato","Encefalograma"]) == 13
    assert largoPalabraMasLarga([]) == 0

def rellenarTablero(tablero):
    """
    - Se utilizan letras de la constante ABECEDARIO
    - rellenarTablero : List(List(Str | Int)) -> List(List(Str))
    - rellenarTablero recibe un tablero de Sopa de letras incompleto y llena los espacios vacios (0) con letras al azar del ABECEDARIO
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
    - revertir : Str -> Str
    - revertir recibe un string, devuelve el string invertido
    - Ejemplos:
    - revertir("hola") => "aloh"
    - revertir("Electroencefalografista") => "atsifargolafecneortcelE"
    - revertir("") => ""
    """
    nuevoStr = ""
    for letra in str:
        nuevoStr = letra + nuevoStr
    return nuevoStr

def test_revertir():
    assert revertir("hola") == "aloh"
    assert revertir("Electroencefalografista") == "atsifargolafecneortcelE"
    assert revertir("") == ""

def palabraIncluida(palabra,lista):
    """
    - Representamos una palabra con un string
    - palabraIncluida : List(Str) List(List(Str)) -> Bool
    - palabraIncluida recibe una palabra y una lista de palabras, devuelve True si la palabra (o su inversa) se encuentra en la lista o incluida dentro de otra palabra
    - Ejemplos:
    - palabraIncluida("ola",["arena","mar","ola","playa"]) => True
    - palabraIncluida("no",["yo","tu","el","nosotros","vosotros","ellos"]) => True
    - palabraIncluida("True",[]) => False
    - palabraIncluida("comer",["fisurar","remocar","limpiar"]) => True
    """
    elemento = 0
    largoL = len(lista)
    inversa = revertir(palabra)
    while elemento < largoL and not palabra in lista[elemento] and not inversa in lista[elemento]:
        elemento += 1
    if elemento < largoL:
        return True
    else:
        return False

def test_palabraIncluida():
    assert palabraIncluida("ola",["arena","mar","ola","playa"]) == True
    assert palabraIncluida("no",["yo","tu","el","nosotros","vosotros","ellos"]) == True
    assert palabraIncluida("True",[]) == False
    assert palabraIncluida("comer",["fisurar","remocar","limpiar"]) == True

def eliminaIncluidos(lista):
    """
    - Representamos palabras con Strings
    - eliminaIncluidos : List(Str) -> List(Str)
    - eliminaIncluidos recibe una lista de palabras (solo strings)
    - Devuelve la lista sin las palabras repetidas o que se incluyen dentro de otras
    - Ejemplos:
    - eliminaIncluidos(["ola","arena","mar","ola","hola","playa"]) => ["arena","mar","hola","playa"]
    - eliminaIncluidos(["comer","fisurar","remocar","limpiar"]) => ["fisurar","remocar","limpiar"]
    - eliminaIncluidos(["chau","tirar","saludar"]) => ["chau","tirar","saludar"]
    """
    for palabra in lista:
        i = lista.index(palabra)
        resto = lista[:i] + lista[i+1:]
        if palabraIncluida(palabra,resto):
            lista = resto
    return lista

def test_eliminaIncluidos():
    assert eliminaIncluidos(["ola","arena","mar","ola","hola","playa"]) == ["arena","mar","hola","playa"]
    assert eliminaIncluidos(["comer","fisurar","remocar","limpiar","remo"]) == ["fisurar","remocar","limpiar"]
    assert eliminaIncluidos(["chau","tirar","saludar"]) == ["chau","tirar","saludar"]

def generaTablero(n):
    """
    - generaTablero : Int -> List(List(Int))
    - generaTablero recibe un numero natural N, devuelve una matriz de NxN con todos sus elementos 0
    - Ejemplos:
    - generaTablero(3) => [[0,0,0],[0,0,0],[0,0,0]]
    - generaTablero(1) => [[0]]
    - generaTablero(4) => [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    """
    tablero = [[0 for x in range(n)] for y in range(n)]
    return tablero

def test_generaTablero():
    assert generaTablero(3) == [[0,0,0],[0,0,0],[0,0,0]]
    assert generaTablero(1) == [[0]]
    assert generaTablero(4) == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

"""
generaListaPalabras -> list(str)
generaListaPalabras: Genera una lista de n elementos que contiene las palabras ingresadas por el usuario
Se espera que la cantidad de palabras sea mayor o igual a 1 
"""
def generaListaPalabras():
    lista = []
    n = int(input("Ingrese la cantidad total de palabras: "))
    contador = 1
    while contador <= n:
        palabra = input("Ingrese la palabra n°" + str(contador) + ": ")
        lista += [palabra]
        contador += 1
    for i in range(len(lista)):
        lista[i] = lista[i].upper()
    return lista

def faltaPoner(palabras):
    """
    - faltaPoner : List(Str) | List(List(Str | Tuple(Int))) -> Bool
    - faltaPoner recibe una lista palabras y devuelve True si aun quedan palabras por colocar
    - (si en la lista principal hay strings)
    - Ejemplos:
    - faltaPoner(["PERRO","GATO","PAJARO"]) => True
    - faltaPoner([["PERRO",(1,2),(3,1)],"GATO","PAJARO"]) => True
    - faltaPoner([["PERRO",(1,2),(3,1)],["GATO",(3,1),(4,5)],["PAJARO",(6,7),(9,8)]]) => False
    """
    elemento = 0
    largoL = len(palabras)
    while elemento < largoL and type(palabras[elemento]) != str:
        elemento += 1
    if elemento < largoL:
        return True
    else:
        return False

def test_faltaPoner():
    assert faltaPoner(["PERRO","GATO","PAJARO"]) == True
    assert faltaPoner([["PERRO",(1,2),(3,1)],"GATO","PAJARO"]) == True
    assert faltaPoner([["PERRO",(1,2),(3,1)],["GATO",(3,1),(4,5)],["PAJARO",(6,7),(9,8)]]) == False

def cualPoner(palabras):
    """
    - cualPoner : List(Str) | List(List(Tuple(Int) | Str)) -> Tuple(Str | Int)
    - cualPoner recibe una lista de palabras con al menos una no colocada en el tablero (no reemplazada por una lista de tuplas)
    - Devuelve una tupla con la palabra y su indice en la lista
    - Ejemplos:
    - cualPoner(["PERRO","GATO","PAJARO"]) => ("PERRO",0)
    - cualPoner(["PERRO",(1,2),(3,1)],"GATO","PAJARO"]) => ("GATO",1)
    - cualPoner([["PERRO",(1,2),(3,1)],["GATO",(3,1),(4,5)],["PAJARO",(6,7),(9,8)]],"OSO") => ("OSO",3)
    """
    for elemento in palabras:
        if type(elemento) == str:
            indice = palabras.index(elemento)
            return (elemento,indice)

def test_cualPoner():
    assert cualPoner(["PERRO","GATO","PAJARO"]) == ("PERRO",0)
    assert cualPoner([["PERRO",(1,2),(3,1)],"GATO","PAJARO"]) == ("GATO",1)
    assert cualPoner([["PERRO",(1,2),(3,1)],["GATO",(3,1),(4,5)],["PAJARO",(6,7),(9,8)],"OSO"]) == ("OSO",3)

def direccion():
    """
    - Representamos direcciones con tuplas, horizontal = (0,1), vertical = (1,0) y diagonal = (1,1)
    - direccion : -> tuple(Int)
    - direccion devuelve, al ser llamada, una tupla que representa la direccion que tomara la palabra elegida al azar
    """
    a = randrange(5)
    if a == 0 or a == 3:
        return (0,1)
    elif a == 1 or a == 4:
        return (1,0)
    else:
        return (1,1)

def sentido(direccion):
    """
    - Representamos sentido con un entero entre 0 y 1, 0 representa "normal" y 1 representa "invertido"
    - sentido : tuple(Int) -> Int
    - sentido recibe la direccion que tomara la palabra y un sentido al azar, a menos que su direccion sea diagonal, en ese caso devuelve "normal" = 0
    """
    if direccion == (1,1):
        return 0
    else:
        sent = randrange(2)
        return sent

def test_sentido():
    assert sentido((1,1)) == 0

def lugares(tablero,direccion,palabra):
    """
    - Representamos los lugares posibles con una lista de tuplas, cada tupla representa un par coordenado X,Y
    - lugares : List(List(Int | Str)) Tuple(Int) Str -> List(Tuple(Int))
    - lugares recibe el tablero, la direccion y la palabra
    - Devuelve todas las posiciones donde la palabra puede empezar para asegurar entrar en el tablero
    - Ejemplos:
    - lugares(generaTablero(6),(1,1),"PERRO") => [(0,0),(0,1),(1,0),(1,1)]
    - lugares(generaTablero(5),(1,0),"OLA") => [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5)]
    - lugares(generaTablero(3),(0,1),"MANO") => []
    """
    anchoAlto = len(tablero)
    lpalabra = len(palabra)
    posibles = []
    maxX = -1
    maxY = -1
    if direccion == (0,1):
        maxX = anchoAlto - lpalabra + 1
        maxY = anchoAlto
    elif direccion == (1,0):
        maxX = anchoAlto
        maxY = anchoAlto - lpalabra + 1
    else:
        maxX = anchoAlto - lpalabra + 1
        maxY = anchoAlto - lpalabra + 1
    for y in range(maxY):
            for x in range(maxX):
                posibles += [(y,x)]
    return posibles

def test_lugares():
    assert lugares(generaTablero(6),(1,1),"PERRO") == [(0,0),(0,1),(1,0),(1,1)]
    assert lugares(generaTablero(5),(1,0),"OLA") == [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(2,2),(2,3),(2,4)]
    assert lugares(generaTablero(3),(0,1),"MANO") == []

def validarPalabraLugar(tablero,posini,direccion,palabra):
    """
    - Representamos posiciones con una tupla Y.X
    - Representamos direccion con una tupla (0,1), (1,0) o (1,1)
    - Representamos palabras con Strings y todos sus caracteres en mayúscula
    - validarPalabraLugar : List(List(Int | Str)) Tuple(Int) Tuple(Int) Str -> Bool
    - validarPalabraLugar recibe un tablero, una posicion, una direccion y una palabra
    - Devuelve True si se puede colocar la palabra con esas condiciones
    - Ejemplos:
    - validarPalabraLugar(generaTablero(5),(0,0),(1,0),"HOLA") => True
    - validarPalabraLugar([["A","B","C"],[0,0,0],[0,0,0]],(0,2),(0,1),"OLA") => False
    """
    t = (posini[0],posini[1],direccion[0],direccion[1])
    letra = 0
    largopalabra = len(palabra)
    while letra < largopalabra and (tablero[t[0]][t[1]] == 0 or tablero[t[0]][t[1]] == palabra[letra]):
        t = (t[0]+t[2],t[1]+t[3],t[2],t[3])
        letra += 1
    if letra < largopalabra:
        return False
    else:
        return True

def test_validarPalabraLugar():
    assert validarPalabraLugar(generaTablero(5),(0,0),(1,0),"HOLA") == True
    assert validarPalabraLugar([["A","B","C"],[0,0,0],[0,0,0]],(0,2),(0,1),"OLA") == False

def ponerPalabra(tablero,posini,direccion,palabra):
    """
    - Representamos posiciones con una tupla Y,X
    - Representamos direccion con una tupla (0,1), (1,0) o (1,1)
    - Representamos palabras con Strings y todos sus caracteres en mayúscula
    - Se esperan tableros de dimensiones que permitan a la palabra ubicerse completamente
    - ponerPalabra : List(List(Int | Str)) Tuple(Int) Tuple(Int) Str -> List(Tuple)
    - ponerPalabra recibe un tablero, una posicion, una direccion y una palabra
    - Coloca la palabra en el tablero comenzando por la posicion inicial y siguiendo en la direccion dada
    - Devuelve una lista con tuplas que representan la posicion y el valor que tenian en donde se posicionaron las letras
    - Ejemplos:
    - ponerPalabra(generaTablero(5),(0,0),(0,1),"HOLA") => [(0,0,0),(0,1,0),(0,2,0),(0,3,0)]
    - ponerPalabra([["H","C","K","T"],["B","O","L","A"],[0,0,0,0],[0,0,0,0]],(0,0),(1,1),"HOY") => [(0,0,"H"),(1,1,"O"),(2,2,0)]
    """
    tuplas = []
    tp = (posini[0],posini[1],direccion[0],direccion[1])
    for letra in palabra:
        tuplas += [(tp[0],tp[1],tablero[tp[0]][tp[1]])]
        tablero[tp[0]][tp[1]] = letra
        tp = (tp[0]+tp[2],tp[1]+tp[3],tp[2],tp[3])
    return tuplas

def test_ponerPalabra():
    assert ponerPalabra(generaTablero(5),(0,0),(0,1),"HOLA") == [(0,0,0),(0,1,0),(0,2,0),(0,3,0)]
    assert ponerPalabra([["H","C","K","T"],["B","O","L","A"],[0,0,0,0],[0,0,0,0]],(0,0),(1,1),"HOY") == [(0,0,"H"),(1,1,"O"),(2,2,0)]

def quitarPalabra(tablero,postupla):
    """
    - Representamos las posiciones a revertir con una tupla de 3 elementos (fila,columa,valoranterior)
    - quitarPalabra : List(List(Str | Int)) List(Tuple(Int)) -> List(List(Str | Int))
    - quitarPlabra recibe un tablero y una lista de posiciones a revertir, devuelve el tablero con los valores anteriores a poner la palabra
    - Ejemplos:
    - quitarPalabra([["H","O","L","A"],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[(0,0,0),(0,1,0),(0,2,0),(0,3,0)]) => [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    - quitarPalabra([["H","C","K","T"],["B","O","L","A"],[0,0,"Y",0],[0,0,0,0]],[(0,0,"H"),(1,1,"O"),(2,2,0)]) => [["H","C","K","T"],["B","O","L","A"],[0,0,0,0],[0,0,0,0]]
    """
    for elem in postupla:
        tablero[elem[0]][elem[1]] = elem[2]
    return tablero

def test_quitarPalabra():
    assert quitarPalabra([["H","O","L","A"],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[(0,0,0),(0,1,0),(0,2,0),(0,3,0)]) == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    assert quitarPalabra([["H","C","K","T"],["B","O","L","A"],[0,0,"Y",0],[0,0,0,0]],[(0,0,"H"),(1,1,"O"),(2,2,0)]) == [["H","C","K","T"],["B","O","L","A"],[0,0,0,0],[0,0,0,0]]

def ponerPalabras(tablero,palabras):
    """
    - Representamos el tablero con una matriz NxN
    - ponerPalabras : List(LIst(Int)) -> List(LIst(Int | Str))
    - ponerPalabras recibe un tablero vacio (todos sus elementos son 0) y una lista de palabras, devuelve el tablero con las palabras colocadas
    """
    while faltaPoner(palabras):
        palabraActual = cualPoner(palabras)
        direccionP = direccion()
        sentidoP = sentido(direccionP)
        if sentidoP:
            palabraActual = (revertir(palabraActual[0]),palabraActual[1]) #Revertimos la palabra en la tupla
            palabras[palabraActual[1]] = palabraActual[0] #Reemplazamos la palabra en la lista por la revertida
        listaLugares = lugares(tablero,direccionP,palabraActual[0])
        shuffle(listaLugares)
        sePuede = False
        iteracion = 0
        while not sePuede and iteracion < len(listaLugares):
            if validarPalabraLugar(tablero,listaLugares[iteracion],direccionP,palabraActual[0]):
                sePuede = True
                reemplazo = ponerPalabra(tablero,listaLugares[iteracion],direccionP,palabraActual[0])
                palabras[palabraActual[1]] = reemplazo
                ponerPalabras(tablero,palabras)
                if palabraActual[1] < len(palabras)-1 and type(palabras[palabraActual[1]+1]) == str:
                        sePuede = False
                        quitarPalabra(tablero,reemplazo)
            iteracion += 1
        if type(palabras[palabraActual[1]]) == str:
            return tablero
    return tablero

def imprimeTablero(tablero):
    """
    - imprimeTablero : List(List(Str | Int) -> NONE
    - imprimeTablero recibe un tablero e imprime sus filas y agrega una fila y columna guia
    """
    for fila in tablero:
        filaStr = ""
        for columna in fila:
            filaStr += (columna + " ")
        print(filaStr)

def generaSopa():
    palabras = generaListaPalabras()
    copiaPalabras = palabras [:]
    palabras = eliminaIncluidos(palabras)
    tamaño = totalCaracteres(palabras)
    tamaño = ceil(sqrt(tamaño))
    masLarga = largoPalabraMasLarga(palabras)
    tamaño = floor(max(tamaño,masLarga) * 1.5)
    tablero = generaTablero(tamaño)
    ponerPalabras(tablero,palabras)
    contador = 1
    largoPalabras = len(palabras)
    if palabras == []:
        palabras = [0]
    while type(palabras[largoPalabras-1]) == str and contador < largoPalabras:
        palabras = palabras[1:] + palabras[0]
        ponerPalabras(tablero,palabras)
        contador += 1
    if type(palabras[0]) == str:
        return generaTablero(tamaño),["NO SE PUDO"]
    tablero = rellenarTablero(tablero)
    imprimeTablero(tablero)
    return tablero,copiaPalabras

def checkPos(tablero,pos,palabra):
    """
    - Representamos posiciones con una tupla (y,x)
    - checkPos : List(List(Str)) Tuple(Int,Int) Str -> Bool || List(Sring)
    - checkPos recibe un tablero, una posicion a buscar (contiene la primer letra de la palabra) y una palabra
    - Si la palabra se encuentra en forma vertical horizontal o diagonal desde ese punto, devuelve las indicaciones correspondientes
    - Ejemplos:
    - checkPos(generaTablero(5),(0,0),"GATO") => False
    - checkPos([["H","B","C"],["P","O","G"],["K","Z","Y"]],(0,0),"HOY") => ["Diagonal","Descendente"]
    - checkPos([["C","A","S","A"],["A","C","A","S"],["S","A","C","A"],["A","S","A","C"]],(3,3),"CASA") => ["Vertical","Arriba"]
    """
    alto = len(tablero)
    ancho = len(tablero[0])
    largoPalabra = len(palabra)
    maxDer = ancho - largoPalabra
    maxInf = alto - largoPalabra
    minSupIzq = largoPalabra - 1
    if pos[0] <= maxInf: #Abajo (+Y)
        copiaPos = (pos[0],pos[1])
        palabraPos = ""
        letra = 0
        while letra < largoPalabra:
            palabraPos += tablero[copiaPos[0]][copiaPos[1]]
            copiaPos = (copiaPos[0]+1,copiaPos[1])
            letra += 1
        if palabra == palabraPos:
            listaPos = ["Vertical","Abajo"]
            return listaPos
    if pos[0] >= minSupIzq: #Arriba (-Y)
        copiaPos = (pos[0],pos[1])
        palabraPos = ""
        letra = 0
        while letra < largoPalabra:
            palabraPos += tablero[copiaPos[0]][copiaPos[1]]
            copiaPos = (copiaPos[0]-1,copiaPos[1])
            letra += 1
        if palabra == palabraPos:
            listaPos = ["Vertical","Arriba"]
            return listaPos
    if pos[1] >= minSupIzq: #Izquierda (-X)
        copiaPos = (pos[0],pos[1])
        palabraPos = ""
        letra = 0
        while letra < largoPalabra:
            palabraPos += tablero[copiaPos[0]][copiaPos[1]]
            copiaPos = (copiaPos[0],copiaPos[1]-1)
            letra += 1
        if palabra == palabraPos:
            listaPos = ["Horizontal","Izquierda"]
            return listaPos
    if pos[1] <= maxDer: #Derecha (+X)
        copiaPos = (pos[0],pos[1])
        palabraPos = ""
        letra = 0
        while letra < largoPalabra:
            palabraPos += tablero[copiaPos[0]][copiaPos[1]]
            copiaPos = (copiaPos[0],copiaPos[1]+1)
            letra += 1
        if palabra == palabraPos:
            listaPos = ["Horizontal","Derecha"]
            return listaPos
    if pos[0] <= maxInf and pos[1] <= maxDer: #Diagonal (+Y +X)
        copiaPos = (pos[0],pos[1])
        palabraPos = ""
        letra = 0
        while letra < largoPalabra:
            palabraPos += tablero[copiaPos[0]][copiaPos[1]]
            copiaPos = (copiaPos[0]+1,copiaPos[1]+1)
            letra += 1
        if palabra == palabraPos:
            listaPos = ["Diagonal","Descendente"]
            return listaPos
    return False

def test_checkPos():
    assert checkPos([["C","C","C","C"],["C","C","C","C"],["C","C","C","C"],["C","C","C","C"]],(0,0),"GATO") == False
    assert checkPos([["H","B","C"],["P","O","G"],["K","Z","Y"]],(0,0),"HOY") == ["Diagonal","Descendente"]
    assert checkPos([["C","A","S","A"],["A","C","A","S"],["S","A","C","A"],["A","S","A","C"]],(3,3),"CASA") == ["Vertical","Arriba"]

def encuentraPalabra(tablero,palabra):
    """
    - Representamos palabras con strings
    - encuentraPlabra : List(List(Str)) Str -> Tuple(Str,Tuple(Int,Int),Str,Str)
    - encuentraPalabra recibe un tablero y una palabra, devuelve una tupla con 4 elementos
    - El primer elemento es la palabra, el segundo es una tupla con 2 elementos Y,X que representan la coordenada inicial
    - El tercer elemento es la direccion y el cuarto el sentido
    - Ejemplos:
    - encuentraPalabra([["C","A","S","A"],["C","C","C","C"],["C","C","C","C"],["C","C","C","C"]],"CASA") => ("CASA",(0,0),"Vertical","Abajo")
    - encuentraPalabra(generaTablero(5),"PERRO") => ("PERRO",(0,0),"No","Encontrada")
    """
    for y in range(len(tablero)):
        for x in range(len(tablero[y])):
            if tablero[y][x] == palabra[0]:
                pos = (y,x)
                posPalabra = checkPos(tablero,pos,palabra)
                if type(posPalabra) == list:
                    devuelve = (palabra,pos,posPalabra[0],posPalabra[1])
                    return devuelve
    noEsta = (palabra,(0,0),"No","Encontrada")
    return noEsta

def test_encuentraPalabra():
    assert encuentraPalabra([["C","A","S","A"],["C","C","C","C"],["C","C","C","C"],["C","C","C","C"]],"CASA") == ("CASA",(0,0),"Horizontal","Derecha")
    assert encuentraPalabra(generaTablero(5),"PERRO") == ("PERRO",(0,0),"No","Encontrada")

def resuelveSopa():
    archivoSopa = open("sopagenerada.txt","r")
    archivoPalabras = open("listaPalabras.txt","r")
    tableroJunto = archivoSopa.readlines()
    palabras = archivoPalabras.readlines()
    archivoSopa.close()
    archivoPalabras.close()
    for x in range(len(palabras)):
        palabras[x] = palabras[x].rstrip() #elimina \n
    for fila in range(len(tableroJunto)):
        tableroJunto[fila] = tableroJunto[fila].rstrip() #elimina \n
    tableroSeparado = []
    for fila in tableroJunto:
        filaLista = []
        for letra in range(len(fila)):
            filaLista += [fila[letra]]
        tableroSeparado += [filaLista]
    listaencontradas = []
    for palabra in palabras:
        listaencontradas += [encuentraPalabra(tableroSeparado,palabra)]
    imprimeTablero(tableroSeparado)
    print(listaencontradas)
    return

def main():
    print("Elija una opcion:")
    print("1- Generar sopa de letras\n2- Resolver sopa automaticamente")
    eleccion = int(input(""))
    if eleccion == 1:
        h = generaSopa()
        guardado = open("sopagenerada.txt","w")
        guardaPalabra = open("listaPalabras.txt","w")
        for fila in h[0]:
            filas = ""
            for columna in fila:
                filas = filas + columna
            filas = filas + "\n"
            guardado.write(filas)
        guardado.close()
        for palabra in h[1]:
            palabra = palabra + "\n"
            guardaPalabra.write(palabra)
        guardaPalabra.close()
    elif eleccion == 2:
        resuelveSopa()
    esperar = input("") #No cierra el programa hasta oprimir ENTER
main()