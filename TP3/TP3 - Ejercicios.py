"""
Autor: Nahuel Lahoz

Fecha: 19/9/2020

Materia: TP3 - Programacion I
"""
#zona de import





#Espacio de funciones


def suma(a,b): #Ejercicio 1

    resultado = a+b

    return resultado




def resta(e,l):  #Ejercicio 2

    if e > l:

        res1 = e-l

        print (res1)

        return res1

    else: 

        res2 = l-e

        print (res2)

        return res2
    



def producto(t,p): #Ejercicio 3

    resprod = t*p

    print (resprod)

    return resprod
    


def max(m,n): #Ejercicio 4

    if m > n:

        print (m)

        return m

    else:

        print (n)

        return n



    
def min(p,q): #Ejercicio 5

    if p > q:

        print (q)

        return q

    else:

        print (p)

        return p





def max_de_tres(a,b,c): #Ejercicio 6

    if a > b and c:

        print (a)

        return a

    elif b > a and c:

        print (b)

        return b

    else:

        print (c)

        return c



def vocalono(): #Ejercicio 7

    A= input("Ingrese un caracter: ")

    print (" ")
    
    
    
    if A == "a":

        print ("TRUE")


    elif A == "e":

        print ("TRUE")

    elif A == "i":

        print ("TRUE")

    elif A == "o":

        print ("TRUE")

    elif A == "u":

        print ("TRUE")
    
    else: 

        print ("FALSE") 



def inversa(a): #Ejercicio 8
    

    return a[::-1]






def es_palindromo(a): #Ejercicio 9 --- Profe en este ejercicio no entiendo donde iria el return
    
    
    if a == a[::-1]:

        print ("TRUE")

    else:

        print("FALSE")

    return a






def longitudCadena(x): #Ejercicio 10
    contador=0
    for i in x:
      contador +=1
    return contador

#Definir una función superposicion() que tome cadenas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario.
# Escribir la función usando el bucle for anidado. 

"""
def suporposicion(a): #No me salio el ejercico 11

    for x in a[:]:

        for j in x[:]:

            if x == j:

                print ("TRUE")

            else: 
                
                print ("False")

"""      




def generar_n_caracteres(a ): #Ejercicio 12

    c= a * "x"

    return c








# Espacio de llamada a funciones

#Sacar el numeral "#" para hacerlas funcionar

#suma(3,6)

#resta(5, 9)

#producto(5, 3)

#max(134, 67)

#min(123, 122)

#max_de_tres(14,23, 5)

#vocalono()

#print(inversa("paragua"))

es_palindromo("neuquen")

#print("Longitud de cadena:", longitudCadena("cadena"))

#suporposicion("mona")

#print (generar_n_caracteres(6))