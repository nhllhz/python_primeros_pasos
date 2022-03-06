"""
Autor: Nahuel Lahoz

Fecha: 10/9/2020

Materia: TP1 - Programacion I
"""
	#El programa deberá generar dos números aleatorios y mostrarlos en pantalla.
	#También deberá generar aleatoriamente un número comprendido entre 1 y 4. Este número determinará un operación que se deberá mostrar en la pantalla:
#	Cuando se genera un 1, se muestra el signo + (sumar).
#	Cuando se genera un 2, se muestra el signo - (restar).
#	Cuando se genera un 3, se muestra el signo * (multiplicar).
##	Cuando se genera un 4, se muestra el signo / (dividir).
	#El usuario deberá ingresar el resultado de la operación solicitada. 
    # Si es el resultado correcto el programa felicitará al usuario, de lo contrario le dirá que se equivocó y le informará el resultado correcto. 

from random import randint

a= int(randint(1,10))
print ("El primer número generado (a) es: " + str(a))

b= int(randint(1,10))
print ("El segundo número generado (b) es: " + str(b))

c= int(randint(1,4))


if c == 1:
    print ("Realice la siguiente operacion: a+b")

elif c== 2:
    print ("Realice la siguiente operacion: a-b")

elif c == 3:
    print ("Realice la siguiente operacion: a*b")

else: 

    print ("Realice la siguiente operacion: a/b")

print ("")

resultado= (input("Ingrese el resultado de la operacion solicitada: "))

if c== 1:
    
    if resultado == (a+b):
        print ("El resultado es correcto, felicitaciones!!")
    else:
        print(f"Se ha equivocado, el resultado correcto es: ", (a+b))


elif c== 2:
    
    if resultado == (a-b):
        print ("El resultado es correcto, felicitaciones!!")
    else:
        print(f"Se ha equivocado, el resultado correcto es: ", (a-b))

elif c== 3:
    
    if resultado ==  (a*b):
        print ("El resultado es correcto, felicitaciones!!")
    else:
        print(f"Se ha equivocado, el resultado correcto es: ", (a*b))

elif c== 4:
    
    if resultado == (a/b):
        print ("El resultado es correcto, felicitaciones!!")
    else:
        print(f"Se ha equivocado, el resultado correcto es: ", (a/b))

#Profe el codigo me salta al else del condicional como si se hubiese equivocado, no se porque