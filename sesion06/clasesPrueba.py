#Definir clase
#class Perro:
    #pass  # para que no de error porque la clase está vacía

#Definir objetos
#objeto_perro = Perro()

#Definir atributos

    #constructor o método init
    def __init__(self, nombre, raza):

    # Atributos de la instancia
        self.nombre = nombre
        self.raza = raza

    #imprimir:   # Mensaje al crear el objeto
    print(f"Creando perro {nombre}, {raza}");

#Objeto: pasar el valor de los atributos
    labrador = ("Zenon", "labrador")
    labrador_otro = ("Tiza", "labrador")

#Acceso a atributo
    print(labrador.raza);
    print (labrador_otro.nombre);




