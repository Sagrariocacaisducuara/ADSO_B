# x=int(input('ingrese valor'))
# print('salidas a consola')
flujo=open('archivos/basico.txt','r')#abre el archivo llamado basico.txt que se encuentra dentro de la carpeta archivos en modo de lectura
#datos=flujo.read()
#print(type(datos))
#flujo.write('Bienvenido al trabajo con archivos')
for dia in flujo:#lee el contenido del archivo representado por la variable flujo línea por línea utilizando un bucle for
  print(dia) #imprimen todo de la variable dia 
#flujo.close()

with open ('archivos/basico.txt','r') as flujo:#abre el archivo llamado basico.txt que se encuentra dentro de la carpeta archivos en modo de lectura 
    datos=flujo.read()#lee todo el contenido del archivo representado por la variable flujo y lo almacena en la variable datos
    print(datos)#imprime todo de la variable datos

with open ('archivos/basico.txt','r') as flujo:#abre el archivo llamado basico.txt que se encuentra dentro de la carpeta archivos en modo de lectura
    for dia in flujo:#lee el contenido del archivo representado por la variable flujo línea por línea utilizando un bucle for
        print(dia)#imprimen todo de la variable dia 
