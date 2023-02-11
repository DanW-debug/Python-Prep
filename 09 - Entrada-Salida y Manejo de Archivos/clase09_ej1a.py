from sys import *
import sys

if (len(sys.argv) == 4):
    print(argv[1])
    print(argv[2])
    print(argv[3])
else:
    print("Error: numero incorrecto de parámetros")
print('Nombre del archivo', argv[0])