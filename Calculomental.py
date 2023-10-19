"""
Created on Thu 17 Aug 15:45:01 2023
@author: Evan André Santana Pacheco A01769493
Juego calculo mental
Es un programa para practicar el calculo mental a traves de ejercicios.
"""

import random
"""
La biblioteca random que importe me permitira generar nuevos problemas bajo la
misma plantilla de ejercicios.Los numeros aleatorios se generán 
"random.randit(x,z)" donde "x" y "z" definen el rango a de donde se generan los
numeros aleatorios.
"""
def instrucciones():
    print("""
          Instrucciones:
              Tras elegir un modo de dificultad tendrá que resolver 10 
              preguntas el cual le dará un puntaje, cada pregunta bien resuelta
              le dará 10 puntos, cada error le restara 10 untos.
              Puede elegir volver a correr el codigo para practicar.
              Cúando se obtenga una respuesta con multiples decimales escriba
              hasta 2 decimales, no redondee.
          """)
    print("Existen diversos modos de entrenamiento")
    matriz = [["facil ", 1], 
              ["medio ", 2],
              ["dificil ", 3],
              ["infinito ", 4],
              ["multijugador ", 5]]
    for nivel in matriz:
        print(f"{nivel[0]}\t{nivel[1]}")
        
        """
        Estás es solo la explicacion y no tiene ninguna otra funcion mas que un
        apoyo visual para que el usuario comprenda como usar el programa,
        la matriz es simplemente una lista para mostrar un "menu" de los
        diferentes niveles.
        """
        

puntaje = 0

def comprobacion(resultado, puntaje, resultado_u):
    """
    Este función tiene el proposito de llevar el puntaje, comprueba si el
    resultado escrito por el usuario "resultado_u" es igual al resultado del
    ejercicio, si es correcto se le suman 10 puntos, si no se le restan 10
    puntos al puntaje el puntaje comienza en 0, como uso el puntaje en otras
    partes del programa me convenía marcarlo como una variable global.
    """
    if resultado == resultado_u:
        puntaje = puntaje + 10
        print("correcto")
        print("tu puntaje es", puntaje)
        return puntaje
    else:
        print("resultado correcto",resultado)
        puntaje = puntaje - 10
        print("tu puntaje es", puntaje)
        return puntaje
    
    

def nivel1():
    """
    la funcion Nivel 1 ya tiene consigo una plantilla, genera numeros
    aleatorios y los asigna al espacio de la plantilla de tal forma que
    se tiene un string que es el que se imprime para que el usuario lo vea y
    tambien se genera una variable que es tal cual el calculo al ejercicio y
    se guarda en la variable resultado.
    """
    num = random.randint(1, 30)
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    num3 = random.randint(1, 30)
    num4 = random.randint(1, 30)
    print( num, "+", num1, "+", num2, "+", num3, "-", num4)
    resultado = num + num1 + num2 + num3 - num4
    return resultado


def nivel2(): 
    """
    Misma idea que la funcion 1 con la diferencia que los numeros que genera y
    se guardan tienen un rango distinto, esto con la idea de que al tener en la 
    plantilla operaciones como multiplicaciones se necesitan numeros más chicos 
    para evitar que el calculo sea muy complejo, el procedimiento es el mismo.
    """
    num = random.randint(5, 10)
    num1 = random.randint(5, 10)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    print("(", num, "*", num1, ")", "-", "(", num2, "*", num3, ")")
    resultado = (num * num1) - (num2 * num3)
    return resultado

def decimales(resultado):
    """
    Esta funcion me permite truncar decimales y tonabdo solo los primeros dos
    sin redondear, recibe el resultado con decimales, lo multiplica por 100 y
    despues lo modifico a un int de forma que eliminará los decimales
    restantes, por ultimo lo divido otra vez entre 100 para que regrese el
    resultado correcto.
    """
    correcto = resultado * 100
    decimales  = int(correcto)
    decimales = decimales / 100
    return decimales

def nivel3():
    """
    Es la misma idea pero aqui al tener divisiones que puedan tener residuos
    mando llamar la funcion decimales
    """
    num = random.randint(5, 10)
    num1 = random.randint(1, 5)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    print("(", num, "/", num1, ")", "+", "(", num2, "*", num3, ")")
    resultado = (num / num1) + (num2 * num3)
    resultado = decimales(resultado)
    return resultado



