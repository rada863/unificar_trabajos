import sqlite3

DATABASE_NAME = 'hospital.db'

def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    tables = [
        """
        CREATE TABLE IF NOT EXISTS Paciente (
            id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            edad INTEGER,
            direccion TEXT,
            telefono TEXT,
            email TEXT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Medico (
            id_medico INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            especialidad TEXT,
            telefono TEXT,
            email TEXT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Turno (
            id_turno INTEGER PRIMARY KEY AUTOINCREMENT,
            id_paciente INTEGER,
            id_medico INTEGER,
            fecha_hora TEXT,
            estado TEXT,
            FOREIGN KEY(id_paciente) REFERENCES Paciente(id_paciente),
            FOREIGN KEY(id_medico) REFERENCES Medico(id_medico)
        )
        """
    ]

    conn = get_connection()
    cursor = conn.cursor()
    for table in tables:
        cursor.execute(table)
    conn.commit()
    conn.close()
