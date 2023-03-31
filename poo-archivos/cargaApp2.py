from Conductor import *#importa todos los nombres definidos en el módulo o archivo conductor
from Carga import *#importa todos los nombres definidos en el módulo o archivo Carga
lista=[]se cre una lista vacia
with open('poo-archivos/listado.txt','r') as flujo:#se está abriendo el archivo de texto listado.txt en modo lectura
    for ob in flujo:#recorrerá cada línea del archivo de texto asociado al objeto flujo
        lista.append(ob)#se está agregando el valor de la variable ob a una lista llamada lista
i=0#se crea una variable llamada se le asigna un valor numérico de cero.
for ob in lista:#recorre cada elemento de la lista 
    lista[i]=ob.rstrip()#modifica el valor de un elemento de la lista
    i+=1#se incrementa el valor de la variable i en una unidad
print(lista)#imprime la lista
#placa, nombre,doc, cap, ejes
lautos=[]#se crea una lista vacia 
for ob in lista: recorrerá cada elemento de la lista lista
    #for x in ob.split(','):
    lautos.append(ob.split(','))#se está agregando una lista de elementos a una lista existente llamada lautos
cargas=[]se crea una lista vacia
print(lautos)#imprime la lista lautos
for i in range(len(lautos)):#que recorrerá los índices de la lista lautos y devuelve la cantidad de elementos que tiene la lista 
    #print(lautos[i][0])    
    p=lautos[i][0]# se está asignando el valor del primer elemento de una sublista de la lista lautos a la variable p
    n=lautos[i][1]# se está asignando el valor del segundo elemento de una sublista de la lista lautos a la variable n
    d=lautos[i][2]# se está asignando el valor del tecer elemento de una sublista de la lista lautos a la variable d
    c=lautos[i][3]# se está asignando el valor del cuarto elemento de una sublista de la lista lautos a la variable c
    e=lautos[i][4]# se está asignando el valor del quinto elemento de una sublista de la lista lautos a la variable e
    con=Conductor(n,d)# crea un objeto llamado con a partir de una clase llamada "Conductor" y pasando dos parámetros n y d
    obj=Carga(p,con,c,e)#creando un objeto llamado obj a partir de una clase llamada Carga y pasando cuatro parámetros p, con, c y e a su constructor
    cargas.append(obj)#el objeto obj al final de una lista llamada cargas

print(cargas)    # imprime todo de carga 
# 
# for ob in lautos:
    
#     #for x in ob:
#      #   print(x)
#         # p=x[0]
#         # n=x[1]
#         # d=x[2]
#         # c=x[3]
#         # e=x[4]
#         # con=Conductor(n,d)
#         # obj=Carga(p,con,c,e)
#         # cargas.append(obj)
# print(cargas)
