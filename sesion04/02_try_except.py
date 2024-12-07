#Sentencias Try&Except

'''
try:
# Codigo a ejecutar
# Pero podria haber errores en este bloque

except < tipo de error >:
# Haz esto para manejar la excepcion
# El bloque except se ejecutara si el bloque try lanza un error

else:
# Esto se ejecutara si el bloque try se ejecuta sin errores

finally:
# Este bloque se ejecutara siempre

'''

'''
________________________________
ejemplo

'''
#Division
def division(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    return result

print(division(4,0))

#otro ejemplo

try:
    res = dividir(num, div)
    print(res)
except ZeroDivisionError:
    print("Trataste de dividir entre cero :( ")


#manejar errores
'''
manejar errores de tipo:
 • ValueError 
(https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
 • ZeroDivisionError

'''