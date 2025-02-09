# Proyecto: Gestion de Clinica

## Fundamentos de programación actividad número:
2

## Opción seleccionada:
4

## Descripción
Este proyecto es una aplicación para la gestión de pacientes en una clínica. 
Permite manejar la información de pacientes, registrar consultas, gestionar citas y generar informes.

## Estructura del Proyecto
El proyecto está organizado de la siguiente manera:

- `clinica.py`: Contiene la lógica principal de la clínica, incluyendo clases como Clinica, Persona, Paciente, Doctor, Enfermero, Administrador y Cita.
- `gestorclinica.py`: Módulo encargado de la gestión de pacientes.
- `.idea/` y `.vscode/`: Archivos de configuración del entorno de desarrollo.

## Funcionalidades

- Registro de pacientes, doctores, enfermeros y administradores.
- Gestión de citas médicas.
- Validación de datos de entrada (DNI, edad, etc.).
- Persistencia de datos mediante JSON.
- Generación de informes con estadísticas sobre la clínica:
  - Total de pacientes registrados. 
  - Total de doctores registrados. 
  - Total de enfermeros registrados. 
  - Total de citas agendadas.

## Requisitos
Para ejecutar este proyecto, necesitas tener instalado:
- Python 3.x
  - Librerías utilizadas:
            os: Para gestionar operaciones del sistema.
            json: Para guardar y cargar los datos de la clínica en un archivo JSON.
            re: Para validar el formato del DNI.

## Ejecución
Para ejecutar el proyecto, usa el siguiente comando:
python gestorclinica.py

## Repositorio en GitHub
Puedes encontrar el proyecto en GitHub en el siguiente enlace:
[https://github.com/monicapenacho/python_2024/tree/main/actividad02gestion](https://github.com/monicapenacho/python_2024/tree/main/actividad02gestion)

## Autor
**Monica Penacho**

## Fecha entrega
**2025.02.09**


---