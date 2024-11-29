from database import create_tables
from util.helper import generate_initial_data
from controller.paciente_controller import (
    registrar_paciente,
    actualizar_paciente,
    ver_paciente,
    eliminar_paciente
)
from controller.medico_controller import (
    agregar_medico,
    actualizar_medico,
    ver_medico
)
from controller.turno_controller import (
    programar_turno,
    actualizar_turno,
    cancelar_turno,
    reporte_turnos_medicos,
    cancelar_turnos_medico_rango
)
from controller.busqueda_controller import (
    buscar_paciente,
    buscar_medico
)

def main_menu():
    while True:
        print("""
=== Sistema de Gestión de Hospital ===
1. Gestión de Pacientes
2. Gestión de Doctores
3. Manejo de Turnos
4. Búsquedas Avanzadas
5. Reporte de Turnos
6. Cancelación de Turnos
7. Salir
""")
        choice = input("Seleccione una opción: ")
        if choice == '1':
            gestion_pacientes()
        elif choice == '2':
            gestion_doctores()
        elif choice == '3':
            manejo_turnos()
        elif choice == '4':
            busquedas_avanzadas()
        elif choice == '5':
            reporte_turnos()
        elif choice == '6':
            cancelacion_turnos()
        elif choice == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

def gestion_pacientes():
    while True:
        print("""
--- Gestión de Pacientes ---
1. Registrar Paciente
2. Actualizar Paciente
3. Ver Paciente
4. Eliminar Paciente
5. Volver
""")
        choice = input("Seleccione una opción: ")
        if choice == '1':
            registrar_paciente()
        elif choice == '2':
            actualizar_paciente()
        elif choice == '3':
            ver_paciente()
        elif choice == '4':
            eliminar_paciente()
        elif choice == '5':
            break
        else:
            print("Opción no válida.")

def gestion_doctores():
    while True:
        print("""
--- Gestión de Doctores ---
1. Agregar Doctor
2. Actualizar Doctor
3. Ver Doctor
4. Volver
""")
        choice = input("Seleccione una opción: ")
        if choice == '1':
            agregar_medico()
        elif choice == '2':
            actualizar_medico()
        elif choice == '3':
            ver_medico()
        elif choice == '4':
            break
        else:
            print("Opción no válida.")

def manejo_turnos():
    while True:
        print("""
--- Manejo de Turnos ---
1. Programar Turno
2. Actualizar Turno
3. Cancelar Turno
4. Volver
""")
        choice = input("Seleccione una opción: ")
        if choice == '1':
            programar_turno()
        elif choice == '2':
            actualizar_turno()
        elif choice == '3':
            cancelar_turno()
        elif choice == '4':
            break
        else:
            print("Opción no válida.")

def busquedas_avanzadas():
    while True:
        print("""
--- Búsquedas Avanzadas ---
1. Buscar Paciente
2. Buscar Doctor
3. Volver
""")
        choice = input("Seleccione una opción: ")
        if choice == '1':
            buscar_paciente()
        elif choice == '2':
            buscar_medico()
        elif choice == '3':
            break
        else:
            print("Opción no válida.")

def reporte_turnos():
    reporte_turnos_medicos()

def cancelacion_turnos():
    cancelar_turnos_medico_rango()

if __name__ == '__main__':
    create_tables()
    generate_initial_data()
    main_menu()
