"""
Autor: Nahuel Lahoz

Fecha: 10/9/2020

Materia: TP1 - Programacion I
"""
#Se necesita un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.
from random import randint

a= int(randint(1,100))


N1= int(input("Ingrese un numero entero: "))

N2= int(input("Ingrese un numero entero: "))

if N1 > N2 and N2 * a == N1:
    print ("es multiplo")

elif N2 > N1 and N1 * a == N2:
    print( "Es multiplo")

else:
    print("no es multiplo")

#No me salio