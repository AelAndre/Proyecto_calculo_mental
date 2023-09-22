import random
#Aqui puse la libreria para generar numeros aleatorios para los diferentes
#niveles de dificultad, este generador de numeros aleatorios lo investigue y
#lo saque de https://j2logo.com/python/generar-numeros-aleatorios-en-python/#

puntaje = 0

nivel = int(input("niivel de dificultad 1,2 ,3 o infinito"))

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
    print( num, "+", num1, "+", num2, "+", num3, " -", num4)
    resultado = num + num1 + num2 + num3 - num4
    return resultado

    
def nivel2():
    ejercicio_1 = str("25 * 5 + 15 * 2")
    resultado = 25 * 5 + 15 * 2
    print(ejercicio_1)
    return resultado
    
def nivel3():
    ejercicio_1 = str("35 / 5 - 2 * 10 + 13 / 9")
    resultado = 35 / 5 - 2 * 10 + 13 / 9
    print(ejercicio_1)
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
# en teoria las funciones de nivel 1 nivel 2 sería generar el ejercicio
# en una version posterior no estaran estas funciones
  
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
    resultado = nivel2()
    resultado_u = float(input("resuelva "))
    puntaje = comprobacion(resultado, puntaje, resultado_u)
elif nivel == 3:
    resultado = nivel3()
    resultado_u = float(input("resuelva "))
    puntaje = comprobacion(resultado, puntaje, resultado_u)
elif nivel == 4:
    resultado = infinito()
    resultado_u = float(input("resuelva "))
    puntaje = comprobacion(resultado, puntaje, resultado_u)
    while resultado_u == resultado:
        resultado_u = float(input("resuelva "))
        resultado = infinito()
        puntaje = comprobacion(resultado, puntaje, resultado_u)
    
#Los if si funcionan, agregue el nuevo modo infinito por lo cual ya no podia
#usar else
#el ciclo while no es el más eficiente pues podría incorporar los pasos previos
# y no repetirlos fuera del ciclo, sin embargo estoy revisando mi algoritmo 
#para comprobalro, de momento funciona
    
    
#para el caso 3 sigo investigando como comparar los decimales pero si funciona   
    




    