def infinito():
    """
    Es exactamente la misma funcion que el nivel1 con la diferencia que queria
    un mayor rango de numeros, de 1 a 100, para ser infinito cuando se mande
    llamar esta funcion entrára un ciclo hasta tener una respuesta incorrecta.
    """
    num = random.randint(1, 100)
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    num4 = random.randint(1, 100)
    print(num,  "+",  num1 , "-",  num2,  "+",  num3,  "+" , num4)
    resultado = num + num1 - num2 + num3 + num4
    return resultado

def multijugador(puntaje):
    """
    Esta funcion genera el juego multijugador, tiene una matriz base para que
    sea llenada por el usuario. Recibe del usuario un rango para definir el
    numero de jugadores y hace un ciclo para que tras escribir el nombre del
    jugador, corran las funciones nivel1 (que pone los ejercicios),
    comprobacion (da el puntaje) y tras recibir el puntaje lo anida a
    la primera posicion que es el primer jugador y reinicia el puntaje a 0
    listo para que el siguiente jugador juege hasta que se haya alcanzado el
    numero de jugadores deseados. El segundo ciclo while funciona para definir
    que el nivel1 seran 10 ejercicios.
    """
    tamaño = int(input("Ingrese el número de jugadores: "))
    matriz = []

    for i in range(tamaño):
        matriz.append([])
        nombre = str(input("Ingrese nombre del jugador: "))
        matriz[i].append(nombre)

        cont = 0
        while cont < 10:
            resultado = nivel1()  
            resultado_u = float(input("Resuelva: "))
            puntaje = comprobacion(resultado, puntaje, resultado_u)
            print("Siguiente ejercicio")
            cont = cont +  1

        if puntaje == 100:
            print("Puntaje perfecto!!!, sigue practicando", puntaje)
        else:
            print("Puntaje final para", nombre, "es", puntaje)
            matriz[i].append(puntaje)
        puntaje = 0

    return matriz



instrucciones()

nivel = int(input("seleccione nivel: "))

"""
Aqui el jugador elige alguna de las opciones y debajo comenzará a comparar cual
ocpion eleigio para que corra el juego.
"""

if nivel == 1:
    ejercicio = 0
    while ejercicio < 10:
        ejercicio = ejercicio + 1
        resultado = nivel1()
        resultado_u = float(input("resuelva "))
        puntaje = comprobacion(resultado, puntaje, resultado_u)
        print("siguiente ejercicio")
    if puntaje == 100 :
        print("puntaje perfecto!!!, sigue practicando", puntaje)
    else:
        print("puntaje final", puntaje)
       
elif nivel == 2:
    ejercicio = 0
    while ejercicio < 10:
        ejercicio = ejercicio + 1
        resultado = nivel2()
        resultado_u = float(input("resuelva "))
        puntaje = comprobacion(resultado, puntaje, resultado_u)
        print("siguiente ejercicio")
    if puntaje == 100 :
        print("puntaje perfecto!!!, sigue practicando", puntaje)
    else:
        print("puntaje final", puntaje)     
        
elif nivel == 3:
    ejercicio = 0
    while ejercicio < 10:
        ejercicio = ejercicio + 1
        resultado = nivel3()
        resultado_u = float(input("resuelva "))
        puntaje = comprobacion(resultado, puntaje, resultado_u)
        print("siguiente ejercicio")
    if puntaje == 100 :
        print("puntaje perfecto!!!, sigue practicando", puntaje)
    else:
        print("puntaje final", puntaje)  
        
elif nivel == 4:
    resultado = infinito()
    resultado_u = float(input("resuelva "))
    puntaje = comprobacion(resultado, puntaje, resultado_u)
    while resultado_u == resultado:
        resultado_u = float(input("resuelva "))
        resultado = infinito()
        puntaje = comprobacion(resultado, puntaje, resultado_u)
        
elif nivel == 5:
    puntaje_inicial = 0
    resultado_matriz = multijugador(puntaje_inicial)
    print("Matriz de resultados:", resultado_matriz)
    
else: 
    print("Entrada no valida")

"""Este es el juego como tal donde manda llamar las funciones niveles y la 
comprobacion, aqui en el juego es donde entra en ciclo para definir el numero
de ejercicios y durante este ciclo despliega las funciones, cuando termina se
muestra un mansaje marcando el puntaje final.
La unica diferencia son en las ultimas 3 opciones que el nivel4 no necesita 
mensajes finales pues es el modo infinito, el nivel 5 es el multijugador
que ya integra el sistema de matriz y solo manda imprimir la matriz final que
tiene nombres y puntajes anidados, por ultimo un else que es si se equivoca el
usuario y elije otra opcion que no esta definida en el programa.
"""