#Listas en Python

'''
 Una lista en Python es una colección ordenada y mutable de
elementos (Mutable significa que los elementos de una lista
pueden ser modificados después de la creación de la lista).
 Las listas son una de las estructuras de datos más versátiles y
más utilizadas.
Nos permiten almacenar colecciones ordenadas de elementos,
como números, cadenas, u otros objetos
'''

'''
 Características de las Listas:
 • Mutabilidad: Los elementos de una lista pueden ser 
modificados después de la creación de la lista
 • Ordenadas: Los elementos de una lista están ordenados y 
mantienen el orden en el que se añadieron
 • Pueden contener cualquier tipo de dato: Una lista puede 
contener elementos de diferentes tipos de datos, como 
enteros, cadenas, flotantes, u otras lista
'''

'''
Las listas se definen utilizando corchetes [] y los elementos se 
separan por comas.

'''
#mi_lista = [1, 2, 3, 4, 5]

'''
 También es posible crear listas vacías, y posteriormente 
añadirle elementos según se necesite.

'''

#lista_vacia = []


#Iterar sobre una lista

'''
 Las listas se definen utilizando corchetes [] y los elementos se 
separan por comas.

'''
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

'''
Operaciones comunes con Listas
 Los elementos de una lista se pueden acceder utilizando 
índices numéricos. El índice comienza en 0 para el primer 
elemento y se incrementa de forma consecutiva
 mi_lista = [10, 20, 30, 40, 50]
 print(mi_lista[0])  # Resultado: 10
 print(mi_lista[2])  # Resultado: 30
'''

'''
Operaciones comunes con Listas
 Las listas en Python tienen varios métodos integrados para 
agregar elementos,
 mi_lista.append(60)  # Agrega 60 al final de la lista
 mi_lista.insert(2, 25)  # Inserta 25 en la posición 2
 Las listas en Python tienen varios métodos integrados para 
eliminar elementos,
 mi_lista.remove(20)  # Elimina el valor 20 de la lista
 mi_lista.pop(3)  # Elimina y devuelve el elemento en la posición 3
 del mi_lista[1]  # Elimina el elemento en la posición 1
 Las listas en Python tienen una función integrada para obtener 
su longitud,
 longitud = len(mi_lista)  # Devuelve la longitud de la lista

'''

'''
Convertir range en list
 El range() se puede convertir en list.
 print(list(range(5, 20, 2)))

'''

'''


--------------------------------------------------------------------
PRACTICA
'''

#Creacion
mi_lista = [1, 2, 3, 4, 5]
mi_lista_nombre = [ "Monica" , "Carlos", "Paco", "Pablo"]
lista_vacia = []

#Imprimir una lista
for nombre in mi_lista_nombre:
    print(nombre)

#Acceder a un elemento
print(f"El primer nombre es {mi_lista_nombre[0]}")

#Añadir un elemento
mi_lista_nombre.append("Alberto")

#Imprimir una lista
for nombre in mi_lista_nombre:
    print(nombre)

print("------")
#Eliminar "Paco"
#mi_lista_nombre.remove("Paco")
indice=0
for nombre in mi_lista_nombre:
    if(nombre=="Paco"):
        mi_lista_nombre.pop(indice)
    indice=indice+1

#Imprimir una lista
for nombre in mi_lista_nombre:
    print(nombre)