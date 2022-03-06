"""
Autor: Nahuel Lahoz

Fecha: 10/9/2020

Materia: TP1 - Programacion I
"""

#el usuario debe ingresar las tres medidas de los ángulos de un triángulo, el programa deberá:
1#	Verificar que corresponden a un triángulo. Para eso la suma de los tres ángulos debe ser igual a 180 grados.
2.#	Informar que tipo de triángulo es:
3.#	Obtusángulos: uno de los ángulos es mayor a 90 grados.
4.#	Rectángulo: uno de los ángulos es igual a 90 grados.
5.#	Acutángulo: los tres ángulos son menores a 90 grados.

An1= int(input("Ingrese medida de angulo1: "))

An2= int(input("Ingrese medida de angulo2: "))

An3= int(input("Ingrese medida de angulo3: "))

if An1 + An2 + An3 == 180:
    print("Los angulos corresponden a un triangulo")

    if An1 or An2 or An3 > 90:
        print ("Es obstusangulo")
    
    elif An1 or An2 or An3 == 90:
        print ("Es rectangulo")

    elif An1 and An2 and An3 < 90:
        print ("Es acutángulo")

else:
    print("los angulos no suman 180, por ende no corresponden a un triangulo")

#No saleS