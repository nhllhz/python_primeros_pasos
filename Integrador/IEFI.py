# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:13:49 2020

@author:Nahuel Lahoz

Resolucion de la IEFI

"""

#Inicio del programa


print (" BIENVENIDO ".center(60,"="))

print ("En este programa puedes hacer las siguientes operaciones: \n") 

print ("1 – Listar los sueldos. ")

print ("2 – Calcular el promedio de los sueldos básicos.")

print ("3 – Exportar los sueldos.")

print ("4 – Consultar el aumento de sueldo de un empleado.")

usuario = int(input ("Ingresa el número que corresponde a tu elección:  "))

print ("  ")


#Funciones y procedimientos


def MostrarSueldos():

    archivo = open ("C:\IEFI.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    aumento1 = float(0)

    aumento2 = float (0)

    basico = float(0)

    for x in Lector:

        x = x.replace("\n", "")

        datos = x.split (";")

        basico = float(datos [5])

        aumento1 = basico * 12/100

        aumento2 = aumento1 * 14/100

        print (datos [1].ljust(15, " ") + datos[2].ljust(15, " ")+

        format (basico, ".2f").rjust(10, " ") +
        
        format (aumento1, ".2f").rjust(10, " ") +
        
        format (aumento2, ".2f").rjust(10, " "))




def CalcularPromedio():

    archivo = open ("C:\IEFI.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    Promedio = 0

    basico = 0

    empleados = 0


    for x in Lector:

        x = x.replace("\n", "")

        datos = x.split (";")

        basico = (basico + float(datos [5]))

        empleados = (empleados + 1)

        
        Promedio = (basico / empleados)


    return Promedio 



def ExportarSueldos():

    archivo = open ("C:\IEFI.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()
    
    Nuevo_archivo = open ("DatosExportados.csv", "tw")

    nombres= " "

    adicional= float (0)

    basico = float (0)

    total= float(0)

    for x in Lector:

        x = x.replace("\n", "")

        datos = x.split (";")

        nombres = datos [1] + ", " + datos [2]

        basico = float(datos [5])
        
        adicional = basico * (float(datos[4])*1.5/100)

        total= basico + adicional

        Nuevo_archivo.write(nombres)
        Nuevo_archivo.write(";")
        Nuevo_archivo.write(str(basico))
        Nuevo_archivo.write(";")
        Nuevo_archivo.write(str(adicional))
        Nuevo_archivo.write(";")
        Nuevo_archivo.write(str(total))
        Nuevo_archivo.write("\n")

    Nuevo_archivo.close()
    


def ConsultarUnAumentoDeSueldo(a):

    archivo = open ("C:\IEFI.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    nombres= " "

    basico = float (0)

    aumento = float (0)

    for x in Lector:

        x = x.replace("\n", "")

        datos = x.split (";")

        if a == int(datos[0]):

            nombres = datos [1] + ", " + datos [2]

            basico = float(datos [5])

            aumento = basico * 12/100

            return nombres, basico, aumento








#LLamada a funciones y procedimientos

if usuario == 1:

    MostrarSueldos()

elif usuario == 2:

    print(f"El promedio de todos los sueldos basicos es de:", format(CalcularPromedio(), " .2f").rjust(5 , " "))


elif usuario == 3:

    ExportarSueldos()

elif usuario == 4:

    usuario = int(input ("Ingrese numero de legajo: "))

    print (ConsultarUnAumentoDeSueldo(usuario))

else:

    print ("Esa opción no está disponible.")



