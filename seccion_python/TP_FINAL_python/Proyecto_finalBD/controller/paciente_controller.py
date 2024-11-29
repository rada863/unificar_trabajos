from database import get_connection

def registrar_paciente():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Paciente (nombre, apellido, edad, direccion, telefono, email)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nombre, apellido, edad, direccion, telefono, email))
    conn.commit()
    conn.close()
    print("Paciente registrado exitosamente.")

def actualizar_paciente():
    id_paciente = input("Ingrese el ID del paciente a actualizar: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Paciente WHERE id_paciente = ?", (id_paciente,))
    paciente = cursor.fetchone()
    if paciente:
        nombre = input(f"Nombre [{paciente[1]}]: ") or paciente[1]
        apellido = input(f"Apellido [{paciente[2]}]: ") or paciente[2]
        edad = input(f"Edad [{paciente[3]}]: ") or paciente[3]
        direccion = input(f"Dirección [{paciente[4]}]: ") or paciente[4]
        telefono = input(f"Teléfono [{paciente[5]}]: ") or paciente[5]
        email = input(f"Email [{paciente[6]}]: ") or paciente[6]

        cursor.execute("""
            UPDATE Paciente SET nombre = ?, apellido = ?, edad = ?, direccion = ?, telefono = ?, email = ?
            WHERE id_paciente = ?
        """, (nombre, apellido, edad, direccion, telefono, email, id_paciente))
        conn.commit()
        print("Paciente actualizado exitosamente.")
    else:
        print("Paciente no encontrado.")
    conn.close()

def ver_paciente():
    id_paciente = input("Ingrese el ID del paciente: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Paciente WHERE id_paciente = ?", (id_paciente,))
    paciente = cursor.fetchone()
    if paciente:
        print(f"ID: {paciente[0]}")
        print(f"Nombre: {paciente[1]} {paciente[2]}")
        print(f"Edad: {paciente[3]}")
        print(f"Dirección: {paciente[4]}")
        print(f"Teléfono: {paciente[5]}")
        print(f"Email: {paciente[6]}")
    else:
        print("Paciente no encontrado.")
    conn.close()

def eliminar_paciente():
    id_paciente = input("Ingrese el ID del paciente a eliminar: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Paciente WHERE id_paciente = ?", (id_paciente,))
    paciente = cursor.fetchone()
    if paciente:
        confirm = input("¿Está seguro que desea eliminar este paciente? (s/n): ")
        if confirm.lower() == 's':
            cursor.execute("DELETE FROM Paciente WHERE id_paciente = ?", (id_paciente,))
            conn.commit()
            print("Paciente eliminado exitosamente.")
    else:
        print("Paciente no encontrado.")
    conn.close()
