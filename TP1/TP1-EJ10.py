"""
Autor: Nahuel Lahoz

Fecha: 10/9/2020

Materia: TP1 - Programacion I
"""

#: el usuario debe ingresar las tres medidas de los ángulos de un triángulo, 
# el programa deberá informar si es acutángulo, para lo que es necesario verificar si tres ángulos son menores a 90 grados.

An1= int(input("Ingrese medida de angulo1: "))

An2= int(input("Ingrese medida de angulo2: "))

An3= int(input("Ingrese medida de angulo3: "))

if An1 and An2 and An3 < 90:
    print("Los angulos corresponden a un triangulo acutangulo")

else:
    print("los angulos no son menores a 90, por ende no corresponden a un triangulo acutangulo")