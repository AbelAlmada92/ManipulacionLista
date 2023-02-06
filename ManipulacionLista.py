def capturar():
    global lista
    lista = []
    print("Cuantos elementos quiere que tenga la lista? ")
    n = input()
    n = int (n)
    for i in range (0, n):
        print("Ingrese el elemento del indice ", i)
        elemento = input()
        lista.insert(i, elemento)

def mostrar():
    print(lista)       
    
def agregar():
    print("Ingrese el elemento que desea agregar: " )
    elemento = input()
    print("Ingrese el indice donde desea agregarlo: ")
    indice = input()
    indice = int (indice)
    longitud = len(lista)
    longitud = int(longitud)
    if(indice>longitud or indice<0):
        print("El indice debe estar entre 0 y ",longitud)
    else:
        lista.insert(indice, elemento)
        print("Elemento agregado")
        
def eliminar():
    print("Ingrese el indice del elemento que desea eliminar: ")
    indice = input()
    indice = int (indice)
    longitud = len(lista)
    longitud = int(longitud)
    if(indice>longitud or indice<0):
        print("El indice debe estar entre 0 y ",longitud=1)
    else:
        del lista[indice]
        print("Elemento eliminado.")
        
def modificar():
    print("Ingrese el indice del elemento que desea modificar: ")
    indice = input()
    indice = int (indice)
    print ("Ingrese el valor del elemento.")
    elemento = input()
    longitud = len(lista)
    longitud = int(longitud)
    if(indice>longitud or indice<0):
        print("El indice debe estar entre 0 y ",longitud=1)
    else:
        lista[indice] = elemento
        print("Elemento modificado.")
        
def princial():
    opcion="1"
    while(opcion !="6"):
         print("Manipulacion de lista")
         print("1. Capturar lista")
         print("2. Mostrar lista")
         print("3. Agregar elemento a la lista")
         print("4. Eliminaar elemento de la lista")
         print("5. Modificar elemento de la lista")
         print("6. Salir ")
         print("Que desea hacer?")
         opcion = input()
         if(opcion == "1"):
            capturar()
         elif(opcion == "2"):
             mostrar()
         elif(opcion == "3"):
             agregar()
         elif(opcion == "4"):
             eliminar()
         elif(opcion == "5"):
             modificar()
         elif(opcion == "6"):
             print("Programa terminado!")
         else:
             print("Opcion incorrecta!")
princial() 