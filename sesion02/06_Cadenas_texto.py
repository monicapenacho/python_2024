#Tipos de datos
#Tipos de datos: Cadenas de Texto

'''
Las cadenas de texto en Python (str) son secuencias de
caracteres encerradas entre comillas simples (') o dobles (").
Pueden contener letras, números, símbolos y espacios. Algunos
ejemplos de cadenas de texto son "Hola", 'Python', "123", etc.

 Las cadenas en Python son inmutables (lo que significa que no
04GIAR
 se pueden modificar una vez creadas). Cualquier operación que
parezca modificar una cadena en realidad crea una nueva
cadena

'''

# Concatenado de cadenas
'''
 La concatenación de cadenas se realiza utilizando el operador 
+:

'''

# Formateo de cadenas

'''
 Tal vez queramos declarar una cadena que contenga variables 
en su interior, como números o incluso otras cadenas. 
Una forma de hacerlo sería concatenando la cadena que 
queremos con otra usando el operador +. 
str() convierte en string lo que se pasa como parámetro
'''

x = 5
s = "El numero es: " + str(x)
print(s) #El número es: 5

'''
 Python ofrece varios métodos para formatear cadenas, como 
format() y literales de cadena formateados (f-string):
'''
 # format()
nombre = "Juan"
edad = 30
mensaje = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(mensaje)  # Salida: "Hola, mi nombre es Juan y tengo 30 años."

 # F-string (Python 3.6+)
mensaje_fstring = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje_fstring)  # Salida: "Hola, mi nombre es Juan y tengo 30 años."

#Preguntando al usuario
'''
 La función input() permite obtener texto escrito por teclado. Al 
llegar a la función, el programa se detiene esperando que se 
escriba algo y se pulse la tecla Intro
'''

print("¿Cómo se llama?")
nombre = input()
print(f"Me alegro de conocerle, {nombre}")
      
'''
-----------------------------------------------------------------------------------------
PRACTICA
'''

# Print

print("Hola Pakito")

# Diferentes definiciones

cadena_simple = 'Hola, mundo!'
cadena_doble = "¡Hola, mundo!"
cadena_triple = """Este es un ejemplo
de una cadena con múltiples líneas."""

print(cadena_triple)

# Concatenacion

saludo = "Hello"
nombre = "Pakito"

print(saludo+" "+nombre)

cadena1 = "Hola"
cadena2 = " mundo"
cadena_concatenada = cadena1 + cadena2
print(cadena_concatenada)  # Salida: "Hola mundo"

# Formateo v1
nombre = "Juan"
edad = 30
mensaje = "Hola, mi nombre es {} y tengo {} años.".format(nombre,edad)
print(mensaje)  # Salida: "Hola, mi nombre es Juan y tengo 30 años."

# F-string (Python 3.6+)
mensaje_fstring = f"Hola, mi nombre es {nombre} y tengo {edad} años."
# print(mensaje_fstring)  # Salida: "Hola, mi nombre es Juan y tengo 30 años."
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")





