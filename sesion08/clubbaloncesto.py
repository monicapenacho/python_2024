import os
class Club:
    '''
    Clase Club. Permite gestionar un club de baloncesto

    ATRIBUTOS DE CLASE
    ------------------
    nombre : str
        Define el nombre del club
    '''

    def __init__(self,nombre="CLUB BASKET"):
        self.nombre=nombre
        pass

    def print_menu(self):
        ''' 
        print_menu. Función que imprime un menu por pantalla '
        
        RETURN
        ------
        opcion : int
            Entero 1|2
        '''
        os.system("cls")
        print(f"-------- GESTOR {self.nombre} --------")
        print("[1] NUEVO EQUIPO")
        print("[2] LISTAR EQUIPOS")

        opcion = input("Introduce opcion [1|2]: ")
        opcion_incorrecta=True
        while(opcion_incorrecta):
            if not opcion.isdigit():
                opcion = input("Introduce opcion [1|2]: ")
                continue
            if not int(opcion) in [1,2]:
                opcion = input("Introduce opcion [1|2]: ")
                continue
            opcion_incorrecta = False

        return opcion


class Persona:
    '''
    Clase Persona. Define un elemento de tipo Persona

    ATRIBUTOS DE CLASE
    ------------------
    nombre : str
        Nombre de la persona
    edad : int
        Edad de la persona
    altura : float
        Altura en m
    peso : float
        Peso en kg
    '''

    def __init__(self,nombre,edad,altura,peso):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def print_persona(self):
        ''' 
        Función que imprime por pantalla una persona
        '''
        print(f"Nombre: {self.nombre}, altura: {self.altura}, peso: {self.peso}, edad: {self.edad}")

class Jugador(Persona):
    '''
    Clase Jugador. Define un elemento de tipo Jugador
    Hereda de Persona

    ATRIBUTOS DE CLASE
    ------------------
    dorsal : int
        Numero del dorsal de un jugador
    '''
    def __init__(self, nombre="", edad=18, altura=1.60, peso=55, dorsal=0):
        super().__init__( nombre, edad, altura, peso)
        self.dorsal = dorsal

    def nuevo_jugador(self):
        ''' 
        Imprimimos por consola el menú para recoger los datos del nuevo jugador
        '''
        print("-------- NUEVO JUGADOR --------")
        nombre = input("Introduce nombre: ")
        edad = input("Introduce edad: ")
        while (edad.isdigit()==False):
            edad = input("Introduce edad [NUMERICA]: ")
        altura = input("Introduce altura [CM no decimal]: ")
        while (altura.isdigit()==False):
            altura = input("Introduce [CM no decimal]: ")
        peso = input("Introduce peso [sin decimales]: ")
        while (peso.isdigit()==False):
            peso = input("Introduce peso [sin decimales]: ")
        #Guardamos datos
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
        #Imprimimos datos recogidos

    def print_persona(self):
        super().print_persona()
        print(f"Dorsal: {self.dorsal}")

class Entrenador(Persona):
    def __init__(self, nombre, edad, altura, peso):
        super().__init__( nombre, edad, altura, peso)

        self.__equipos=[]

    def add_equipo(self,equipo):
        self.__equipos.append(equipo)

    def print_equipos(self):
        for i in range(len( self.__equipos)):
            print(f"Equipo: {self.__equipos[i].nombre}")

class Tutor(Persona):
    def __init__(self, nombre, edad, altura, peso):
        super().__init__( nombre, edad, altura, peso)

        self.__jugadores = []

    def add_jugador(self,jugador):
        self.__jugadores.append(jugador)

class Directiva(Persona):
    def __init__(self, nombre, edad, altura, peso):
        super().__init__( nombre, edad, altura, peso)

class Equipo:

    def __init__(self,nombre,categoria,entrenador):
        self.nombre=nombre
        self.categoria=categoria
        self.entrenador=entrenador
        #Anaydir el equipo al entrenador
        self.entrenador.add_equipo(self)

        self.__jugadores=[]

    def add_jugador(self,jugador):
        self.__jugadores.append(jugador)

class Menu:
    pass