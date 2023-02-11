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
        # Init internal variables
        Result_value = 0.0 
        Units = [['Celsius','Farenheit'], ['Celsius', 'Kelvin'],['Farenheit', 'Celsius'],['Farenheit','Kelvin'], ['Kelvin','Celsius'],['Kelvin','Farenheit']]
        CheckUnit = ['Celsius', 'Farenheit', 'Kelvin']
        # Arguments validation
        if(isinstance(Temp_value, (int, float)) == False):
            return("Error: Temperature must be integer or float")    
        if(CheckUnit.count(From) == 0):
            return("Error: Source unit must be Celsius, Farenheit or Kelvin")
        if(CheckUnit.count(To) == 0):
            return("Error: Destination unit must be Celsius, Farenheit or Kelvin")    
        if(From == To):
            return("Error: Destination and Source units must be different")

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

class Operaciones_list(Operaciones):
    def __init__(self, arglist):  
        Operaciones.__init__(self)    
        if (type(arglist) != list):
            self.arglist = []
            print("AAA")
            raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de núemeros enteros')  
        else:        
            print("BBB")
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
