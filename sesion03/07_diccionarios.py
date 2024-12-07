#DICCIONARIO

'''
 Un diccionario es una colección no ordenada de pares clave
valor. Las claves son únicas e inmutables, mientras que los
valores pueden ser de cualquier tipo y pueden ser modificados.
 Características de los diccionarios:
 • Claves únicas: Cada clave en un diccionario es única, lo que
significa que no puede haber claves duplicadas
 • Mutabilidad de valores: Los valores de un diccionario
pueden ser modificados después de la creación
 • Desordenados: Aunque los diccionarios mantienen el orden
de inserción a partir de Python 3.7, no se debe confiar en el
ordeN
'''

'''
 Los diccionarios en Python se definen utilizando llaves {} y los 
pares clave-valor se separan por dos puntos :
 Por ejemplo, la sintaxis sería así,
'''

#mi_diccionario = {
 #   "clave1": valor1,
  #  "clave2": valor2,
   # "clave3": valor3
 #}


d1 = {
    "Nombre": "Sara",
    "Edad": 27,
    "Documento": 1003882
}


dn = dict([
    ('Nombre', 'Sara'),
    ('Edad', 34),
    ('Documento', 1003882),
])
print(dn)

'''
Diccionarios
 Para acceder a los valores de un diccionario, se utiliza la clave 
correspondiente de la siguiente manera:
 print(mi_diccionario["nombre"])  # Resultado: Luis
 print(mi_diccionario["edad"])  # Resultado: 30
'''

'''
Para agregar un nuevo par clave-valor a un diccionario en 
Python, 
puede 
utilizar 
mi_diccionario["nueva_clave"] = nuevo_valor.
 mi_diccionario["ciudad"] = "Madrid"  # Agrega una nueva clave-valor
 la 
sintaxis 
'''

'''
El método items() retorna una vista de los pares clave-valor del 
diccionario en forma de tuplas.
 mi_diccionario = {"nombre": "Luis", "edad": 30, "ciudad": "Madrid"}
 vista_items = mi_diccionario.items()  # Retorna una vista de los pares clave
valor
 print(vista_items)  
# Resultado: dict_items([('nombre', 'Luis'), ('edad', 
30), ('ciudad', 'Madrid')])

'''

'''
Por otro lado, también disponemos de los métodos:
 • keys() devuelve una lista de todas las claves en el diccionario
 • values() que devuelve una lista de todos los valores
'''

'''
Diccionarios
 04GIAR
 Los diccionarios se pueden iterar de manera muy similar a las 
listas u otras estructuras de datos. Para imprimir los key y los 
value
 # Imprime los key del diccionario
 for x in d1:
    print(x)
 #Nombre
 #Edad
 #Documento
 #Direccion
 # Impre los value del diccionario
 for x in d1:
    print(d1[x])
 #Laura
 #27
 #1003882
 #Calle 123
 # Imprime los key y value del 
diccionario
 for x, y in d1.items():
    print(x, y)
 #Nombre Laura
 #Edad 27
 #Documento 1003882
 #Direccion Calle 123


'''


'''
-------------------------------------------------------------------------
PRACTICA
'''

#Creacion de diccionarios
registro_sara = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}
registro_paco = dict([
      ('Nombre', 'Paco'),
      ('Edad', 49),
      ('Documento', 454678456),
])
print(registro_paco)
#Acceder a elemento
print(registro_paco["Nombre"])
#Cambio de documento
registro_paco["Documento"]=64
print(registro_paco)

#Imprimir todos los elementos de un diccionario
# Imprime las claves del diccionario
for clave in registro_paco:
    print(clave)

# Imprime las claves del diccionario
for clave in registro_paco:
    print(registro_paco[clave])

#Imprime todo
for clave,valor in registro_paco.items(): # ("Nombre","Paco") ("Edad",49)
    print(f"{clave} - {valor}")


