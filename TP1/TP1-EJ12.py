"""
Autor: Nahuel Lahoz

Fecha: 10/9/2020

Materia: TP1 - Programacion I
"""

#el usuario debe ingresar las tres medidas de los lados de un triángulo, el programa deberá:
6.#	Verificar que corresponden a un triángulo. Para eso la suma de dos lados debe ser mayor al lado restante.
7.#	Informar que tipo de triángulo es:
8.#	Equilátero: los tres lados iguales.
9.#	Isósceles: dos lados iguales y uno diferente.
10.#	Escaleno: los tres lados diferentes.


An1= int(input("Ingrese medida de lado1: "))

An2= int(input("Ingrese medida de lado2: "))

An3= int(input("Ingrese medida de lado3: "))

if An1 + An2 > An3 or An1 + An3 > An2 or An2 + An3 > An1:
    print("Correspoden a un triangulo")

if An1 == An2 and An2== An3:
    print("Es equilatero")

elif An1 == An2 and An2 != An3 or An1 == An3 and An3 != An2 or An2 == An3 and An3 != An1:
    print ("Es isosceles")

elif An1 != An2 and An2  != An3 and An1  != An3: 
    print ("Es escaleno")

    