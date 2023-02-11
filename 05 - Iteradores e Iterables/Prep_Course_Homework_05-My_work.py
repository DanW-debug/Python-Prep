#!/usr/bin/env python
# coding: utf-8
#from collections import Iterable

## Iteradores e iterables

#1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

My_list = list()

for n in range(-15,0):
    My_list.append(n)
print(My_list)
    
#2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

i = 0
while i < len(My_list):  
    if(My_list[i]%2 == 0):
        print(My_list[i])
    i += 1    

#3) Resolver el punto anterior sin utilizar un ciclo while

for element in My_list:
    if(element%2 == 0):
        print(element)

#4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

i = 0
for element in My_list:
    print(element)
    i += 1
    if(i > 2):
        break


#5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

i = 0
for index, element in enumerate(My_list):
    print(index, element)
    i += 1
    if(i > 2):
        break

#6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

My_list = [1,2,5,7,8,10,13,14,15,17,20]
for index, element in enumerate(My_list):
    if(index == len(My_list)-1):
        break
    if(My_list[index+1] != element+1):
        My_list.insert(index+1,element+1)
print(My_list)


#7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
#n<sub>0</sub> = 0<br>
#n<sub>1</sub> = 1<br>
#n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
#Crear una lista con los primeros treinta números de la sucesión.<br>

My_list = list()

for n in range(0,30):
    if(n == 0 or n == 1):
        My_list.insert(n, n)
    else:
        My_list.insert(n, My_list[n-2]+My_list[n-1])
print(My_list)

#8) Realizar la suma de todos elementos de la lista del punto anterior

sum = 0
for element in My_list:
    sum = sum+element
print(sum)

#9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
#Donde i es la cantidad total de elementos<br>
#n<sub>i-1</sub> / n<sub>i</sub><br>
#n<sub>i-2</sub> / n<sub>i-1</sub><br>
#n<sub>i-3</sub> / n<sub>i-2</sub><br>
#n<sub>i-4</sub> / n<sub>i-3</sub><br>
#n<sub>i-5</sub> / n<sub>i-4</sub><br>
  
for n in range(25,30):
    if (n == 29):
        break
    print(My_list[n+1]/My_list[n])

#10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
#cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

My_str = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

for i, c in enumerate(My_str):
    if(c == 'n'):
        print(i)

#11) Crear un diccionario e imprimir sus claves utilizando un iterador

My_dictionary ={'city': ['Buenos Aires','Berlin','New York'],
                'country': ['Argentina','Germany','EE.UU.'],
                'continent': ['South America','Europe','North America']}

for key in My_dictionary:
    print(key)

 
#12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

My_list = list(My_str)
for  element in My_list:
    print(element)

#13) Crear dos listas y unirlas en una tupla utilizando la función zip

My_first_list = [10, 25, 18]
My_second_list = [2, -4, 140]

c = zip(My_first_list, My_second_list)

My_list = list(c)

print(My_list)

#14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
#lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

My_result_list = list()
My_list = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

for element in My_list:
    if(element%7 == 0):
        My_result_list.append(element)
print(My_result_list)

#15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
#lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

My_list = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

print(type(My_list))

count = 0
for element_a in My_list:
    if(isinstance(element_a, list) == True):
        for element_b in element_a:
            count +=1
    else:
        count +=1
print('Total number of elements is', count)

#16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

for index, element in enumerate(My_list):
    if(isinstance(element, list) != True):
        My_list[index] = list(element)
print(My_list)

