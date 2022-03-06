"""
Autor: Nahuel Lahoz

Fecha: 10/9/2020

Materia: TP1 - Programacion I
"""
#el usuario debe ingresar dos números, el programa debe indicar cuál es el menor.

A= int(input("Ingrese un numero: "))

B= int(input("Ingrese otro numero: "))

if A < B:
    print ("El primer numero es menor que el segundo")
else:
    print("El segundo numero es menor que el primero")