import pygame
from enum import Enum
from pygame import Surface


#Clase GameObject
#   Atributos
#   - tag
#   - pos_x
#   - pos_y
#   - image
#
#   Metodo
#   - get_image: Devuelve una image de pygame para ese gameobject
#   - get_rect: Devuelve el rectangulo que ocupa este gameobject
class GameObject:

    #constructor
    def __init__(self,tag,screen,pos_x=0,pos_y=0,image="fallenangel.png"):
        print(f"Creando el GameObject {tag}")

        #Atributos de la instancia
        self.tag = tag
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = image

        #Atributos privados
        self.__img = pygame.image.load(self.image)
        self.__img.convert()
        self.__rect = self.__img.get_rect()
        self.__rect.center = pos_x, pos_y
        self.__screen = screen

    #Mover hacia arriba el gameobject
    def move_up(self,y=5):
        #print(self.__rect.y)
        if (self.__rect.top-y) > 0:
            self.__rect.move_ip(0,-y)

    #Mover hacia derecha el gameobject
    def move_right(self,x=5):
        if self.__rect.right+x<self.__screen.get_width():
            self.__rect.move_ip(x,0)

    #Mover hacia izquierda el gameobject
    def move_left(self,x=5):
        if self.__rect.left - x > 0:
            self.__rect.move_ip(-x,0)

    #Mover hacia abajo el gameobject
    def move_down(self,y=5):
        if self.__rect.bottom + y < self.__screen.get_height():
            self.__rect.move_ip(0,y)

    #Funcion que devuelve la imagen del game_object
    def get_image(self):
        return self.__img

    #Funcion que actualiza la imagen del game_object
    def set_image(self,img):
        if isinstance(img, Surface):
            self.__img = img
        else:
            print("Animal!!!!")

    #Funcion que devuelve la imagen del game_object
    def get_rect(self):
        return self.__rect

# Class Character
# Atributo
# - life

class Character(GameObject):
    # constructor
    def __init__(self, tag, screen, pos_x=0, pos_y=0, image="fallenangel.png",life=3):
        super().__init__(tag, screen, pos_x, pos_y, image)

        #Atributo privado
        self.__life=life



    # Funcion comprobacion de la colision entre objetos
    def __comprobar_colision(self,list_gameobjects):
        #Debo excluir de la comprobación al jugador que está en la posición 0
        #WARNING con el tema de la posicion 0
        for i in range(1,len(list_gameobjects)):
            # Si colisiona, no puedo moverlo
            if (list_gameobjects[i].get_rect().colliderect(self.get_rect())):
                return True
        return False

    def move_character_right(self, list_gameobjects, x=5):
        super().move_right(x)
        if self.__comprobar_colision(list_gameobjects):
            super().move_left(x)

    def move_character_left(self, list_gameobjects, x=5):
        super().move_left(x)
        if self.__comprobar_colision(list_gameobjects):
            super().move_right(x)

    def move_character_up(self, list_gameobjects, y=5):
        super().move_up(y)
        if self.__comprobar_colision(list_gameobjects):
            super().move_down(y)

    def move_character_down(self, list_gameobjects, y=5):
        super().move_down(y)
        if self.__comprobar_colision(list_gameobjects):
            super().move_up(y)

# Class Obstacle
# Atributo
# - hurt
class TypeObstacle(Enum):
    FURNITURE = 0
    TRAP = 1

class AmountDamage(Enum):
    LIGHT = 0
    HIGH = 1


class Obstacle(GameObject):
    def __init__(self, tag, screen, pos_x=0, pos_y=0, image="rock.png", type_obstacle=TypeObstacle.FURNITURE):
        super().__init__(tag, screen, pos_x, pos_y, image)

        #Estrutura o condicional ternario
        #self.__hurt = 0 if type_obstacle == TypeObstacle.FURNITURE else 1
        if type_obstacle == TypeObstacle.TRAP :
            self.__damage = AmountDamage.HIGH
        else:
            self.__damage  = AmountDamage.LIGHT


# Class Item
# Atributo
