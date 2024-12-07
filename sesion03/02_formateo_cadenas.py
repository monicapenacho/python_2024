#Formateo de cadenas
'''
 Cuando disponemos entre llaves la variable a sustituir podemos 
agregar luego dos puntos y la cantidad de espacios que ocupará 
la variable:
 print(f"{elemento:10}")
 print(f"{elemento:10.2f}")

'''

'''

¡Por supuesto! Estas dos expresiones en Python usando f-strings tienen que ver con el formateo de la salida en pantalla, específicamente cómo se presenta el contenido de elemento.

1. print(f"{elemento:10}")
Qué Hace
Esta expresión reserva 10 espacios de ancho para el valor de elemento.
Si el contenido de elemento ocupa menos de 10 caracteres, Python rellenará el resto con espacios en blanco para alinear el texto.
Detalles Técnicos
10: Representa el ancho mínimo que debe ocupar el valor en la salida.
No se especifica ningún formato para el tipo de dato, por lo que se usa el valor tal cual.
Ejemplo
Si elemento = "Hola":

python
Copiar código
print(f"{elemento:10}")
Salida:

Copiar código
Hola      
(Notarás que hay 6 espacios en blanco después de "Hola" para completar los 10 caracteres).

Si elemento = 1234 (un número entero):

python
Copiar código
print(f"{elemento:10}")
Salida:

yaml
Copiar código
1234      
(El número se alinea de forma similar).

2. print(f"{elemento:10.2f}")
Qué Hace
Este formato es específico para números de tipo float.
10.2f indica que el número:
Debe ocupar un ancho total de 10 caracteres.
Debe mostrarse con exactamente 2 decimales.
Detalles Técnicos
.2f: Especifica que el valor debe presentarse como un número flotante con 2 decimales.
10: Representa el ancho total, incluyendo los dígitos, el punto decimal, los decimales y cualquier espacio en blanco necesario para completar los 10 caracteres.
Ejemplo
Si elemento = 123.456:

python
Copiar código
print(f"{elemento:10.2f}")
Salida:

markdown
Copiar código
    123.46
(Notarás que el número se redondeó a 2 decimales y que hay 4 espacios en blanco antes del número para completar los 10 caracteres).

Si elemento = 7.1:

python
Copiar código
print(f"{elemento:10.2f}")
Salida:

markdown
Copiar código
      7.10
(Se agrega un 0 después del 1 para cumplir con los 2 decimales, y se añaden 6 espacios antes para completar los 10 caracteres).

Diferencia Clave entre Ambos
{elemento:10}:

Alinea el valor (ya sea texto o número) en un espacio de 10 caracteres.
No aplica ningún formato adicional.
{elemento:10.2f}:

Es específico para números flotantes (float).
Formatea el número con 2 decimales y alinea el resultado en un espacio de 10 caracteres.
Errores Comunes
Si elemento no es un número flotante y usas .2f, obtendrás un error como:

python
Copiar código
ValueError: Unknown format code 'f' for object of type 'str'
Para asegurarte de que funcione, convierte elemento a float si no estás seguro de su tipo:

python
Copiar código
elemento = float(input("Ingresa un número: "))
print(f"{elemento:10.2f}")

'''
