'''
Getter y Setter
 Los métodos getters y setters son funciones que
permiten obtener y establecer el valor de un atributo
de una clase, respectivamente.
 Se utilizan para agregar lógica adicional al acceso de
los atributos, como validación o transformación de
datos

'''


class Persona:
    def __init__(self, nombre, edad, edadSucia):
        self.__nombre = nombre
        self.__edad = edad
        self.edadSucia = edadSucia
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de texto")

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        if isinstance(edad, int) and edad > 0:
            self._edad = edad
        else:
            raise ValueError("La edad debe ser un número entero positivo")

paco = Persona ("Paco",49,-5)
print(edadSucia)
print(paco.get.edad())
paco.edadSucia = -2
paco.set_edad(-2)