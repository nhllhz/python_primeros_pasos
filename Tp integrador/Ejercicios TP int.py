# -*- coding: utf-8 -*-
"""
Created on Sep 23 10:25:15 2020

@author: Nahuel Lahoz

Ejercicios tp integrador

"""



#Inicio del programa
print ("En este programa puedes hacer las siguientes operaciones:")
print ("1 - Conocer cuál es el menor de tres números. ")
print("2 - Conocer cuál es el tipo de triángulo.")
print ("3 - Conocer cuántas vocales tiene una oración.")
print ("4 - Conocer si una palabra es un palíndromo.")

print (" ")

a=int( input("Ingresa el número que corresponde a tu elección:"))


# Espacio de funciones

print (" ")

def DescubrirMenor(A, B, C):

    if A < B and A < C:
        print (A)

    elif B < A and B < C:
        print (B)

    elif C < A and C < B:
        print (C)

    elif A==B and A < C:
        print (A)

    elif A==C and A < B:
        print (A)

    elif C==B and C < A:
        print (C)





def TipoDeTriangulo(An1, An2, An3):




    if An1 + An2 + An3 == 180:
        print("Los angulos corresponden a un triangulo")

        if An1 > 90:
            print("Es obtusángulo")

        elif An2  > 90:
            print("Es obtusángulo")

        elif An3 > 90:
            print("Es obtusángulo")

        elif An1 == 90:
            print("Es un triangulo rectangulo")

        elif An2  == 90:
            print("Es un triangulo rectangulo")

        elif An3 == 90:
            print("Es un triangulo rectangulo")

        elif An1 and An2 and An3 < 90:
            print("Es un triangulo acutangulo")

 
    else:
        print("los angulos no suman 180, por ende no corresponden a un triangulo")




def ContarVocales(A):

    cont=0
        
    for caracter in A:
        if caracter in 'aeiouAEIOU':
            
            cont=cont+1

        print(f'Hay:',cont,'vocales en: ', A)
            
    return cont #no se que retornar aca o como hacer para que no se impriman cada vez que pasa por el for y solo se imprima el final
        
   





def EsPalindromo(a):
    
    
    if a == a[::-1]:

        print ("TRUE")

    else:

        print("FALSE")

    return a



# Llamada las funciones

if a == 1:

    print ("Ingrese tres numeros")

    print (" ")

    A = int( input("Ingrese el primer número: "))

    B= int( input("Ingrese el segundo número: "))

    C = int( input("Ingrese el tercer número: "))

    DescubrirMenor(A,B, C)

elif a == 2:


    print ("Ingrese las medidas de cada ángulo")

    print (" ")

    An1 = int( input("Ingrese el primer ángulo: "))

    An2= int( input("Ingrese el segundo ángulo: "))

    An3 = int( input("Ingrese el tercer ángulo: "))

    TipoDeTriangulo(An1, An2, An3)

elif a== 3:

    print ("Ingrese una palabra u oración ")

    print (" ")

    A = input("Ingresela aquí: ")
    
    
    ContarVocales(A)

    



elif a== 4:

    a= input("Ingrese aquí una palabra para saber si es palindromo: ")

    print(EsPalindromo(a))

    

else: 

    print ("Esa opción no está disponible")





