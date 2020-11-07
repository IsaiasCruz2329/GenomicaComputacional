# La formula para el índice de Masa Corporral es IMC = kg/m2 donde kg es el peso de la persona en kilogramos y m2 es la altura en metros al cuadrado. Realizar programa que calcula el IMC cuando se le provee el peso y altura 

print("Introducir el peso del individuo: ")
peso = float(input())

print("Introducir la altura en metros del individuo: ")
altura = float(input())

indice = peso/altura**2

print("El IMC es: ", indice)
