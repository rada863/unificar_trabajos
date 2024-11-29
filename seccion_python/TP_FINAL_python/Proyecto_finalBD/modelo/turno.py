from modelo.medico import Medico
from modelo.paciente import Paciente

class Turno:
    def __init__(self, id_turno: int, id_paciente: int, id_medico: int, fecha_hora: str, estado: str = 'Programado'):
        if not isinstance(id_turno, int):
            raise ValueError("El 'id_turno' debe ser un entero")
        if not isinstance(id_paciente, int):
            raise ValueError("El 'id_paciente' debe ser un entero")
        if not isinstance(id_medico, int):
            raise ValueError("El 'id_medico' debe ser un entero")
        if not isinstance(fecha_hora, str) or not fecha_hora.strip():
            raise ValueError("La 'fecha_hora' debe ser una cadena no vacía")
        if not isinstance(estado, str) or not estado.strip():
            raise ValueError("El 'estado' debe ser una cadena no vacía")
        
        self._id_turno = id_turno
        self._id_paciente = id_paciente
        self._id_medico = id_medico
        self._fecha_hora = fecha_hora.strip()
        self._estado = estado.strip()
    
    
    def obtener_id_turno(self):
        return self._id_turno

    def obtener_id_paciente(self):
        return self._id_paciente

    def obtener_id_medico(self):
        return self._id_medico

    def obtener_fecha_hora(self):
        return self._fecha_hora

    def obtener_estado(self):
        return self._estado
