from sys import *
import sys
import calendar
import time
import os
import argparse

parser = argparse.ArgumentParser(prog='ENVREC', description='Write environmental variables to a file.')
parser.add_argument('temperature', metavar='temperature', type=float, 
                    help='temperature expressed in Celsius degrees')
parser.add_argument('humidity', metavar='humidity', type=float,
                    help='humidity expressed in %')
parser.add_argument('rain_event', metavar='rain event', choices=['True', 'False'],
                    help='Rain event expressed in boolean')

args = parser.parse_args([sys.argv[1],sys.argv[2],sys.argv[3]])
print(type(args.temperature), type(args.humidity), type(args.rain_event))

#Getting the timestamp
current_GMT = time.gmtime()
time_stamp = calendar.timegm(current_GMT)
#Building the record structure
    
namestring =[str(time_stamp),str(argv[1]),str(argv[2]),str(argv[3])]
record = ', '.join(namestring)
print(record)
print(type(record))
buffer = [record]
print(buffer)
#Open file
file_handle = open("clase09_ej2.csv", 'a')
for line in buffer:
    file_handle.write(line+'\n')
file_handle.close()







#else:
    #print("Error: numero incorrecto de parámetros")
    #print('Nombre del archivo', argv[0])