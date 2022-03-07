# -*- coding: utf-8 -*-
"""

@author: Nahuel Lahoz

Ejercicios parcial 1 - tema b

"""



#Inicio del programa
print ("En este programa puedes hacer las siguientes operaciones:")
print ("1 – Conocer cuántos caracteres de un tipo tiene un texto. ")
print("2 - Conocer la sumatoria de 0 hasta un número ingresado por el usuario.")
print ("3 - Conocer el precio de una entrada.")
print ("4 - Conocer cuál es la calificación cualitativa de un alumno")

print (" ")

a=int( input("Ingresa el número que corresponde a tu elección:"))

print (" ")

# Espacio de funciones

def CuentaCaracter(A, B):

    contador= 0

    for x in A:

        if x == B:

            contador = contador+1

    return (contador)


def sumatoria (n1):

    total=0

    for x in range(0,n1+1):

        total  = x + total

    return (total)




def precios(a):

    precio =""
    if a < 4:

        precio= "$25"

    elif a >= 4 and a < 18:

        precio = "$75"
    
    else:

        precio = "$100"

    return (precio)


def Notaes(a):

    calificacion= ""

    if a == 1 or a == 2 or a == 3:

        calificacion = "No satisfactorio"

    elif a == 4:

        calificacion = "Suficiente"

    elif a == 5 or a == 6:

        calificacion = "Satisfactorio"

    elif a == 7:

        calificacion ="Bueno"

    elif a == 8 or a ==9:

        calificacion= "Muy bueno"
    
    elif a == 10:

        calificacion = "Excelente"

    return (calificacion)










#Espacio de procedimientos

def ContarCaracter ():

    A = input("Ingrese una frase: ")

    B= input("Ingrese un caracter: ")

    print ("La frase tiene", CuentaCaracter(A, B), "caracteres del elegido"  )

    

def CalcularSumatoria():

    n1 = int( input("Ingrese un numero entre 0 y 10: "))

    print ("La suma de 0 al numero ingresado da: ", sumatoria (n1))





def ConsultarPrecio():

    edad = int(input("Ingrese su edad: "))

    print ("El precio de su entrada es", precios(edad) )



def CalificarAlumno():

    nota =int(input("Ingrese una nota entre 1 y 10: "))

    print("La calificacion cualitativa correspondiente es:", Notaes(nota))






# Llamada las funciones

if a == 1:

    ContarCaracter ()

elif a == 2:

    CalcularSumatoria()

elif a== 3:

    ConsultarPrecio()

    
elif a== 4:

    CalificarAlumno()

    
else: 

    print ("Esa opción no está disponible")
 


