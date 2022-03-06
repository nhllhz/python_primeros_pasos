"""
Autor: Nahuel Lahoz

Fecha: 10/9/2020

Materia: TP1 - Programacion I
"""

#el usuario debe ingresar las tres medidas de los ángulos de un triángulo, 
#el programa deberá verificar que corresponden a un triángulo. Para eso la suma de los tres ángulos debe ser igual a 180 grados.

An1= int(input("Ingrese medida de angulo1: "))

An2= int(input("Ingrese medida de angulo2: "))

An3= int(input("Ingrese medida de angulo3: "))

if An1 + An2 + An3 == 180:
    print("Los angulos corresponden a un triangulo")

else:
    print("los angulos no suman 180, por ende no corresponden a un triangulo")
