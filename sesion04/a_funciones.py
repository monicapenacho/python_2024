#Funcion saludo
def saludo():
    print("Hola Paco")

#Funcion suma
def suma(a, b):
    print(a + b)

#Funcion suma
def sumaReturn(a, b):
    return (a + b)

#Funcion division
def division(a, b):
    print(a / b)

#Usar saludo
saludo()

#Usamos suma
suma(27652, 5) # llamamos a la función

#Usamos suma con bucle for y constante + i
CONSTANTE=20
for i in range(1,5,1):
    suma(CONSTANTE, i)

#Usar sumaReturn
#Primero almacenar lo que me devuelve la función dentro de result
#Segundo imprimir si quiero:  {result}
result=sumaReturn(27652, 5)
print(f"El resultado es {result}")

#Usar division
division(4,2)