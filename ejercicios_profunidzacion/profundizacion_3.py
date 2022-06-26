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
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
temp_1 = float(input("Ingrese el primer valor:"))
temp_2 = float(input("Ingrese el segundo valor:"))
temp_3 = float(input("Ingrese el tercer valor:"))
#temp 1 es la maxima y temp 3 es la minima
if temp_1 > temp_2 and temp_1 > temp_3 and temp_2 > temp_3:
    print("{} es la temperatura mas alta ingresada".format(temp_1))
    print("{} es la temperatura mas baja ingresada".format(temp_3))
# temp1 maxima y temp2 minima
elif temp_1 > temp_2 and temp_1 > temp_3 and temp_3 > temp_2:
    print("{} es la temperatura mas alta ingresada".format(temp_1))
    print("{} es la temperatura mas baja ingresada".format(temp_2))
# temp2 maxima y temp1 minima        
elif temp_2 > temp_1 and temp_3 > temp_1 and temp_2 > temp_3:
    print("{} es la temperatura mas alta ingresada".format(temp_2))
    print("{} es la temperatura mas baja ingresada".format(temp_1))
#temp2 maxima y temp 3 minima
elif temp_2 > temp_1 and temp_1 > temp_3 and temp_2 > temp_3:
    print("{} es la temperatura mas alta ingresada".format(temp_2))
    print("{} es la temperatura mas baja ingresada".format(temp_3))
# temp3 maxima y temp 1 minima
elif temp_3 > temp_1 and temp_3 > temp_2 and temp_2 > temp_1:
    print("{} es la temperatura mas alta ingresada".format(temp_3))
    print("{} es la temperatura mas baja ingresada".format(temp_1))
#temp3 maxima y temp2 minima
elif temp_3 > temp_1 and temp_3 > temp_2 and temp_1 > temp_2:
    print("{} es la temperatura mas alta ingresada".format(temp_3))
    print("{} es la temperatura mas baja ingresada".format(temp_2))    

promedio = (temp_1 + temp_2 + temp_3)
resultado = (promedio // 3)
print("El promedio de las temperaturas ingresadas es: {}".format(resultado))



