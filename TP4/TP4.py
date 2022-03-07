"""

Autor: Nahuel Lahoz

TP4

"""
"""
Se necesita un programa que genere un listado de todos los mozos con los siguientes datos: 
nombre del mozo, categoría, importe a cobrar por la comisión de la venta. 

"""
#### Sector de procedimientos  #####

def DatosMozos():

    archivo = open ("C:\Mozos.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    for x in Lector:

        x = x.replace("\n", "")

        datos = x.split (";")

        importe = float(datos[3] )* float(datos[4])/100

        
        print(datos[1] + " - " + datos[2] + " - " + str(importe))
        


    



"""
Se necesita un programa que genere un listado de los mozos que correspondan a una categoría en particular, indicada por el usuario.
"""


def ListadoMozos ():

    print ("Existen las siguientes categorias:")
    print ("1. Juniors")
    print ("2. Master")
    print ("3. Experto")
    print("")

    usuario = input ("Ingrese la categoria que quiere ver: ")

    archivo=  open ("C:\Mozos.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()
    
    for x in Lector:

        datos = x.split (";")

        if usuario == datos [2]:

            print (datos [1])
    




""""
Se necesita un programa que genere un archivo con extensión CSV de todos los mozos con los siguientes datos: 
nombre del mozo, categoría, importe a cobrar por la comisión de la venta.

"""



def archivoMozo():

    
    archivo = open ("C:\Mozos.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    Nuevo_archivo = open ("EjNahuel", "tw")


   
    for x in Lector:

        x = x.replace("\n", "")

        datos = x.split (";")

        importe = float(datos[3] )* float(datos[4])/100

        
        Nuevo_archivo.write (datos[1] + " - " + datos[2] + " - " + str(importe) + "\n")

    Nuevo_archivo.close()



"""
programa que genere un archivo con extensión CSV de los mozos que correspondan a una categoría en particular, indicada por el usuario

"""

def ArchiUsuario():

    print ("Existen las siguientes categorias:")
    print ("1. Juniors")
    print ("2. Master")
    print ("3. Experto")
    print("")

    usuario = input ("Ingrese la categoria que quiere ver: ")

    archivo = open ("C:\Mozos.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    Nuevo_archivo = open ("Archivo2tp4", "tw")

    for x in Lector:

        datos = x.split (";")

        if usuario == datos [2]:

           Nuevo_archivo.write (datos [1])

    Nuevo_archivo.close()


"""
Se necesita un programa que muestre el total de las ventas.

"""

def TotalVentas():

    archivo = open ("C:\Mozos.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    contador = 0

    for x in Lector:

        x = x.replace("\n", "")

        datos = x.split (";")

        contador = contador + int(datos [4])

    print (contador)


"""

Se necesita un programa que muestre el promedio de las ventas.

"""

def PromedioVentas():


    archivo = open ("C:\Mozos.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    contador = 0

    empleados = 0

    for x in Lector:

        x = x.replace("\n", "")

        datos = x.split (";")

        contador = contador + int(datos [4])

        empleados = empleados + 1

        promedio = contador / empleados
    
    print ("En promedio, cada vendedor ha vendido:", promedio)



"""

Se necesita un programa que muestre el nombre del mozo que logró la mayor venta.

"""


def MayorVenta():

    archivo = open ("C:\Mozos.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    contador = 0

    vendedor = ""
    
    for x in Lector:

        x = x.replace("\n", "")

        datos = x.split (";")

        if (float (datos [4]) > contador):

            contador = float(datos[4])
            vendedor= datos[1]
                
            
    print ("El vendedor con mayor ventas es", vendedor)


"""

•	Se necesita un programa que muestre el total a pagar por comisiones de ventas

"""

def comisiones():

    archivo = open ("C:\Mozos.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()
    
    total = 0

    for x in Lector:

        x = x.replace("\n", "")

        datos = x.split (";")

        importe = float(datos[3] )* float(datos[4])/100

        total = total + importe

    print ("El importe total a pagar de comisiones es de: ", total)


"""

•	Se necesita un programa que muestre el promedio a pagar por comisiones de ventas.

"""

def PromedioComisiones():

    archivo = open ("C:\Mozos.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()
    
    total = 0

    vendedores = 0

    for x in Lector:

        x = x.replace("\n", "")

        datos = x.split (";")

        importe = float(datos[3] )* float(datos[4])/100

        total = total + importe

        vendedores = vendedores + 1

        promedio = total / vendedores #Ahi solucione la variable vendedores, es incremental con el for, a medida que va entrando en cada linea suma uno

    print ("El importe del promedio de comisiones es de: ", promedio)


"""

•	Se necesita un programa que muestre el mayor importe a pagar por comisiones de ventas

"""


def MayorComision():

    archivo = open ("C:\Mozos.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    contador = 0

    
    for x in Lector:

        x = x.replace("\n", "")

        datos = x.split (";")

        importe = float(datos[3] )* float(datos[4])/100

        if importe > contador:

            contador = importe
                
            
    print ("El mayor importe a pagar por comision de venta es de: ", contador)





#### Sector de llamado a los procedimientos #####

#DatosMozos()

#ListadoMozos()

#archivoMozo()

#ArchiUsuario()

#TotalVentas()

PromedioVentas()

#MayorVenta()

#comisiones()

#PromedioComisiones()

#MayorComision()