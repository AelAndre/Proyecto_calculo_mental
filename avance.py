
puntaje = 100

nivel = int(input("niivel de dificultad 1,2 o 3"))

def comprobacion(resultado, puntaje, resultado_u):
    if resultado == resultado_u:
        puntaje = puntaje + 10
        print("correcto")
        print(puntaje)
        return puntaje
    else:
        print("resultado correcto",resultado)
        puntaje = puntaje - 10
        print(puntaje)
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
    ejercicio_1 = str("24 + 39 - 11 + 62 - 49")
    resultado = 24 + 39 - 11 + 62 - 49
    print(ejercicio_1)
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
# en teoria las funciones de nivel 1 nivel 2 sería generar el ejercicio
# en una version posterior no estaran estas funciones
  
if nivel == 1:
    resultado = nivel1()
elif nivel == 2:
    resultado = nivel2()
else:
    resultado = nivel3()
#para el caso 3 sigo investigando como comparar los decimales pero si funciona   
    
resultado_u = float(input("resuelva "))
puntaje = comprobacion(resultado, puntaje, resultado_u)

    
