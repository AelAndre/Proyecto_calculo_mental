import random
#Aqui puse la libreria para generar numeros aleatorios para los diferentes
#niveles de dificultad, este generador de numeros aleatorios lo investigue y
#lo saque de https://j2logo.com/python/generar-numeros-aleatorios-en-python/#
def instrucciones():
    print("existen diversos modos de entrenamiento")
    matriz = [["facil ", 1], 
              ["medio ", 2],
              ["dificil ", 3],
              ["infinito ", 4],
              ["multijugador ", 5]]
    for nivel in matriz:
        print(f"{nivel[0]}\t{nivel[1]}")
#aqui puse mi primera lista en forma de matriz para demostrar este aspecto
#la verdad no se porque me imprime "none", yo solo busque como dar el espacio
# entre el nivel y el numero, el f"[]\t[]" lo saque de 
#https://es.stackoverflow.com/questions/372221/c%C3%B3mo-mostrar-una-matriz-en-python

print(instrucciones())
                    
puntaje = 0

nivel = int(input("seleccione nivel"))

def comprobacion(resultado, puntaje, resultado_u):
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
#Esta funcion la ocupare al terminar cada ejercicio

#Todavia no se como generar aleatoriamente numeros 
#para hacer una función para generar ejercicios distintos
#El estado inicial de esta funcion será indicar el nivel de dificultad
#si es 1 serán sumas si es 2 serán restaa... etc
#El estado final será arrojar la operacion con numeros aleatorios
# que se imprima y regresar resultado 
#por lo mientras yo escribire los ejercicios a mano

def nivel1():
    num = random.randint(1, 30)
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    num3 = random.randint(1, 30)
    num4 = random.randint(1, 30)
    print( num, "+", num1, "+", num2, "+", num3, "-", num4)
    resultado = num + num1 + num2 + num3 - num4
    return resultado

def nivel2():
    num = random.randint(5, 10)
    num1 = random.randint(5, 10)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    print("(", num, "*", num1, ")", "-", "(", num2, "*", num3, ")")
    resultado = (num * num1) - (num2 * num3)
    return resultado
    
def nivel3():
    num = random.randint(5, 10)
    num1 = random.randint(1, 5)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    print("(", num, "/", num1, ")", "+", "(", num2, "*", num3, ")")
    resultado = (num / num1) + (num2 * num3)
    return resultado


def infinito():
    num = random.randint(1, 100)
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    num4 = random.randint(1, 100)
    #este codigo para generar numeros enteros lo aprendi y lo obtuve de 
    #https://j2logo.com/python/generar-numeros-aleatorios-en-python/#
    print(num,  "+",  num1 , "-",  num2,  "+",  num3,  "+" , num4)
    resultado = num + num1 - num2 + num3 + num4
    return resultado

def multijugador(nivel1):
    tamaño = int(input("ingrese el numero de jugadores: "))
    matriz = []
    for i in range(tamaño):
        nombre = str(input("ingrese nombre del jugador: "))
        matriz.append(nombre)
    print("los jugadores son", matriz)
    lista_anidada = [[nombre, nivel1()] for nombre in matriz]
    print(lista_anidada)



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
#me acabo de dar cuenta que puedo hacer una funcion porque se repite el sistema 
#en los 3 niveles, lo empezaré a hacer
#tambien hay error para comparar los resultados por el numero de decimales
elif nivel == 4:
    resultado = infinito()
    resultado_u = float(input("resuelva "))
    puntaje = comprobacion(resultado, puntaje, resultado_u)
    while resultado_u == resultado:
        resultado_u = float(input("resuelva "))
        resultado = infinito()
        puntaje = comprobacion(resultado, puntaje, resultado_u)
elif nivel == 5:
    multijugador(nivel1())
    #mi matriz normal si funciona lo que estoy investigando es como anidar el 
    #puntaje y hacerlo de forma eficiente
    #estaba pensando en correr las funciones de las preguntas dentro del 
    #multijugador para evitar los errores de variabes locales en el puntaje y 
    #revolverme
    #mi matriz si funciona y funcionaria algo asi

def multijugador1():
    tamaño = int(input("ingrese el numero de jugadores: "))
    matriz = []
    for i in range(tamaño):
        nombre = str(input("ingrese nombre del jugador: "))
        matriz.append(nombre)
    print("los jugadores son", matriz)
    lista_anidada = [[nombre, i + 1] for i, nombre in enumerate(matriz)]
    print(lista_anidada)
#en vez de que se agreguen i + 1 se ira agregando el puntaje de cada jugador
multijugador1()

    




    
