#Definir clase
#class Perro:
    #pass  # para que no de error porque la clase está vacía

#Definir objetos
#objeto_perro = Perro()

#Definir atributos
    #class
class Perro:
    #atributos clase
    especie = "mamífero"



    #constructor o método init
    def __init__(self, nombre, raza):

    #imprimir:   # Mensaje al crear el objeto
        print(f"Creando perro {nombre}, {raza}");

    # Atributos de la instancia
        self.nombre = nombre
        self.raza = raza

    #acceso atributo clase (sin objeto)
        print(Perro.especie)

#Objeto: pasar el valor de los atributos
labrador = Perro("Zenon", "labrador")
labrador_otro = Perro("Tiza", "labrador")

#Acceso a atributo objeto
print(labrador.raza);
print (labrador_otro.nombre);

#acceso atributo clase desde el objeto
print(labrador.especie, labrador.nombre, labrador.raza);




