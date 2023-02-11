#!/usr/bin/env python
# coding: utf-8

#Flujos de Control

    #1. Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
    
from gettext import npgettext
from re import I
from tkinter import N


a = 10

if(a > 0):
    print("a is greater than zero")
if(a < 0):
    print("a is lower than zero")
if(a == 0):
    print("a is equal to zero")

    #2. Crear dos variables y un condicional que informe si son del mismo tipo de dato

a = 40
b = "String"
c = 3

if(type(a) == type(b)):
    print("Type match")
else:
    print("Type mismatch")

if(type(a) == type(c)):
    print("Type match")
else:
    print("Type mismatch")

    #3. Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

for n in range(1,10):
    if(n%2 == 0):
        print(n, " is even")
    else:
        print(n, " is odd")

    #4. En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for n in range(0,6):
    print(n**3)

    #5. Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

a = 10
for n in range(0,a):
    print("cycle #", n+1)

    #6. Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

n = 5

if (type(n) == int):
    if (n > 0):
        factorial = 1
        i = 1
        while (i <= n):
            factorial = factorial * i
            i += 1
        print("n factorial is ", factorial)
    else:
        print(n, " is not greater than zero")
else:
    print(n, " is not an integer") 


    #7. Crear un ciclo for dentro de un ciclo while

a = 10
b = 5
i = 1
while(i <= a):
    for n in range(1,b):
        print("loop for ", n, " in cycle while #", i)
    i +=1

    #8. Crear un ciclo while dentro de un ciclo for

a = 5
b = 5
i = 1
for n in range(1,a):
    while(i <= b):
        print("loop while", i, " in cycle for #", n)
        i +=1
    
    #9. Imprimir los números primos existentes entre 0 y 30

flag = True
for m in range(2,30):
    for n in range(2,m):
        if(m%n == 0):
            flag = False
    if(flag == True):
        print(m, "is a prime number!")
    else:
        flag = True


    #10. ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

flag = True
for m in range(2,30):
    for n in range(2,m):
        if(m%n == 0):
            flag = False
            break
    if(flag == True):
        print(m, "is a prime number!")
    else:
        flag = True

    #11. En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

from time import time

start_time = time()
flag = True
for m in range(2,30):
    for n in range(2,m):
        if(m%n == 0):
            flag = False
            break
    if(flag == True):
        print(m, "is a prime number!")
    else:
        flag = True
elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)

    #12. Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

from time import time

start_time = time()
flag = True
for m in range(2,100):
    for n in range(2,m):
        if(m%n == 0):
            flag = False
            break
    if(flag == True):
        print(m, "is a prime number!")
    else:
        flag = True
elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)

import time

start_time = time.perf_counter()
flag = True
for m in range(2,30):
    for n in range(2,m):
        if(m%n == 0):
            flag = False
            break
    if(flag == True):
        print(m, "is a prime number!")
    else:
        flag = True
elapsed_time = time.perf_counter() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)
     
    #13. Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

n = 100
while(n <= 300):
    if(n%12 == 0):
        print(n)
    n +=1    

    #14. Utilizar la función input() que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

"""
while(True):
    print("Type an integer number: ")
    m = int(input())

    while(True):
        flag = True
        for n in range(2,m):
            if(m%n == 0):
                flag = False
                break
        if(flag == True):
            print(m, "is a prime number!")
        else:
            flag = True
            print(m, "is not a prime number")    
        print("Do you want to check the next number, input a new number or exit? [y/n/x]: ")
        answer = input()
        if(answer == "y"):
            m +=1
            continue
        elif (answer == "n"):
            break
        else:
            exit()
"""
    #15. Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

n = 100
while (n <= 300):
    if(n%3 == 0 and n%6 == 0):
        print("First number:",n)
        break
    else:
        n +=1

    # Bonus track: Crear código para factorizar un entero mayor que cero. Entregará dos listas, una con los factores y otra con los exponentes

# variables init
N = 18               # Number to factoring
divisor = 0
expo_nr = 0
np = 2
factors_list = list()
exponents_list = list()
m = 2
divisor = N
factor_flag = False
# Main loop
while (divisor != 1):
    if(divisor%np == 0):
        divisor = divisor/np
        if (factor_flag == False):  #Is it a new factor?
            factors_list.append(np)
            factor_flag = True   
        expo_nr += 1
    else: 
        if(expo_nr >0):             #Is it the first occurrence of the new factor?
            exponents_list.append(expo_nr)
        factor_flag =False
        expo_nr = 0
        m += 1      #Ready to the next search for a prime number
        # Finding the prime number
        remainder_flag = True
        reach_prime_flag = False
        while(reach_prime_flag == False): #Did we get a prime number?
            for n in range(2,m):
                if(m%n == 0):
                    remainder_flag = False
            if(remainder_flag == True):
                #print(m, "is a prime number!")
                np = m
                reach_prime_flag = True
            else:
                remainder_flag = True
                m += 1
        #-------------------------

exponents_list.append(expo_nr)
print(factors_list, exponents_list)























 

