import os
from clinica import Clinica, Paciente, Doctor, Enfermero, Administrador, Cita, HistorialMedico

os.system('cls')

clinica = Clinica()
historial_medico = HistorialMedico()
pacientes = []
doctores = []
citas = []

def mostrar_menu():
    """Muestra el menú principal de la aplicación"""
    print(f"-------- GESTOR {clinica.nombre} --------")
    print("1. Registrar Paciente")
    print("2. Registrar Doctor")
    print("3. Agendar Cita")
    print("4. Ver Historial Médico")
    print("5. Salir")

def registrar_paciente():
    """Registra un nuevo paciente."""
    nombre = input("Nombre del paciente: ")
    edad = input("Edad: ")
    while not edad.isdigit():
        edad = input("Edad inválida. Ingrese una edad numérica: ")
    dni = input("DNI: ")
    numero_seguro = input("Número de seguro: ")
    paciente = Paciente(nombre, edad, dni, "", numero_seguro)
    pacientes.append(paciente)
    print("Paciente registrado con éxito.")

def registrar_doctor():
    """Registra un nuevo doctor."""
    nombre = input("Nombre del doctor: ")
    edad = input("Edad: ")
    while not edad.isdigit():
        edad = input("Edad inválida. Ingrese una edad numérica: ")
    dni = input("DNI: ")
    especialidad = input("Especialidad: ")
    numero_colegiatura = input("Número de colegiatura: ")
    doctor = Doctor(nombre, edad, dni, especialidad, numero_colegiatura)
    doctores.append(doctor)
    print("Doctor registrado con éxito.")

def agendar_cita():
    """Agenda una cita entre paciente y doctor."""
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
    """Muestra el historial médico de un paciente."""
    dni = input("Ingrese el DNI del paciente: ")
    print(historial_medico.obtener_historial(dni))

# Menú principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_paciente()
    elif opcion == "2":
        registrar_doctor()
    elif opcion == "3":
        agendar_cita()
    elif opcion == "4":
        ver_historial()
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")
