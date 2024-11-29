from database import get_connection

def programar_turno():
    id_paciente = input("Ingrese el ID del paciente: ")
    id_medico = input("Ingrese el ID del médico: ")
    fecha_hora = input("Ingrese la fecha y hora del turno (YYYY-MM-DD HH:MM): ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Turno (id_paciente, id_medico, fecha_hora, estado)
        VALUES (?, ?, ?, 'Programado')
    """, (id_paciente, id_medico, fecha_hora))
    conn.commit()
    conn.close()
    print("Turno programado exitosamente.")

def actualizar_turno():
    id_turno = input("Ingrese el ID del turno a actualizar: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Turno WHERE id_turno = ?", (id_turno,))
    turno = cursor.fetchone()
    if turno:
        fecha_hora = input(f"Fecha y hora [{turno[3]}]: ") or turno[3]
        estado = input(f"Estado [{turno[4]}]: ") or turno[4]

        cursor.execute("""
            UPDATE Turno SET fecha_hora = ?, estado = ?
            WHERE id_turno = ?
        """, (fecha_hora, estado, id_turno))
        conn.commit()
        print("Turno actualizado exitosamente.")
    else:
        print("Turno no encontrado.")
    conn.close()

def cancelar_turno():
    id_turno = input("Ingrese el ID del turno a cancelar: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Turno WHERE id_turno = ?", (id_turno,))
    turno = cursor.fetchone()
    if turno:
        confirm = input("¿Está seguro que desea cancelar este turno? (s/n): ")
        if confirm.lower() == 's':
            cursor.execute("""
                UPDATE Turno SET estado = 'Cancelado'
                WHERE id_turno = ?
            """, (id_turno,))
            conn.commit()
            print("Turno cancelado exitosamente.")
    else:
        print("Turno no encontrado.")
    conn.close()

def reporte_turnos_medicos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Medico.nombre || ' ' || Medico.apellido AS medico, COUNT(Turno.id_turno) AS total_turnos
        FROM Turno
        INNER JOIN Medico ON Turno.id_medico = Medico.id_medico
        GROUP BY Medico.id_medico
        ORDER BY total_turnos DESC
        LIMIT 3
    """)
    resultados = cursor.fetchall()
    print("--- Médicos con más turnos ---")
    for row in resultados:
        print(f"{row[0]} - {row[1]} turnos")
    conn.close()

def cancelar_turnos_medico_rango():
    id_medico = input("Ingrese el ID del médico: ")
    fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha fin (YYYY-MM-DD): ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Turno
        SET estado = 'Cancelado'
        WHERE id_medico = ? AND DATE(fecha_hora) BETWEEN ? AND ?
    """, (id_medico, fecha_inicio, fecha_fin))
    conn.commit()
    print("Turnos cancelados exitosamente.")
    conn.close()
