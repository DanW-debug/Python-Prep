#!/usr/bin/env python
# coding: utf-8

## Funciones

#1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

def Check_prime(num):
    for n in range(2,num):
        if(num%n == 0):
            return False
    return True 

print("Prime Test is", Check_prime(12))

#2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

Source_list = [4, 5, 8, 7, 11]
Result_list = list()

def Check_prime_list(List_input):
    List_output = list()
    for n in range(0,len(List_input)):
        if(Check_prime(List_input[n]) == True):
            List_output.append(List_input[n])
    return List_output

print (Check_prime_list(Source_list))

#3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

Number_list = [1, 3, 5, 3, 78, 3, 5]

def Get_repeated_numbers(Source_list):
    My_tuple = tuple(Source_list)
    Repetition_list = list()
    Number_list = list()
    Repetition = 0
    Number = 0
    for n in range(0,len(Source_list)):
        Rep_counter = 0
        if(Source_list[n] in Number_list):
            continue
        else:
            Number_list.append(Source_list[n])
            Repetition_list.append(My_tuple.count(Source_list[n]))
    for nr, rep in zip(Number_list, Repetition_list):
        if(Repetition < rep):
             Repetition = rep
             Number = nr
    print(Repetition, Number)
    return Number

print(Get_repeated_numbers(Number_list))

#4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.

Number_list = [1, 3, 5, 3, 78, 3, 5]

def Get_repeated_numbers(Source_list, flag):
    My_tuple = tuple(Source_list)
    Repetition_list = list()
    Number_list = list()
    Results_list = list()
    
    for n in range(0,len(Source_list)):
        Rep_counter = 0
        if(Source_list[n] in Number_list):
            continue
        else:
            Number_list.append(Source_list[n])
            Repetition_list.append(My_tuple.count(Source_list[n]))
    
    if(flag == True):
        for Repetition, Number in sorted(zip(Repetition_list, Number_list), reverse=True):
            print(Number, Repetition)
            a = [Number, Repetition]
            Results_list.append(a)
    else:
        for Repetition, Number in sorted(zip(Repetition_list, Number_list)):
            print(Number, Repetition)
            a = [Number, Repetition]
            Results_list.append(a)
    return Results_list

print(Get_repeated_numbers(Number_list, False))

#5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
#Fórmula 1	: (°C × 9/5) + 32 = °F<br>
#Fórmula 2	: °C + 273.15 = °K<br>
#Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino

def Temperature_Conversion(Temp_value, From, To):
    Result_value = 0.0 
    Units = [['Celsius','Farenheit'], ['Celsius', 'Kelvin'],['Farenheit', 'Celsius'],['Farenheit','Kelvin'], ['Kelvin','Celsius'],['Kelvin','Farenheit']]
    SrcDest = [From, To]
    n = Units.index(SrcDest)
    if (n == 0):            # Celsius to Farenheit
        Result_value = (Temp_value * 9/5) + 32
    if (n == 1):            # Celsius to Kelvin
        Result_value = Temp_value + 273.15
    #if (n == 2):          # Farenheit to Celsius

    #if (n == 3):          # Farenheit to Kelvin
    
    #if (n == 4):          # Kelvin to Celsius
    
    #if (n == 5):          # Kelvin to Farenheit
    
    
    return(Result_value)


print(Temperature_Conversion(-273.0, 'Celsius', 'Kelvin'))

#6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:




#7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo
