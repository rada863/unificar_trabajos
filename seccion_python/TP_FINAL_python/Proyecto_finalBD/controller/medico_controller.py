from database import get_connection

def agregar_medico():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    especialidad = input("Especialidad: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Medico (nombre, apellido, especialidad, telefono, email)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, apellido, especialidad, telefono, email))
    conn.commit()
    conn.close()
    print("Doctor agregado exitosamente.")

def actualizar_medico():
    id_medico = input("Ingrese el ID del médico a actualizar: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Medico WHERE id_medico = ?", (id_medico,))
    medico = cursor.fetchone()
    if medico:
        nombre = input(f"Nombre [{medico[1]}]: ") or medico[1]
        apellido = input(f"Apellido [{medico[2]}]: ") or medico[2]
        especialidad = input(f"Especialidad [{medico[3]}]: ") or medico[3]
        telefono = input(f"Teléfono [{medico[4]}]: ") or medico[4]
        email = input(f"Email [{medico[5]}]: ") or medico[5]

        cursor.execute("""
            UPDATE Medico SET nombre = ?, apellido = ?, especialidad = ?, telefono = ?, email = ?
            WHERE id_medico = ?
        """, (nombre, apellido, especialidad, telefono, email, id_medico))
        conn.commit()
        print("Médico actualizado exitosamente.")
    else:
        print("Médico no encontrado.")
    conn.close()

def ver_medico():
    id_medico = input("Ingrese el ID del médico: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Medico WHERE id_medico = ?", (id_medico,))
    medico = cursor.fetchone()
    if medico:
        print(f"ID: {medico[0]}")
        print(f"Nombre: Dr. {medico[1]} {medico[2]}")
        print(f"Especialidad: {medico[3]}")
        print(f"Teléfono: {medico[4]}")
        print(f"Email: {medico[5]}")
    else:
        print("Médico no encontrado.")
    conn.close()
