# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    
    if (type(numero) == int):
            if (numero > 0):
                factorial = 1
                i = 1
                while (i <= numero):
                    factorial = factorial * i
                    i += 1
                return(factorial)
            else:
                return(None)
    else:
        return(None) 
    
    #return 'Funcion incompleta'

def EsPrimo(valor):
    '''
    Esta función devuelve el valor booleano True si el número reibido como parámetro es primo, de lo 
    contrario devuelve False..
    En caso de que el parámetro no sea de tipo entero debe retornar nulo.
    Recibe un argumento:
        valor: Será el número a evaluar
    Ej:
        EsPrimo(7) debe retornar True
        EsPrimo(8) debe retornar False
    '''
    #Tu código aca:
    
    if (isinstance(valor, int) == False):
        return(None)
    
    for n in range(2,valor):   
            if(valor%n == 0):
                return False
    return True
    
    #return 'Funcion incompleta'
    
def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    #Tu código aca:
    class Animal:
        def __init__(self, especie, color):
            self.especie = especie
            self.color = color
            self.Edad = 0
        
        def CumplirAnios(self):
            self.Edad += 1        
            return(self.Edad)
   
    a = Animal(especie, color)    
    return(a)
    #return 'Funcion incompleta'
