#Mi Estado inicial es la libreria de ejercicos
#Mi estado inicial son los resultados del usuario
#Mi estado final es que verifique si es cierto o no

puntaje = 100 
#El puntaje se le sumaria o restaria si esta bien
# o mal la pregunt, es una variable que se actualizara
# durante todo el programa

resultado_c1= 24 + 39 - 11 + 62 - 49
resultado_c2= 25 * 5 + 15 * 2
resultado_c3= 35 / 5 - 2 * 10 + 13 / 9

ejercicio_1= str("24 + 39 - 11 + 62 - 49")
ejercicio_2= str("25 * 5 + 15 * 2")
ejercicio_3= str("35 / 5 - 2 * 10 + 13 / 9")

#Aqui esta mi biblioteca de resultados y strings  
 
print(ejercicio_1)
resultado_u1 = float(input("resuelva"))

#aqui se muestra el string y el espacio a resolver

if resultado_u1 == resultado_c1:
	 print("correcto")
	 puntaje = puntaje + 10
	 print("puntaje:",puntaje) 

#Por error de sintaxis lo escribi con dos simbolos ==
else:
	 print("resultado correcto",resultado_c1) 
	 puntaje = puntaje -10
	 print("puntaje:",puntaje)

#Si se tiene mal aparacera correcto y si no mostrara el resultado correcto

#Este procedimiento para el resto de los ejercicios

print(ejercicio_2)
resultado_u2 = float(input("resuelva"))

if resultado_u2 == resultado_c2:
	 print("correcto")
	 puntaje = puntaje + 10
	 print("puntaje:",puntaje) 
else:
	print("resultado correcto",resultado_c2)
	puntaje = puntaje -10
	print("puntaje:",puntaje)

#Aqui el resultado correcto aparece como 155 por la jeraquia en python
#La idea es que los numeros en el programa final vayan apareciendo en orden para hacer operaciones
#De modo que se leeria de izquierda a derecha paso por paso, estoy investigando como resolver esto

print(ejercicio_3)
resultado_u3 = float(input("resuelva"))

if resultado_u3 == resultado_c3:
	 print("correcto")
	 puntaje = puntaje + 10
	 print("puntaje:",puntaje) 
else:
	 print("resultado correcto",resultado_c3)
	 puntaje = puntaje -10
	 print("puntaje:",puntaje)


#Por las mismas razones del orden de jerarquía el resultado fue -11.55
#Mientras que si se leyera de izuierda a derecha el resultado que se buscaba era 7
#Por diseño una vez resuelva este problema no habra numeros decimales ya que el 
#Calculo mental no se practica con puntos decimales dejando todas las variables en 
#Int, enteros




