#Definicion funcion
def nombre_de_la_funcion(parametros):
 # Bloque de código de la función
 # Puede contener múltiples instrucciones
    return resultado

#parametros y argumentos
def suma(a, b):
    print(a + b) # Output: 8
suma(3, 5) # llamamos a la función

#Valores de retorno

def dameNumero():
    return 8
resultado = dameNumero()
print(resultado) # Output: 8

#parametros posicionales

def resta(a, b):
    return a-b
resta(5, 3)  # 2
print(resta(5, 3))
# resta(1) # Error! TypeError

#parametros con valores predeterminados

def saludar(nombre="Mundo"):
    print("Hola,", nombre)
# Llamada a la función sin proporcionar un valor para el parámetro
saludar()  # Salida: Hola, Mundo
# Llamada a la función con un valor para el parámetro
saludar("Luis")  # Salida: Hola, Luis

def suma(a, b, c=0):
    return a+b+c
suma(5,5,3) # 13
suma(4,3) # 7

#Parámetros con nombre

def saludar(nombre, saludo="Hola"):
    print(saludo + ",", nombre)

# Llamadas a la función con parámetros con nombre
saludar(nombre="Ana")                             # Salida: Hola, Ana
saludar(saludo="Buenos días", nombre="Pedro")     # Salida: Buenos días, Pedro
saludar("Luis", saludo="¡Qué tal!")               # Salida: ¡Qué tal!, Luis



'''
Diferencias Principales
Aspecto	Parámetros con Valores Predeterminados	Parámetros con Nombre
Definición	Asignan un valor por defecto en la definición de la función.	Usan el nombre del parámetro en la llamada.
Uso	Parámetros opcionales.	Mayor claridad y flexibilidad en el orden.
Sobrescribir Valor	Puedes sobrescribir el valor predeterminado si pasas un argumento.	Puedes omitir valores predeterminados si no los necesitas.
Orden de Parámetros	Depende de la posición en la llamada.	No depende del orden, ya que se pasan por nombre.


'''

#Tipos de parámetros en Python. Paso por valor o por referencia

'''
Resumen
Tipos inmutables (int, str, float):
Dentro de la función, parece un paso por valor. Las modificaciones no afectan a la variable original.
Tipos mutables (list, dict, set):
Dentro de la función, se pasa la referencia al objeto. Los cambios afectan directamente al objeto original.
'''

 #Ejemplo paso por valor:
 # Ejemplo con un tipo básico (int)
def modificar_numero(numero):
    numero = numero * 2
numero_original = 5
modificar_numero(numero_original)
print("Número original después de llamar a la función:", numero_original)  #
Resultado: 5

 # Ejemplo con una referencia (lista)
def modificar_lista(lista):
    lista.append(4)
lista_original = [1, 2, 3]
modificar_lista(lista_original)
print("Lista original después de llamar a la función:", lista_original)  #
Resultado: [1, 2, 3, 4]

