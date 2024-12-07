#Módulos

#definición

#creando un módulo

# operaciones.py
def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

#Importando un módulo

import operaciones
resultado_suma = operaciones.suma(5, 3)
print("Resultado de la suma:", resultado_suma)
resultado_resta = operaciones.resta(10, 4)
print("Resultado de la resta:", resultado_resta)


#Importando funciones específicas de un módulo

from operaciones import multiplicacion, division

resultado_multiplicacion = multiplicacion(6, 2)
print("Resultado de la multiplicación:", resultado_multiplicacion)
resultado_division = division(15, 3)
print("Resultado de la división:", resultado_division)

# Alias en la Importación

import operaciones as ops
resultado_suma = ops.suma(5,3)
print("Resultado de lasuma:", resultado_suma)

from operaciones import resta as restar
resultado_resta= restar(10, 4)
print("Resultado de laresta:",resultado_resta)

#Módulos Estándar de Python

'''
 Además de crear nuestros propios módulos, Python incluye 
una biblioteca estándar con una amplia variedad de módulos 
útiles para diversas tareas. Algunos ejemplos son:
 Módulo
 math
 random
 datetime
 os
 string
 Descripción
 Contiene funciones matemáticas comunes
 Permite generar números aleatorios
 Proporciona clases para manejar fechas y horas
 Proporciona funciones para interactuar con el sistema 
operativo

'''