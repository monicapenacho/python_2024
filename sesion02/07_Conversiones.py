'''

Conversión de tipos o cast
 Hacer un cast o casting significa convertir un tipo de dato a otro.
Existen dos tipo:
 • Conversión implícita: Es realizada automáticamente por
Python. Sucede cuando realizamos ciertas operaciones con
dos tipos distintos.
 • Conversión explícita: Es realizada expresamente por
nosotros, como por ejemplo convertir de str a int con str().
 04GIAR
Conversión implícita
 Esta conversión de tipos es realizada automáticamente por
Python, prácticamente sin que nos demos cuenta. Aún así, es
importante saber lo que pasa por debajo para evitar problemas
futuros.
 El ejemplo más sencillo donde podemos ver este
comportamiento es el siguiente:
 a = 1 # <class 'int'>
 b = 2.3 # <class 'float'>
 a = a + b
 print(a)
 # 3.3
 print(type(a)) # <class 'float'>
 04GIAR
Conversión implícita
 Sin embargo hay otros casos donde Python no es tan listo y no
es capaz de realizar la conversión.
Si intentamos sumar un int a un string, tendremos un error
TypeError.
 a = 1
 b = "2.3"
 c = a + b
 # TypeError: unsupported operand type(s) for +: 'int' and 'str'
 04GIAR
Conversión explícita
 Por otro lado, podemos hacer conversiones entre tipos o cast de
manera explícita haciendo uso de diferentes funciones que nos
proporciona Python.
Las más usadas son las siguientes: float(), str(), int()
 04GIAR
Conversión explícita. Conversión a integer
 04GIAR
 Para convertir de float a int o de str a int debemos usar int().
Pero mucho cuidado, ya que el tipo entero no puede almacena
decimales, por lo que perderemos lo que haya después de la
coma. a=3.5
 a=int(a)
 print(a)
 #Salida:3
 a="3"
 print(type(a)) # <class 'str'>
 a=int(a)
 print(type(a)) # <class'int'>
 Cuidado ya que no es posible convertir a int cualquier valor.
 a="Python"
 a=int(a)
 #ValueError:invalidliteral for int() withbase 10: 'Python'
Conversión explícita. Conversión a float
 Para convertir a float debemos usar float(). Es importante notar
que se usa el . como separador.
 a = "35.5"
 print(float(a))
 # Salida: 35.5
 El siguiente código daría un error, dado que , no se reconoce
por defecto como separador decimal.
 a = "35,5"
 print(float(a))
 # Salida: ValueError: could not convert string to float: '35,5'
 04GIAR
Conversión explícita. Conversión a string
 Para convertir de float o int a str debemos usar str().
a = 10
 print(type(a)) # <class 'int'>
 a = str(a)
 print(type(a)) # <class 'str'>



'''


'''
-----------------------------------------------------------------------------
PRACTICA

'''


# Numeros
a = 1
b = "12.3"
edad = "4"

# Calculo
c = a + float(b)

ponderacion = c * int(edad)

print(c)
print(ponderacion)

print(int(ponderacion))