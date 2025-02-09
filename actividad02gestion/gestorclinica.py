import json
import os
from clinica import Clinica, Persona, Paciente, Doctor, Enfermero, Administrador, Cita, HistorialMedico, Menu

os.system('cls')

clinica = Clinica()
historial_medico = HistorialMedico()
pacientes = []
doctores = []
enfermeros = []
administradores = []
citas = []

def dni_duplicado(dni):
    '''
    Verifica si el DNI ya está registrado en pacientes, doctores, enfermeros o administradores
    '''
    return any(p.dni == dni for p in pacientes) or \
           any(d.dni == dni for d in doctores) or \
           any(e.dni == dni for e in enfermeros) or \
           any(a.dni == dni for a in administradores)
class GestorDatos:
    ARCHIVO_DATOS = "datos_clinica.json"

    def __init__(self):
        self.pacientes = []
        self.doctores = []
        self.enfermeros = []
        self.administradores = []
        self.citas = []
        self.cargar_datos()

    def guardar_datos(self):
        '''
        Guarda los datos en un archivo JSON
        '''
        datos = {
            "pacientes": [vars(p) for p in self.pacientes],
            "doctores": [vars(d) for d in self.doctores],
            "enfermeros": [vars(e) for e in self.enfermeros],
            "administradores": [vars(a) for a in self.administradores],
            "citas": [self.serializar_cita(c) for c in self.citas]
        }
        with open(self.ARCHIVO_DATOS, "w") as f:
            json.dump(datos, f, indent=4)

    def cargar_datos(self):
        '''
        Carga los datos almacenados en JSON
        '''
        if os.path.exists(self.ARCHIVO_DATOS):
            with open(self.ARCHIVO_DATOS, "r") as f:
                try:
                    datos = json.load(f)
                    self.pacientes = [Paciente(**p) for p in datos.get("pacientes", [])]
                    self.doctores = [Doctor(**d) for d in datos.get("doctores", [])]
                    self.enfermeros = [Enfermero(**e) for e in datos.get("enfermeros", [])]
                    self.administradores = [Administrador(**a) for a in datos.get("administradores", [])]
                    self.citas = [Cita(**c) for c in datos.get("citas", [])]
                except json.JSONDecodeError:
                    print("⚠️ Error al cargar datos: Archivo JSON corrupto o vacío.")

    def serializar_cita(self, cita):
        '''
        Convierte un objeto cita en un formato serializable para JSON
        '''
        return {
            "paciente": vars(cita.paciente),
            "doctor": vars(cita.doctor),
            "fecha": cita.fecha,
            "hora": cita.hora
        }

    def generar_informes(self):
        '''
        Incluye 4 algoritmos de cálculo
        '''
        print("\n--- INFORMES ---")
        print(f"Total de pacientes: {len(self.pacientes)}")
        print(f"Total de doctores: {len(self.doctores)}")
        print(f"Total de enfermeros: {len(self.enfermeros)}")
        print(f"Total de citas agendadas: {len(self.citas)}")

gestor = GestorDatos()
menu = Menu(clinica.nombre, gestor)

def registrar_paciente():
    '''
    Registra un nuevo paciente
    '''
    nombre = input("Nombre del paciente: ")
    edad = input("Edad: ")
    while not edad.isdigit():
        edad = input("Edad inválida. Ingrese una edad numérica: ")
    # Validar y evitar DNI duplicado
    while True:
        dni = input("DNI: ")
        dni = Persona.validar_dni(dni)  # Validación del formato DNI

        # Comprobar si el DNI ya está en la lista de pacientes
        if any(p.dni == dni for p in pacientes):
            print("Error: El DNI ya está registrado. Intente con otro.")
        else:
            break  # Si no está duplicado, salir del bucle
    numero_seguro = input("Número de seguro: ")
    paciente = Paciente(nombre, edad, dni, "", numero_seguro)
    pacientes.append(paciente)
    gestor.pacientes.append(paciente)
    print("Paciente registrado con éxito.")

