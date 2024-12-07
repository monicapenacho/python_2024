#Bucles

'''
Los bucles son una herramienta que 
nos permite repetir un bloque de 
código varias veces. 
En Python, contamos con dos tipos 
principales de bucles: 
• For
 • while
'''

#Bucle for
''' 
#Bucle for
 El bucle for se utiliza para iterar sobre una secuencia (como una 
lista, tupla, diccionario, etc.) y ejecutar un bloque de código para 
cada elemento en esa secuencia.
 La sintaxis básica del bucle for es la siguiente:
 for elemento in secuencia:
 # bloque de código a ejecutar para cada elemento

 Podemos utilizar el bucle for para realizar una serie de 
iteraciones específicas, por ejemplo, un número fijo de veces.
 Esto se logra utilizando la función range(), que genera una 
secuencia de números en un rango dado.
 # Ejemplo de bucle for con range(5)
 for i in range(5):
 print(i)
 En este ejemplo, range(5) genera una secuencia de números 
desde 0 hasta 4 (excluyendo el 5), y el bucle for itera sobre 
cada uno de estos números, asignándolos a la variable i en 
cada iteración. Luego, se imprime el valor de i, resultando en la 
salida:
'''

#Bucle while
'''
Bucle while
 El bucle while se utiliza para repetir un bloque de código 
mientras una condición sea verdadera. 
La sintaxis básica del bucle while es la siguiente:

contador = 1
 while contador <= 5:
 print(contador)
 contador += 1

'''


# Sentencias break y continue

'''
 Dentro de los bucles en Python, también podemos utilizar las 
sentencias break y continue para controlar el flujo de 
ejecución.

BREAK
 • break : Termina el bucle y ejecuta el bloque de código que 
está después del bucle.
 • continue : Salta a la siguiente iteración del bucle, ignorando 
el resto del bloque de código para esa iteración.
 frutas = ["manzana", "banana", "cereza", "sandía", "uva"]
 for fruta in frutas:
 print(fruta)
 if fruta == "sandía":
 break
 
 CONTINUE
 numeros = [1, 2, 3, 4, 5]
 for numero in numeros:
 if numero % 2 == 0:
 continue
 print(numero)

'''
