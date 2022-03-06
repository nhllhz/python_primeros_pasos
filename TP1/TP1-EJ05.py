"""
Autor: Nahuel Lahoz

Fecha: 10/9/2020

Materia: TP1 - Programacion I
"""
#el usuario debe ingresar un número entero y el programa debe informar si está comprendido entre 0 y 10, 
# si esta entre 11 y 20, si esta entre 21 y 30 otro mensaje, o si es mayor a 30.

A= int(input("Ingrese un numero: "))

if A >= 0 and A <= 10:
    print ("El numero ingresado está comprendido entre 0 y 10")

elif A >= 11 and A <= 20:
    print ("El numero ingresado está comprendido entre 11 y 20")

elif A >= 21 and A <= 30:
    print ("El numero ingresado está comprendido entre 21 y 30")

else:
    print ("El numero ingresado es mayor a 30")