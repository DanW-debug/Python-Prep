#!/usr/bin/env python
# coding: utf-8

from Operaciones import *

## Manejo de errores

#1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?

a1 = Operaciones_list([2, 4, 5, 2, 7])

print(a1.CalcFactorial_01())
print(a1.Get_repeated_numbers_01())
print(a1.Temperature_Conversion_01('Celsius','Farenheit'))
print(a1.Check_prime_01())



#2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.

import unittest




#3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
#Creacion del objeto incorrecta<br>
#Creacion correcta del objeto<br>
#Metodo valor_modal()<br>

#Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta funcionalidad.

class ProbandoMiClase(unittest.TestCase):
    
    def test_crear_objeto1(self):
        param = 'hola'
        self.assertRaises(ValueError, Operaciones_list, param)
        #self.failUnlessRaises(ValueError, Operaciones_list , param)

    def test_crear_objeto2(self):
        param = [1,2,2,5]
        h1 = Operaciones_list(param)
        self.assertEqual(h1.arglist, param)

    def test_valor_modal(self):
        lis = [1,2,1,3]
        h1 = Operaciones_list(lis)
        moda, veces = h1.Get_repeated_numbers_01()
        moda = [moda]
        moda.append(veces)
        resultado = [1, 2]
        self.assertEqual(moda, resultado)

    def test_check_primes(self):
        lis = [3,5,7,11,34]
        h1 = Operaciones_list(lis)
        Response = h1.Check_prime_01()
        Result = [True, True, True, True, False]
        self.assertEqual(Response, Result)

unittest.main(argv=[''], verbosity=2, exit=False)



#4) Probar una creación incorrecta y visualizar la salida del "raise"

#6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo

#7) Agregar casos de pruebas para el método conversion_grados()

#8) Agregar casos de pruebas para el método factorial()

#9) Completar el código en las funciones del archivo "checkpoint.py" y probarlo a partir de la ejecución del script "tests.py"