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
#busque como dar el espacio
# entre el nivel y el numero, el f"[]\t[]" lo saque de 
#https://es.stackoverflow.com/questions/372221/c%C3%B3mo-mostrar-una-matriz-en-python

instrucciones()
                    
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

def multijugador(puntaje):
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
    puntaje_inicial = 0
    resultado_matriz = multijugador(puntaje_inicial)
    print("Matriz de resultados:", resultado_matriz)
else: 
    print("entrada no valida")




    
