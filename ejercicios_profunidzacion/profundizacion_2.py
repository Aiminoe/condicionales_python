# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
numero_1 = int(input("Ingrese el primer numero:"))
numero_2 = int(input("Ingrese el segundo numero:"))
numero_3  = int(input("Ingrese el tercer numero:"))

resto_1 = numero_1 % 2
resto_2 = numero_2 % 2
resto_3 = numero_3 % 2

if resto_1 == 0:
    print("{} es par".format(numero_1))
else:
    print("{} es impar".format(numero_1))

if resto_2 == 0:
    print("{} es par".format(numero_2))
else:
    print("{} es impar".format(numero_2))

if resto_3 == 0:
    print("{} es par".format(numero_3))
else:
    print("{} es impar".format(numero_3))
