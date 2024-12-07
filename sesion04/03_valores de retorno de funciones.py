#Valores de retorno de funciones en Python

#Sintaxis de return


def nombre_de_la_funcion(parametros):
 # bloque de código de la función
    return valor_a_devolver

#Sintaxis de return. Devolver un valor simple

def suma(a, b):
    resultado = a + b
    return resultado
 # Llamada a la función y asignación del valor devuelto a una variable
resultado_suma = suma(5, 3)
print(resultado_suma)  # Salida: 8


#Sintaxis de return. Devolver múltiples valores

def tupla_colores():
    return ("rojo", "verde", "azul")
colores = tupla_colores()
print(colores)  # Salida: ('rojo', 'verde', 'azul')


