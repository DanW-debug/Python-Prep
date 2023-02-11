#!/usr/bin/env python
# coding: utf-8

## Estructuras de Datos

#1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

from typing import List


my_list = ['Buenos Aires','Roma','Berlin','New York','Helsinki','Amsterdam','Tokyo']

print(my_list)

#2) Imprimir por pantalla el segundo elemento de la lista

print(my_list[1])

#3) Imprimir por pantalla del segundo al cuarto elemento

print(my_list[1:4])

#4) Visualizar el tipo de dato de la lista

print(type(my_list))

#5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

print(my_list[2:])

#6) Visualizar los primeros 4 elementos de la lista

print(my_list[:4])

#7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

my_list.append('Mendoza')
my_list.append('Roma')
print(my_list[0:])

#8) Agregar otra ciudad, pero en la cuarta posición

my_list.insert(3,'London')
print(my_list[:])

#9) Concatenar otra lista a la ya creada

my_list.extend(['Leeds','Auckland','Melbourne','Sydney','Perth'])
print(my_list[:])

#10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

print(my_list.index('Roma'))

#The search stops when finds the first instance of the given element


#11) ¿Qué pasa si se busca un elemento que no existe?

#print(my_list.index('Venecia'))

#System displays the message "ValueError: 'Venecia' is not in list"

#12) Eliminar un elemento de la lista

my_list.remove('Berlin')
print(my_list[:])

#13) ¿Qué pasa si el elemento a eliminar no existe?

#my_list.remove('Venecia')
#System displays message "ValueError: list.remove(x): x not in list"


#14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

last = my_list.pop()
print(last)

#15) Mostrar la lista multiplicada por 4

print(4*my_list[:])

#16) Crear una tupla que contenga los números enteros del 1 al 20

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
My_tuple = tuple(my_list)
print(My_tuple)

#17) Imprimir desde el índice 10 al 15 de la tupla

print(My_tuple[10:15])

#18) Evaluar si los números 20 y 30 están dentro de la tupla

print(20 in My_tuple)
print(30 in My_tuple)

#19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

length = len(my_list)
city = "London"
In_my_list = False
print(length)
for n in range(0,length):
    if(my_list[n] == city):
        In_my_list = True
        break
if(In_my_list == False):
    my_list.append(city)
    print(city,"added to my_list")
else:
    print(city,"was found in my_list")

#20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# in the list

length = len(my_list)
city = 'Berlin'
In_my_list = False
count = 0
print(length)
for n in range(0,length):
    if(my_list[n] == city):
        count += 1
        In_my_list = True
        
if(In_my_list == False):
    print(city,"was not found in my_list")
else:
    print(city,"was found", count, "times")

# In the tuple

My_tuple_of_cities = tuple(my_list)
city = 'Roma'
print(city, "was found", My_tuple_of_cities.count(city), "times")

#21) Convertir la tupla en una lista

print(My_tuple_of_cities)
print(callable(My_tuple_of_cities))
My_list_of_cities = list(My_tuple_of_cities)
print(My_list_of_cities)


#22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

city1, city2, city3 = My_tuple_of_cities[0],My_tuple_of_cities[1],My_tuple_of_cities[2] 

print("City1", city1, "City2", city2, "City3", city3)


#23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

my_list = ['Buenos Aires','Roma','Berlin','New York','Helsinki','Amsterdam','Tokyo']
my_tuple = tuple(my_list)
my_dictionary = {'city':my_list,
                 'country':['Argentina','Italy','Germany','Finland','Netherlands','Japan'],
                 'continent':['America','Europe','Europe','Europe','Europe','Asia']}
                   
print(my_dictionary)

#24) Imprimir las claves del diccionario

print(my_dictionary.keys())

#25) Imprimir las ciudades a través de su clave

print(my_dictionary['city'])
