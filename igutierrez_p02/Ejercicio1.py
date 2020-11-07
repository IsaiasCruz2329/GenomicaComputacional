# Escribir un programa que me permita aplicar el 10% de descuento si la compra total es mayor a $100

print("Digite el costo total de la compra:")
compra_total = int(input())

descuento = 0

if (compra_total>100):
    descuento = compra_total*.10

total_pago = compra_total - descuento

print("El total a pagar es: ", total_pago)