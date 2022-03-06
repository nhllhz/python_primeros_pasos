"""
Autor: Nahuel Lahoz

Fecha: 10/9/2020

Materia: TP1 - Programacion I
"""
#el usuario debe ingresar un número entero y el programa debe informar si está comprendido entre 0 y 10.

A= int(input("Ingrese un numero: "))

if A >= 0 and A <= 10:
    print ("El numero ingresado está comprendido entre 0 y 10")
else:
    print ("El numero ingresado no está comprendido entre 0 y 10")