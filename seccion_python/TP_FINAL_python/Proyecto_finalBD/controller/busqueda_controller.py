from database import get_connection

def buscar_paciente():
    termino = input("Ingrese nombre, apellido o ID del paciente: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM Paciente
        WHERE nombre LIKE ? OR apellido LIKE ? OR CAST(id_paciente AS TEXT) LIKE ?
    """, (f'%{termino}%', f'%{termino}%', f'%{termino}%'))
    resultados = cursor.fetchall()
    if resultados:
        print("--- Resultados de Búsqueda de Pacientes ---")
        for paciente in resultados:
            print(f"ID: {paciente[0]}, Nombre: {paciente[1]} {paciente[2]}, Edad: {paciente[3]}")
    else:
        print("No se encontraron pacientes.")
    conn.close()

def buscar_medico():
    termino = input("Ingrese nombre, apellido, ID o especialidad del médico: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM Medico
        WHERE nombre LIKE ? OR apellido LIKE ? OR especialidad LIKE ? OR CAST(id_medico AS TEXT) LIKE ?
    """, (f'%{termino}%', f'%{termino}%', f'%{termino}%', f'%{termino}%'))
    resultados = cursor.fetchall()
    if resultados:
        print("--- Resultados de Búsqueda de Médicos ---")
        for medico in resultados:
            print(f"ID: {medico[0]}, Nombre: Dr. {medico[1]} {medico[2]}, Especialidad: {medico[3]}")
    else:
        print("No se encontraron médicos.")
    conn.close()
