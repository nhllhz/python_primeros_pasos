"""
Autor: Nahuel Lahoz

Fecha: 10/9/2020

Materia: TP1 - Programacion I
"""

#el usuario debe ingresar las tres medidas de los ángulos de un triángulo, 
# el programa deberá informar si es obtusángulo, para lo que es necesario verificar si uno de los ángulos es mayor a 90 grados.

An1= int(input("Ingrese medida de ángulo 1: "))

An2= int(input("Ingrese medida de ángulo 2: "))

An3= int(input("Ingrese medida de ángulo 3: "))

if An1 > 90:
    print("Es obtusángulo")

elif An2  > 90:
    print("Es obtusángulo")

elif An3 > 90:
    print("Es obtusángulo")

else:
    print("No es obtusángulo")