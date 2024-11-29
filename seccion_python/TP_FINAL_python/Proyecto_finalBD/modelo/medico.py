class Medico:
    def __init__(self, id_medico:int, nombre:str, apellido:str, especialidad:str, telefono:str, email:str):
        if not isinstance(id_medico,int)or id_medico is None:
            raise ValueError
        if not isinstance(nombre,str) or nombre.strip():
            raise ValueError
        if not isinstance(apellido,str) or apellido.strip():
            raise ValueError
        if not isinstance(especialidad,str) or especialidad.strip():
            raise ValueError
        if not isinstance(telefono,str) or telefono.strip():
            raise ValueError
        if not isinstance(email,str)or email.strip():
            raise ValueError

        self._id_medico = id_medico
        self._nombre = nombre.strip()
        self._apellido = apellido.strip()
        self._especialidad = especialidad.strip()
        self._telefono = telefono.strip()
        self._email = email.strip()
    
    def obtener_id_medico(self):
        return self._id_medico
    
    def obtener_nombre(self):
        return self._nombre
    
    def obtener_apellido(self):
        return self._apellido
    
    def obtener_especialidad(self):
        return self._especialidad
    
    def obtener_telefono(self):
        return self._telefono
    
    def obtener_email(self):
        return self._email
    
