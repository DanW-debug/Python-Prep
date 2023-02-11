#!/usr/bin/env python
# coding: utf-8
""""
## Clases y Programación Orientada a Objetos

#1) Crear la clase vehículo que contenga los atributos:<br>
#Color<br>
#Si es moto, auto, camioneta ó camión<br>
#Cilindrada del motor

class Vehiculo:
    ## Definición de la clase
    def __init__(self, color, tipo, cilindrada):
        # Definición de atributos
        self.color
        self.tipo
        self.cilindrada
  
#2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
#Acelerar<br>
#Frenar<br>
#Doblar<br>

class Vehiculo:
    ## Definición de la clase
    def __init__(self, color, tipo, cilindrada):
        # Definición de atributos
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0
    def Acelerar(self, vel):
        self.velocidad += vel
    def Frenar(self, vel):
        self.velocidad -= vel
    def Doblar(self, grados):
        self.dirección += grados
    def Estado_Operacional(self):
        print(self.velocidad, self.direccion)
    def Caracteristicas(self):
        print(self.tipo,'-', self.color,'-', self.cilindrada)

#3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

a1 = Vehiculo('rojo','auto','1500')
a2 = Vehiculo('negro', 'auto', '2400')
a3 = Vehiculo('verde', 'camioneta', '1700')

print(a1.color)
print(a2.tipo)
print(a3.cilindrada)

#4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

a1.Caracteristicas()
a1.Estado_Operacional()
a1.Acelerar(10)
a1.Estado_Operacional()

#5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>
#Verificar Primo<br>
#Valor modal<br>
#Conversión grados<br>
#Factorial<br>

class Operaciones:
# Constructor
    def __init__(self) -> None:
        pass  
# Métodos
    def Check_prime(self, num):
        for n in range(2,num):
            if(num%n == 0):
                return False
        return True 

    def Get_repeated_numbers(self, Source_list):
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
            #print(Repetition, Number)
        return Number, Repetition

    def Temperature_Conversion(self, Temp_value, From, To):
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

    def CalcFactorial(self, n):
        if (type(n) == int):
            if (n > 0):
                factorial = 1
                i = 1
                while (i <= n):
                    factorial = factorial * i
                    i += 1
                return(factorial)
            else:
                return(-1)
        else:
            return(-2) 


#6) Probar las funciones incorporadas en la clase del punto 5

a1 = Operaciones()

print(a1.CalcFactorial(4))
print(a1.Get_repeated_numbers([1, 5, 8, 1, 4, 1, 7, 2]))
print(a1.Temperature_Conversion(34.5, 'Celsius', 'Farenheit'))
print(a1.Check_prime(56))

#7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

class Operaciones_list(Operaciones):
    def __init__(self, arglist):  
        Operaciones.__init__(self)    
        self.arglist = arglist
        print(self.arglist)
        
    # Factorial calculus
    def CalcFactorial_01(self):
        Results = list()   
        for i in self.arglist:
            Results.append(self.CalcFactorial(i))    
        return(Results)    

    # Modal calculus
    def Get_repeated_numbers_01(self):
        return(self.Get_repeated_numbers(self.arglist))

    # Temperature conversion
    def Temperature_Conversion_01(self, From, To):
        Results = list()
        for i in self.arglist:
            Results.append(self.Temperature_Conversion(i, From, To))
        return(Results)    


    # Prime number verification
    def Check_prime_01(self):
        Results = list()
        for i in self.arglist:
            Results.append(self.Check_prime(i))
        return(Results)    




a1 = Operaciones_list([2, 4, 5, 2, 7])

print(a1.CalcFactorial_01())
print(a1.Get_repeated_numbers_01())
print(a1.Temperature_Conversion_01('Celsius','Farenheit'))
print(a1.Check_prime_01())


#8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones


"""
from Operaciones import *

a1 = Operaciones_list([2, 4, 5, 2, 7])

print(a1.CalcFactorial_01())
print(a1.Get_repeated_numbers_01())
print(a1.Temperature_Conversion_01('Celsius','Farenheit'))
print(a1.Check_prime_01())
