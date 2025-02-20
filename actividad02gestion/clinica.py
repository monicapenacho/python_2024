
import os
import re

class Clinica:
    '''
    Clase Clinica. Permite gestionar una clínica médica

    ATRIBUTOS DE CLASE
    ------------------
    nombre : str
        Define el nombre de la clínica
    '''


    def __init__(self, nombre="CLINICA PENACHO"):
        '''
        Constructor: El método init es el llamado a crear el objeto
        '''
        self.nombre = nombre
        '''
        Atributo de instancia
        '''
        pass

class Persona:
    '''
    Clase Persona. Define un elemento de tipo Persona. Representa a una persona en la clínica

    ATRIBUTOS DE CLASE
    ------------------
    nombre : str
        Nombre de la persona
    edad : int
        Edad de la persona
    dni : str
        Número de DNI y letra

    '''

    def __init__(self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = self.validar_numero(edad, "Edad")
        self.dni = self.validar_dni(dni)

    @staticmethod
    def validar_numero(valor, mensaje):
        while True:
            try:
                return int(valor)
            except ValueError:
                valor = input(f"{mensaje} inválido. Ingrese un número: ")

    @staticmethod
    def validar_dni(dni):
        patron_dni = r"^\d{8}[A-Za-z]$"
        while not re.match(patron_dni, dni):
            dni = input("DNI inválido. Ingrese un DNI válido (8 números seguidos de una letra): ")
        return dni.upper()

    def informacion_general(self):
        return f"Nombre: {self.nombre}, edad: {self.edad}, dni: {self.dni}"

    def print_persona(self):
        '''
        Función que imprime por pantalla una persona
        '''
        print(f"Nombre: {self.nombre}, edad: {self.edad}, dni: {self.dni}")

class Paciente(Persona):
    '''
    Clase Paciente. Define un elemento de tipo Paciente
    Hereda de Persona

    ATRIBUTOS DE CLASE
    ------------------
    historial_medico : str
        Contiene el historial médico del paciente. Este atributo es específico de la clase Paciente.

    numero_seguro : str
        Número del seguro médico del paciente. Este atributo también es específico de la clase Paciente.
    '''

    def __init__(self, nombre, edad, dni, historial_medico="", numero_seguro=""):
        '''
        Método constructor de la clase Paciente. Inicializa los atributos heredados de la clase Persona
        y los atributos específicos de la clase Paciente (historial_medico y numero_seguro).
        '''
        # Llamamos al constructor de la clase padre (Persona) para inicializar los atributos comunes (nombre, edad, dni).
        super().__init__(nombre, edad, dni)

        # Inicializamos los atributos específicos de la clase Paciente.
        self.historial_medico = historial_medico
        self.numero_seguro = numero_seguro

    def nuevo_paciente(self):
        '''
        Imprimimos por consola el menú para recoger los datos del nuevo paciente
        '''
        print("-------- NUEVO PACIENTE --------")
        nombre = input("Introduce nombre: ")
        edad = input("Introduce edad: ")
        while (edad.isdigit()==False):
            edad = input("Introduce edad [NUMERICA]: ")
        dni = input("Introduce dni: ")
        historial_medico = input("Introduce historial medico: ")
        numero_seguro = input("Introduce numero de seguro: ")

        #Guardamos datos
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.historial_medico = historial_medico
        self.numero_seguro = numero_seguro

        #Imprimimos datos recogidos
    def print_persona(self):
        super().print_persona()
        print(f"historial: {self.historial_medico}, seguro: {self.numero_seguro}")

    def detalles_paciente(self):
        return super().informacion_general() + f", Historial: {self.historial_medico}, Seguro: {self.numero_seguro}"

class Doctor(Persona):
    def __init__(self, nombre, edad, dni, especialidad, numero_colegiado):
        super().__init__(nombre, edad, dni)
        self.especialidad = especialidad
        self.numero_colegiado = numero_colegiado
        self.__pacientes = []  # Lista de pacientes para este doctor

    def add_paciente(self,paciente):
        self.__pacientes.append(paciente)

    def print_pacientes(self):
        for i in range(len( self.__pacientes)):
            print(f"Paciente: {self.__pacientes[i].nombre}")

    def informacion_doctor(self):
        return super().informacion_general() + f", Especialidad: {self.especialidad}, Nº Colegiado: {self.numero_colegiado}"

class Enfermero(Persona):
    def __init__(self, nombre, edad, dni, turno, hospital_asignado):
        super().__init__(nombre, edad, dni)
        self.turno = turno
        self.hospital_asignado = hospital_asignado

    def datos_enfermero(self):
        return super().informacion_general() + f", Turno: {self.turno}, Hospital: {self.hospital_asignado}"

class Administrador(Persona):
    def __init__(self, nombre, edad, dni, rol_sistema):
        super().__init__(nombre, edad, dni)
        self.rol_sistema = rol_sistema

    def perfil_administrador(self):
        return super().informacion_general() + f", Nivel de Acceso: {self.rol_sistema}"

class Cita:
    '''
    Representa una cita médica
    '''
    def __init__(self, paciente, doctor, fecha, hora):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora

    def descripcion_cita(self):
        return f"Cita - Paciente: {self.paciente.nombre}, Doctor: {self.doctor.nombre}, Fecha: {self.fecha}, Hora: {self.hora}"

class HistorialMedico:
    '''
    Clase independiente que maneja el historial médico de los pacientes
    '''

    def __init__(self):
        self.historial = {}

    def agregar_diagnostico(self, dni, diagnostico):
        if dni not in self.historial:
            self.historial[dni] = []
        self.historial[dni].append(diagnostico)

    def obtener_historial(self, dni):
        return self.historial.get(dni, "Sin historial disponible")


class Menu:
    '''
    Clase que representa el menú de la aplicación
    '''

    def __init__(self, nombre, gestor):
        self.nombre = nombre
        self.gestor = gestor

    def mostrar_menu(self):
        '''
        Muestra el menú principal de la aplicación

        RETURN
        ------
        opcion: int
            Entero  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8
        '''
        os.system("cls")  # Limpiamos la pantalla en sistemas Windows
        print(f"-------- GESTOR {self.nombre} --------")
        print("[1] REGISTRAR PACIENTE")
        print("[2] REGISTRAR DOCTOR")
        print("[3] REGISTRAR ENFERMERO")
        print("[4] REGISTRAR ADMINISTRADOR")
        print("[5] AGENDAR CITA")
        print("[6] VER HISTORIAL MÉDICO")
        print("[7] GENERAR INFORMES")
        print("[8] SALIR")

        opcion = input("Introduce opción [1|2|3|4|5|6|7|8]: ")
        opcion_incorrecta=True
        while(opcion_incorrecta):
            if not opcion.isdigit():
                opcion = input("Introduce opción [1|2|3|4|5|6|7|8]: ")
                continue
            if not int(opcion) in [1,2,3,4,5,6,7,8]:
                opcion = input("Introduce opción [1|2|3|4|5|6|7|8]: ")
                continue
            opcion_incorrecta = False

        return opcion



