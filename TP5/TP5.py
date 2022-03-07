"""

Autor: Nahuel Lahoz

TP5

"""
#####   Llamada a importaciones #####
import random

#Inicio archivo

def JuegoPreguntados():

    archivo = open ("C:\Preguntas.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()
    
    contador = 0 

    contador2= 0

    print ("COMIENZA EL JUEGO!!!!\n")

    print ("Si contesta 5 veces bien ganará; si se equivoca 3 veces perderá\n")



    for x in Lector:

        aleatorio = random.choice (Lector)

        fila = aleatorio.replace("\n", "")

        datos = fila.split (";")

# Visualizacion usuario        

        
        
        print (datos[0])

        print ("1. ",  datos[1])

        print ("2. ", datos[2])

        print ("3. ", datos[3])

        print ("4. ", datos[4])

        usuario = input("Ingrese su respuesta: ")

        print ("")


#Logica del juego

        if usuario == datos[5]:

            contador = contador + 1

            print("Aciertos: ", contador)

            print("Errores: ", contador2)

            print ("")

            if contador == 5:

                print ("HA GANADOOO!!!!!" )

                break

            
        else: 

            contador2 = contador2 + 1

            print("Aciertos: ", contador)

            print("Errores: ", contador2)

            print ("")

            if contador2 == 3:

                print ("Oh! Ha perdido, vuelva a intentarlo" )

                break

    print ("El juego termino.")  

            

            
            







#LLamada procedimiento

JuegoPreguntados()