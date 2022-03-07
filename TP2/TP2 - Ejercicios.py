"""
Autor: Nahuel Lahoz

Fecha: 17/9/2020

Materia: TP1 - Programacion I
"""
from random import randint 


# Espacio de funciones

def UnDado(): # Funcion Ejercicio 1

    a= randint (1,6)
    b= randint (1,6)
    Alvaro = print ("El jugador Alvaro tiró el dado y salio: ", a )
    print (" ")
    Barbara = print ("La jugadora Barbara tiró el dado y salio", b)

    print (" ")
    if a > b:
        print ("Alvaro ha ganado")
    
    elif a == b: 

        print ("Han empatado")
    
    else:
        print ("Barbara ha ganado")




def DosDados(): #Ejercicio 2

    a= randint (1,6)
    b= randint (1,6)
    c= (a+b)

    x= randint (1,6)
    y= randint (1,6)
    z=x+y

    Carmen= print (f"Carmen tiró los dados y salio:  {a} y  {b} --  Ambos dan un total de  {c}"  )
    print (" ")
    David = print (f"David tiró los dados y salio:  {x} y  {y} --  Ambos dan un total de  {z}" )

    print (" ")

    if c > z: #Cuando el resultado es mayor
        print("Carmen ha ganado")
    
    elif c == z: #cuando es igual, pasa a cada dado y verifica cual es el mayor o si empatan
        
        if a > b and a == x and x > y:

            print ("Han empatado")
        
        elif b > a and b == x and x > y:

            print ("Han empatado")

        elif a > b and a == y and y > x:

            print ("Han empatado")
        
        elif b > a and b == y and y > x:

            print ("Han empatado")

        elif a or b < x or y:

            print ("David ha ganado")

        elif a or b > x or y:

            print ("Carmen ha ganado") 
    
    else:
        print ("David ha ganado")


def PiPaTi(): #Ejercicio 3 piedra papel o tijera

    A= randint (1,3)
    B= randint (1,3)

#Jugada jugador 1
    if A == 1:
        a = "piedra"
    elif A == 2:
        a =  "papel"
    
    elif A == 3:

        a = "tijera"

#Jugada jugador 2

    if B == 1:
        b = "piedra"
    elif B == 2:
        b =  "papel"
    
    elif B == 3:

        b = "tijera"

    # Jugadores
    Juan = print ("El jugador Juan ha sacado: ", a)
    
    print (" ")
    
    Ines = print ("La jugadora Ines ha sacado: ", b)

    print (" ")

#Reglas

    if A == 1 and B == 3:
        print ("Juan ha ganado")
    
    elif A == 3 and B== 2:
        print ("Juan ha ganado")
    
    elif A==2 and B == 1:
        print ("Juan ha ganado")
    
    elif A == B:
        print ("Empate")
    
    else:
        print ("Ines ha ganado")



def ej4(): #Ejercicio 4

    A= int(input("Ingrese un numero: "))
    
    print (" ")

    B= int(input("Ingrese un numero: "))

    print (" ")

    print ("El numero mayor es:")

    if A > B:
        print (A)

    else:
        print (B)


def ejer5():

    A= int(input("Ingrese un numero: "))
    
    print (" ")

    B= int(input("Ingrese un numero: "))

    print (" ")


    C= int(input("Ingrese un numero: "))

    print (" ")

    print ("El numero mayor es:")

    if A > B and C:
        print (A)

    elif B > A and C:
        print (B)

    elif C > A and B:
        print (C)

    elif A==B and A > C:
        print (A)

    elif A==C and A > B:
        print (A)

    elif C==B and C > A:
        print (C)
    


#Escribir un programa que tome un carácter e informe si es una vocal o no lo es

def ejer6(): #Ejercicio 6

    A= input("Ingrese un caracater: ")

      

    if A == "a":

        print ("El caracter ingresado es una vocal")

    elif A == "e":

        print ("El caracter ingresado es una vocal")

    elif A == "i":

        print ("El caracter ingresado es una vocal")

    elif A == "o":

        print ("El caracter ingresado es una vocal")

    elif A == "u":

        print ("El caracter ingresado es una vocal")
    
    else: 

        print ("El caracter ingresado no es una vocal")



def UnoaCien():  

    x= 1

    while x <= 100:
        
        print (x)

        x=x+1 






def Ejer8():


    for x in range (101):
        print (x)


 


def CuentaLetras(): #Actividad 9

    A= input("Ingrese una palabra: ")

    print ("  ")

    print (len(A))




def LetraxLetra(): #Actividad 10

    A= input("Ingrese una palabra: ")

    print ("  ")

    for x in A:
        print (x)




def ej11():

    A= input("Ingrese una palabra: ")

    print ("  ")

    for x in A:
        print ("Dame una: ", x)

    print (A)




def SumaLista(): #Ejerccio 12

    total= 0

    for x in [1,2,3,5,9,4]:
        
        total = total + x

        print (total)



def MultiplicarLista(): #Ejercicio 13
    
    total= 1

    for x in [2,2,3]:
        
        total = total * x

        print (total)





def ejer14():  #Ejercicio 14

    n= int(input("Ingrese un numero: "))

    print(n * " * ")







def Mostrador(): #Ejercio 15

    n= int(input("Ingrese un numero: "))

    print("  ")

    c= input("Ingrese el caracter a mostrar: ")

    print("  ")

    print(n * c)




def ListShow(): #Ultimo Ejercicio

    a =[2, 4, 6]

    print (a[0] * " * ")

    print (a[1] * " * ")

    print (a[2] * " * ")








    


# Espacio de llamada a funciones

#Sacar el numeral "#" para hacerlas funcionar


#UnDado()
#DosDados()
#PiPaTi()
#ej4()
#ejer5()
#jer6()
UnoaCien()
#Ejer8()
#CuentaLetras()
#LetraxLetra()
#ej11()
#SumaLista()
#MultiplicarLista()
#ejer14()
#Mostrador()
#ListShow()