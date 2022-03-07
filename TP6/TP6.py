"""

Autor: Nahuel Lahoz

TP6  - Programacion IA

"""


"""
Se necesita un programa que genere un listado en pantalla con los siguientes datos: 
nombre del empleado, categoría, sueldo básico, adicional por antigüedad, presentismo y total. 

o	El adicional por antigüedad es igual al sueldo básico por el 1.2% por cada año de antigüedad. Ej: (Básico * Antigüedad * 1.2 / 100)
o	El presentismo es el 8.35% de la suma del básico más el adicional por antigüedad. Ej: (básico + antigüedad) * 8.35 / 100
o	Total a Cobrar: es la suma de básico, antigüedad y presentismo

"""

def ListadoPantalla():

    archivo = open ("C:\DatosPrograma.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    adicional = float (0)

    Basico = float (0)

    Presentismo= float (0)

    Total = float (0)

    for x in Lector:

        fila = x.replace("\n", "")

        datos = fila.split (";")

        Basico = float(datos [6])

        adicional = Basico * (float(datos [5])* 1.2/100)

        Presentismo = (Basico + adicional) * 8.35/100

        Total = Basico + adicional + Presentismo

        print (datos [1].ljust(25, " ") + datos[2].ljust(25, " ") +

            format(Basico, ".2f").rjust(12 , " ") + 

            format(adicional, " .2f").rjust(12 , " ") + 

            format(Presentismo, ".2f").rjust(12 , " ") + 

            format(Total, " .2f").rjust(12 , " "))


"""
Se necesita un programa que genere un listado de los empleados que tengan a una antigüedad mayor a un valor ingresado por el usuario. 
Se deberá mostrar: Nombre del empleado, Categoría y sueldo básico.

"""

def ListaAntig():
    
    archivo = open ("C:\DatosPrograma.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()
    
    usuario =  int(input ("Ingrese un valor de antiguedad: "))
    
    contador = 0
    
    nombre = " "
    
    categoria = " "
    
    basico = float (0)
    
    for x in Lector:
        
        fila = x.replace("\n", "")

        datos = fila.split (";")
        
        if usuario <  int(datos [5]):
                                    
            for i in datos [5]:
            
                nombre = datos [1]
            
                categoria = datos [2]
            
                basico = float(datos [6])
            
            print (nombre.ljust(20 , " "), categoria.ljust(20 , " "), format(basico, ".2f").rjust(12 , " "))


"""
Se necesita un programa que genere un archivo CSV con los siguientes datos: 
nombre del empleado, categoría, sueldo básico, adicional por antigüedad, presentismo y total. 

"""
          
def Datoscsv():

    archivo = open ("C:\DatosPrograma.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    NewArchivo = open("TP6ej3", "tw")

    adicional = float (0)

    Basico = float (0)

    Presentismo= float (0)

    Total = float (0)

    for x in Lector:

        fila = x.replace("\n", "")

        datos = fila.split (";")

        Basico = float(datos [6])

        adicional = Basico * (float(datos [5])* 1.2/100)

        Presentismo = (Basico + adicional) * 8.35/100

        Total = Basico + adicional + Presentismo

        NewArchivo.write (datos[1] + " - " + datos[2] + " - " + str(Basico)+ " - "  + str(adicional) + " - " + str(Presentismo) + " - " + str(Total) + "\n")

    NewArchivo.close()
            

"""
Se necesita un programa que genere un archivo CSV con los empleados que tengan a una categoría indicada por el usuario. 
Se deberá grabar: Nombre del empleado, Categoría y sueldo básico.

"""


def Categoriacsv():

    archivo = open ("C:\DatosPrograma.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    NewArchivo = open("Categorias", "tw")

    usuario =  input ("Ingrese una categoria: ")

    nombre = " "

    categoria = ""

    basico = float (0)

    for x in Lector:
        
        fila = x.replace("\n", "")

        datos = fila.split (";")
        
        if usuario ==  datos [2]:
                                    
            for i in datos [2]:
            
                nombre = datos [1]
            
                categoria = datos [2]
            
                basico = float(datos [6])
            
            NewArchivo.write ( nombre + "-" + categoria + "-" + str(basico) + "\n")

    NewArchivo.close()


"""
Se necesita un programa que muestre nombre del empleado, categoría, sueldo básico, adicional por antigüedad, 

presentismo y total cuando el usuario ingrese un número de legajo.

"""

def legajo():

    archivo = open ("C:\DatosPrograma.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    adicional = float (0)

    Basico = float (0)

    Presentismo= float (0)

    Total = float (0)

    usuario =  input ("Ingrese una numero de legajo: ")

    for x in Lector:

        fila = x.replace("\n", "")

        datos = fila.split (";")

        Basico = float(datos [6])

        adicional = Basico * (float(datos [5])* 1.2/100)

        Presentismo = (Basico + adicional) * 8.35/100

        Total = Basico + adicional + Presentismo

        if usuario == datos[0]:

            print (datos [1].ljust(25, " ") + datos[2].ljust(25, " ") +

            format(Basico, ".2f").rjust(12 , " ") + 

            format(adicional, " .2f").rjust(12 , " ") + 

            format(Presentismo, ".2f").rjust(12 , " ") + 

            format(Total, " .2f").rjust(12 , " "))


"""
•	Se necesita un programa que muestre la suma total de los sueldos básicos.
"""
def Suma_basicos():

    archivo = open ("C:\DatosPrograma.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    basico = float (0)

    total = float (0)

    for x in Lector:

        fila = x.replace("\n", "")

        datos = fila.split (";")

        basico = float(datos [6])

        total = total + basico

    print (f"La suma total de los sueldos basicos es de: ", total)


"""


"""


def Promedio_basicos():

    archivo = open ("C:\DatosPrograma.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    basico = float (0)

    total = float (0)

    promedio = float (0)

    empleados = 0

    for x in Lector:

        fila = x.replace("\n", "")

        datos = fila.split (";")

        basico = float(datos [6])

        total = total + basico

        empleados = empleados + 1

        promedio = total / empleados

    print (f"El pomedio de los sueldos basicos es de: ", promedio)


"""
•	Se necesita un programa que muestre la suma total a pagar por adicionales por antigüedad.
"""

def Suma_adicionales():

    archivo = open ("C:\DatosPrograma.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    basico = float (0)

    total = float (0)

    adicional = float (0)

    for x in Lector:

        fila = x.replace("\n", "")

        datos = fila.split (";")

        basico = float(datos [6])

        adicional = basico * (float(datos [5])* 1.2/100)

        total = total + adicional

    print (f"La suma total de los adicionales es de: ", total)


"""
•	Se necesita un programa que muestre el promedio de los adicionales por antigüedad.

"""


def Promedio_basicos():

    archivo = open ("C:\DatosPrograma.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    basico = float (0)

    total = float (0)

    promedio = float (0)

    empleados = 0

    adicional = float (0)

    for x in Lector:

        fila = x.replace("\n", "")

        datos = fila.split (";")

        basico = float(datos [6])

        adicional = basico * (float(datos [5])* 1.2/100)

        total = total + adicional

        empleados = empleados + 1

        promedio = total / empleados

    print (f"El pomedio de los adicionales es de: ", promedio)


"""
•	Se necesita un programa que muestre la suma total a pagar por presentismo.

"""

def Suma_presentismo():

    archivo = open ("C:\DatosPrograma.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    basico = float (0)

    total = float (0)

    presentismo = float (0)

    adicional = float (0)

    for x in Lector:

        fila = x.replace("\n", "")

        datos = fila.split (";")

        basico = float(datos [6])

        adicional = basico * (float(datos [5])* 1.2/100)

        presentismo = (basico + adicional) * 8.35/100

        total = total + presentismo

    print (f"La suma total del presentismo es de: ", total)


""""

"""

def Promedio_presentismo():

    archivo = open ("C:\DatosPrograma.csv", "tr")

    Lector = archivo.readlines()

    archivo.close()

    basico = float (0)

    total = float (0)

    presentismo = float (0)

    adicional = float (0)

    empleados = 0

    for x in Lector:

        fila = x.replace("\n", "")

        datos = fila.split (";")

        basico = float(datos [6])

        adicional = basico * (float(datos [5])* 1.2/100)

        presentismo = (basico + adicional) * 8.35/100

        total = total + presentismo

        empleados = empleados + 1

        promedio = total / empleados

    print (f"El promedio total del presentismo es de: ", promedio)






##### LLamado a funciones #####

#ListadoPantalla()

#ListaAntig()

#Datoscsv()

#Categoriacsv()

#legajo()

#Suma_basicos()

#Promedio_basicos()

#Suma_adicionales()

#Promedio_basicos()

#Suma_presentismo()

Promedio_presentismo()