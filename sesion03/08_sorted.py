#sorted
'''

Sorted
 La función sorted(). Esta función toma un iterable como
argumento principal
 numbers = [5, 3, 4, 3, 6, 7, 3, 2, 3, 4, 1]
 sorted(numbers)
 [1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 7]

'''

'''

Sorted. Dict
 04GIAR
 En el caso de los diccionarios nos sirve para poder ordenar por 
la clave o valores
 people = {3: "Jim", 2: "Jack", 4: "Jane", 1:
 "Jill"}
 #Sort by key
 dict(sorted(people.items()))
 #{1:'Jill',2: 'Jack',3:'Jim',4:'Jane'}
 #Sort by value
 dict(sorted(people.items(), key=lambda item:
 item[1]))
 #{2:'Jack', 4: 'Jane',1:'Jill',3: 'Jim'}
 student_scores ={
 'Alex':88,
 'Ben':75,
 'Cyrus':93,
 'Denver':85
 }
 sorted_by_values =
 dict(sorted(student_scores.items(),
 key=lambda item: item[1],
 reverse=True))
 print(sorted_by_values)

'''

'''
---------------------------------------------------------------
PRACTICA

'''

#numbers = [5, 3, 4, 3, 6, 7, 3, 2, 3, 4, 1]
#print(sorted(numbers))

#El diccionario
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
sorted_people = dict(sorted(people.items()))
print(sorted_people)

#Ordenar por elemento
sorted_alph_people = dict(sorted(people.items(),key=lambda item:item[1]))
print(sorted_alph_people)

#Ordenar por elemento + asc/desc
sorted_alph_people_reverse = dict(sorted(people.items(),key=lambda item:item[1],reverse=True))
print(sorted_alph_people_reverse)

