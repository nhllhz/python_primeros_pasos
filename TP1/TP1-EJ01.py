"""
Autor: Nahuel Lahoz

Fecha: 10/9/2020

Materia: TP1 - Programacion I
"""

#el usuario debe ingresar el precio de un producto y se deberá informar cual es el valor del IVA de un producto y su precio final.

A= int(input("Ingrese el precio del producto: "))

IVA= (A*0.21)

print(f"El IVA de su producto es $", IVA)

print (f"El precio final es: $", A+IVA)
