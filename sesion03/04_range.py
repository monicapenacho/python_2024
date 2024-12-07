# range

'''
 range() genera una secuencia de números que van desde 0
por defecto hasta el número que se pasa como parámetro
menos 1.
En realidad, se pueden pasar hasta tres parámetros separados
por coma, donde el primer es el inicio de la secuencia, el
segundo el final y el tercero el salto que se desea entre
números. Por defecto se empieza en 0 y el salto es de 1.
 #range(inicio, fin, salto)



'''
for i in range(5, 20, 2):
    print(i) #5,7,9,11,13,15,17,19

'''
 Se pueden generar también secuencias inversas, empezando
por un número mayor y terminando en uno menor, pero para
ello el salto deberá ser negativo.
'''
for i in range (5, 0, -1):
    print(i) #5,4,3,2,1


'''

Convertir range en list
 El range() se puede convertir en list.
 print(list(range(5, 20, 2)))

'''