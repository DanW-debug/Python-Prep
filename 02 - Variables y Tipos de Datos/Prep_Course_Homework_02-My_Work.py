#!/usr/bin/env python
# coding: utf-8


## Variables

##1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

a = 34
print(a)


##2) Imprimir el tipo de dato de la constante 8.5

print(type(8.5))


##3) Imprimir el tipo de dato de la variable creada en el punto 1

print("la variable a es:", type(a))

##4) Crear una variable que contenga tu nombre

Mi_nombre = "Daniel"
print(Mi_nombre)


##5) Crear una variable que contenga un número complejo

Complex_nr = 10 + 5j

##6) Mostrar el tipo de dato de la variable crada en el punto 5

print(Complex_nr, "El tipo de Complex_nr es:", type(Complex_nr))

##7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

pi = round(3.14159265359,4)
print(pi)

##8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

Logic_str = 'True'
Logic = True

##9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

print(type(Logic_str))
print(type(Logic))

##10) Asignar a una variable, la suma de un número entero y otro decimal

Var_sum = 10 + 3.4
print(Var_sum)

##11) Realizar una operación de suma de números complejos

Complex_sum = (10 + 4j) + (-4 + 30j)
print(Complex_sum)

##12) Realizar una operación de suma de un número real y otro complejo

Real_Complex_sum = 104.45 + (34 - 5j)
print(Real_Complex_sum)

##13) Realizar una operación de multiplicación

Mult = 8 * 4
print(Mult)

##14) Mostrar el resultado de elevar 2 a la octava potencia

Power = 2**8
print(Power)

##15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

Div_op = 27 / 4
print(Div_op)

##16) De la división anterior solamente mostrar la parte entera

Div_Integerpart_op = 27 // 4
print(Div_Integerpart_op)

##17) De la división de 27 entre 4 mostrar solamente el resto

Div_Reminderpart_op = 27 % 4
print(Div_Reminderpart_op)

##18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado)

Result27 = (Div_Integerpart_op * 4) + Div_Reminderpart_op
print(Result27)

##19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

a_str = "This is a string"
b_str = "this is another string"
sum_str = a_str + ' and ' + b_str
print(sum_str)

##20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

Two_str = "2"
Two_int = 2
Two_str == Two_int

if (Two_str == Two_int):
    print(True)
else:
    print(False)

##21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

if (int(Two_str) == Two_int):
    print(True)
else:
    print(False)

int(Two_str) == Two_int

##22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

#Because ',' is not the right symbol between the integer and fractional parts of a real number

##23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

c = 3
print("Initial value: ",c)
c -= 1
print("New value: ", c)

##24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

print(1 << 2)

# The binary system is composed by two symbols named '1' and '0'
# 1 << 2 means the following:
#   3 2 1 0 n
#   8 4 2 1 2 ** n  
#   0 0 0 1  ===> 1
# This position is equivalent to 2**0 = 1
# If we move the '1' to the left we get:
#  8 4 2 1  
#  0 0 1 0   ===> 2
# This position is equivalent to 2**1 = 2
#  A second move to the left bring us:
#  8 4 2 1
#  0 1 0 0   ===> 4

##25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# Mix_op = 2 + '2'  The interpreter can't resolve the sum of two heterogeneous types
Mix_op1 = 2 + 2
print("Integer sum: ", Mix_op1) 
Mix_op2 = '2' + '2'
print("Concatenation of two strings: ", Mix_op2)

##26) Realizar una operación válida entre valores de tipo entero y string

Mix_op3 = str(24) + " es un entero"
print(Mix_op3)

var1 = 'este texto se repite '
var2 = 3
print(var1 * var2 + str(var2) + ' veces')
