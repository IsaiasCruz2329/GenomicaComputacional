# Sabiendo que la fórmula para obtener el área de un triangulo es a = (b x h)/2, donde b es la longitud de la base del triángulo, y h es su altura. Escribir un programa que permita realizar el cálculo del área de un triángulo. Si el área contiene valores decimales, imprimir el resultado con dos dígitos. 
import math

print("Introducir la base del triangulo: ")
base = float(input())

print("Introducir la altura del triangulo: ")
altura = float(input())

area_triangulo = (altura*base)/2

parte_decimal, parte_entera = math.modf(area_triangulo)

if parte_decimal != 0: 
    area_triangulo = round(area_triangulo, 2)


print("El área es: ", area_triangulo)

