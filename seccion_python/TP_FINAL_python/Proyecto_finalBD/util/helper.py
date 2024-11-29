import random
from datetime import datetime, timedelta
from database import get_connection
import names  # Asegúrate de tener instalado el paquete 'names'

def generate_initial_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Generar 10 pacientes
    for _ in range(10):
        nombre = names.get_first_name()
        apellido = names.get_last_name()
        edad = random.randint(18, 80)
        direccion = f"Calle {random.randint(1, 100)}"
        telefono = f"+54911{random.randint(10000000, 99999999)}"
        email = f"{nombre.lower()}.{apellido.lower()}@example.com"

        cursor.execute("""
            INSERT INTO Paciente (nombre, apellido, edad, direccion, telefono, email)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre, apellido, edad, direccion, telefono, email))

    # Generar 10 médicos
    especialidades = ['Cardiología', 'Neurología', 'Pediatría', 'Dermatología', 'Traumatología']
    for _ in range(10):
        nombre = names.get_first_name()
        apellido = names.get_last_name()
        especialidad = random.choice(especialidades)
        telefono = f"+54911{random.randint(10000000, 99999999)}"
        email = f"dr.{nombre.lower()}.{apellido.lower()}@hospital.com"

        cursor.execute("""
            INSERT INTO Medico (nombre, apellido, especialidad, telefono, email)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, apellido, especialidad, telefono, email))

    conn.commit()

    # Generar turnos
    cursor.execute("SELECT id_paciente FROM Paciente")
    pacientes = cursor.fetchall()
    cursor.execute("SELECT id_medico FROM Medico")
    medicos = cursor.fetchall()

    for paciente in pacientes:
        for _ in range(10):  # 10 turnos por paciente
            id_paciente = paciente[0]
            id_medico = random.choice(medicos)[0]
            fecha_hora = datetime.now() + timedelta(days=random.randint(1, 30))
            fecha_hora_str = fecha_hora.strftime('%Y-%m-%d %H:%M:%S')
            estado = 'Programado'

            cursor.execute("""
                INSERT INTO Turno (id_paciente, id_medico, fecha_hora, estado)
                VALUES (?, ?, ?, ?)
            """, (id_paciente, id_medico, fecha_hora_str, estado))

    conn.commit()
    conn.close()
