#!/usr/bin/env python
# coding: utf-8
def Listadelistas(lista):
    """
    Esta función recibe una lista, que puede contener elementos que a su vez sean listas y devuelve esos elementos por 
    separado en una lista única.
    En caso de que el parámetro no sea de tipo lista, debe retornar NULO.
    """

    stack = lista.copy()
    Result = []
    if (type(lista) != list):
        return(None)

    while(len(stack) != 0):
        current = stack.pop(0)
        print('current',current)
        if(type(current) != list):
            Result.append(current)
            print('Result', Result)
        else:
            for m in range(0, len(current)):
                stack.insert(0, current.pop())
    return(Result)

print(Listadelistas([1,[2,[3,4,[45,46,47]]],5,6]))


def CalcFactorial(n):
        if (n >= 0):
            if (n > 0):
                factorial = 1
                i = 1
                while (i <= n):
                    factorial = factorial * i
                    i += 1
                return(factorial)
            else:
                return(1)
        else:
            return(None) 


print (CalcFactorial(4))

def Calcprimos(desde, hasta):
    if ((type(desde) != int) or (type(hasta) != int) or (desde <= 0) or (hasta <= 0)):
        return(None)
    if ((desde > hasta) and (desde > 0) and (hasta > 0)):
        return([])
      
    flag = True
    Result = []
    for m in range(desde,hasta+1):
        for n in range(2,m):
            if(m%n == 0):
                flag = False
        if(flag == True):
            Result.append(m)
        else:
            flag = True
    return(Result)        


print(Calcprimos(7, 15))

Number_list = [1, 3, 5, 3, 78, 3, 5]

def Get_repeated_items(Source_list):
    if(len(Source_list) == 0):
        return(None)
    
    My_tuple = tuple(Source_list)
    Repetition_list = list()
    Item_list = list()
    Result = list()
    Repetition = 0
    Number = 0
    for n in range(0,len(Source_list)):
        Rep_counter = 0
        if(Source_list[n] in Item_list):
            continue
        else:
            Item_list.append(Source_list[n])
            Repetition_list.append(My_tuple.count(Source_list[n]))
            print('Number_list', Item_list, ' - ', 'Repetition_list', Repetition_list)
    length = len(Repetition_list)
    for n in range(0, length):
        Result.append([Item_list[n], Repetition_list[n]])        
    return Result

print(Get_repeated_items(Number_list))
print(Get_repeated_items(['hola','mundo','hola',13,14]))
print(Get_repeated_items([1, 2, 2, 4]))
print(Get_repeated_items([]))


def OrderDictionary( dictionary, key, order_flag = True):
    #Check parameters validity and local params init
    keylist = tuple(dictionary.keys())
    Relations = list()
    OrderedDict = {}
    if ((keylist.count(key) == 0) or type(dictionary) != dict):    
        return(None)

    # Using the key param, create a list of tuples with indexes and sort them
    value2order = dictionary.get(key)
    for n in range(0,len(value2order)):
        Relations.append((value2order[n],n))   
    print(Relations)
    Relations = sorted(Relations, reverse=order_flag, key=lambda item: item[0])
    print(Relations)
    # Loop for every key and insert the ordered value into OrderedDict iterable
    for n in range(0,len(dictionary.keys())):
        newvalue = list()
        key2process = keylist[n]  
        if (key2process == key):
            for n in range(0,len(Relations)):
                newvalue.append(Relations[n][0])
            print(newvalue)
            OrderedDict[key2process] = newvalue               
        else:
            for n in range(0, len(Relations)):
                newvalue.append((dictionary[key2process])[Relations[n][1]])
            print(newvalue)
            OrderedDict[key2process] = newvalue

    return(OrderedDict)

def OrderDictionary_1( dictionary, key, order_flag = True):
    #Check parameters validity and local params init
    keylist = tuple(dictionary.keys())
    Relations = list()
    OrderedDict = {}
    value_length = len(dictionary.get(key))
    key_length = len(dictionary.keys())

    if ((keylist.count(key) == 0) or type(dictionary) != dict):    
        return(None)

    # Using the key param, create a list of tuples with the nth element of each value per key
    for n in range(0,value_length):
        Valuelist = list()
        for m in range(0, key_length):
            element_store = dictionary.get(keylist[m])[n]
            Valuelist.append(element_store)
        Relations.append(tuple(Valuelist))
    print(Relations)
    # Sorting Relations ordered by key parameter
    keypos = keylist.index(key)
    Relations = sorted(Relations, reverse=order_flag, key=lambda item: item[keypos])
    print(*Relations)
    list_of_values = list(zip(*Relations))
    print(list_of_values)    
    #Arrange the new dictionary
    for i in range(0, key_length):
        OrderedDict[keylist[i]] = list_of_values[i]
             
    return(OrderedDict)




dict_par = {'clave1':['c','a','b'],
            'clave2':['casa','auto','barco'],
            'clave3':[1,2,3]}

print(OrderDictionary_1(dict_par, 'clave3', False))
