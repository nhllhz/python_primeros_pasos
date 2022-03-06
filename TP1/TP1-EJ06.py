"""
Autor: Nahuel Lahoz

Fecha: 10/9/2020

Materia: TP1 - Programacion I
"""
#el usuario debe ingresar el importe de una compra que quiere realizar e informar si la misma es de contado, 
# tarjeta de crédito, cheque o cuenta corriente. El programa deberá mostrar el importe a pagar, teniendo en cuenta las siguientes reglas:
#Contado: el importe a pagar es igual al importe de venta.
#	Tarjeta de Crédito: el importe a pagar es igual al importe de venta con un aumento del 2 %.
#	Cheque: el importe a pagar es igual al importe de venta con un aumento del 3 %.
#	Cuenta Corriente: el importe a pagar es igual al importe de venta con un aumento del 1,5 %.


Importe= int(input("Ingrese importe de la compra a realizar: "))

print("Seleccione metodo de pago")

print("Si es al contado ingrese: A") 
print("si es con tarjeta de credito ingrese: B")
print("si es con cheque ingrese: C")
print("si es con cuenta corriente ingrese: D")

Apagar= input("Ingrese el método de pago: ")

la= Importe

le=  Importe + (Importe*2/100)

li= (Importe*103)/100

lo= (Importe * 101.5)/100

if Apagar == "A":
    print(la)

elif Apagar == "B":
    print (le)

elif Apagar == "C":
    print(li)

else: 
    print (lo) 
