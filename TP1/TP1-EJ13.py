"""
Autor: Nahuel Lahoz

Fecha: 10/9/2020

Materia: TP1 - Programacion I
"""

#programa que calcule el índice de masa corporal:
#	El usuario deberá ingresar el peso y la altura de un paciente y el programa deberá informar el valor de IMC y un diagnóstico.
#	El IMC se calcula del siguiente modo: IMC = Peso / (Altura * Altura)
#	El diagnóstico depende del IMC:
#	Si es menos a 20 el peso es “Muy Bajo”
#	De lo contrario, si fuese menor a 30 el peso es “Normal”
#	De lo contrario, si fuese menor a 40 el peso es “Ligero Sobrepeso”
#	De lo contrario, si fuese menor a 50 el peso es “Sobrepeso”

Peso = float (input("Ingrese peso del paciente en K.g: "))
Altura= float(input("Ingrese la altura del paciente en M.cm: "))

IMC = Peso / (Altura * Altura)

if IMC < 20:
    print("Es muy bajo")

elif IMC < 30 and IMC > 20:
    print ("Normal")

elif IMC < 40 and IMC > 30:
    print("Ligero sobrepeso")

elif IMC < 50 and IMC > 40:
    print("Sobrepeso")