def registrar_doctor():
    '''
    Registra un nuevo doctor
    '''
    nombre = input("Nombre del doctor: ")
    edad = input("Edad: ")
    while not edad.isdigit():
        edad = input("Edad inválida. Ingrese una edad numérica: ")
    # Validar y evitar DNI duplicado
    while True:
        dni = input("DNI: ")
        dni = Persona.validar_dni(dni)  # Validación del formato DNI

        # Comprobar si el DNI ya está en la lista de doctores
        if any(d.dni == dni for d in doctores) or any(p.dni == dni for p in pacientes):
            print("Error: El DNI ya está registrado. Intente con otro.")
        else:
            break  # Si no está duplicado, salir del bucle
    especialidad = input("Especialidad: ")
    numero_colegiatura = input("Número de colegiatura: ")
    doctor = Doctor(nombre, edad, dni, especialidad, numero_colegiatura)
    doctores.append(doctor)
    gestor.doctores.append(doctor)
    print("Doctor registrado con éxito.")

def registrar_enfermero():
    '''
    Registra un nuevo enfermero
    '''
    nombre = input("Nombre del enfermero: ")
    edad = input("Edad: ")
    while not edad.isdigit():
        edad = input("Edad inválida. Ingrese una edad numérica: ")
    # Validar y evitar DNI duplicado
    while True:
        dni = input("DNI: ")
        dni = Persona.validar_dni(dni)  # Validación del formato DNI

        # Comprobar si el DNI está duplicado
        if dni_duplicado(dni):  #Verifica si ya existe en cualquier lista
            print("Error: El DNI ya está registrado en otra persona. Intente con otro.")
        else:
            break  # Si no está duplicado, salir del bucle
    turno = input("Turno del enfermero: ")
    hospital_asignado = input("Hospital asignado: ")
    enfermero = Enfermero(nombre, edad, dni, turno, hospital_asignado)
    enfermeros.append(enfermero)
    gestor.enfermeros.append(enfermero)
    print("Enfermero registrado con éxito.")

def registrar_administrador():
    '''
    Registra un nuevo administrador
    '''
    nombre = input("Nombre del administrador: ")
    edad = input("Edad: ")
    while not edad.isdigit():
        edad = input("Edad inválida. Ingrese una edad numérica: ")
    # Validar y evitar DNI duplicado
    while True:
        dni = input("DNI: ")
        dni = Persona.validar_dni(dni)  # Validación del formato DNI

        # Comprobar si el DNI está duplicado
        if dni_duplicado(dni):  # Verifica si ya existe en cualquier lista
            print("Error: El DNI ya está registrado en otra persona. Intente con otro.")
        else:
            break  # Si no está duplicado, salir del bucle
    rol_sistema = input("Rol del administrador: ")
    administrador = Administrador(nombre, edad, dni, rol_sistema)
    administradores.append(administrador)
    gestor.administradores.append(administrador)
    print("Administrador registrado con éxito.")

def agendar_cita():
    '''
    Agenda una cita entre paciente y doctor
    '''
    if not pacientes or not doctores:
        print("Debe haber al menos un paciente y un doctor registrados.")
    else:
        print("Lista de pacientes:")
        for i, paciente in enumerate(pacientes):
            print(f"{i+1}. {paciente.detalles_paciente()}")
        paciente_idx = int(input("Seleccione el número del paciente: ")) - 1

        print("Lista de doctores:")
        for i, doctor in enumerate(doctores):
            print(f"{i+1}. {doctor.informacion_doctor()}")
        doctor_idx = int(input("Seleccione el número del doctor: ")) - 1

        fecha = input("Fecha de la cita (YYYY-MM-DD): ")
        hora = input("Hora de la cita (HH:MM): ")
        cita = Cita(pacientes[paciente_idx], doctores[doctor_idx], fecha, hora)
        citas.append(cita)
        print("Cita agendada con éxito.")

def ver_historial():
    '''
    Muestra el historial médico de un paciente
    '''
    dni = input("Ingrese el DNI del paciente: ")
    print(historial_medico.obtener_historial(dni))

# Menú principal
while True:
    opcion = menu.mostrar_menu()

    if opcion == "1":
        print("Función registrar_paciente() llamada")
        registrar_paciente()
        input("\nPresione Enter para continuar...")
    elif opcion == "2":
        registrar_doctor()
        input("\nPresione Enter para continuar...")
    elif opcion == "3":
        registrar_enfermero()
        input("\nPresione Enter para continuar...")
    elif opcion == "4":
        registrar_administrador()
        input("\nPresione Enter para continuar...")
    elif opcion == "5":
        agendar_cita()
        input("\nPresione Enter para continuar...")
    elif opcion == "6":
        ver_historial()
        input("\nPresione Enter para continuar...")
    elif opcion == "7":
        menu.gestor.generar_informes()
        input("\nPresione Enter para continuar...")
    elif opcion == "8":
        menu.gestor.guardar_datos()
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")



