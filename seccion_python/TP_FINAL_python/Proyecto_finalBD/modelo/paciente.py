class Paciente:
    def __init__(self, id_paciente:int, nombre:str, apellido:str, edad:int, direccion:str, telefono:str, email:str):
        if not isinstance(id_paciente,int) or id_paciente is None:
            raise ValueError
        if not isinstance(nombre, str) or nombre.strip():
            raise ValueError
        if not isinstance(apellido,str) or apellido.strip():
            raise ValueError
        if not isinstance(edad,int)or edad is None:
            raise ValueError
        if not isinstance(direccion,str)or direccion.strip():
            raise ValueError
        if not isinstance(telefono,str)or telefono.strip():
            raise ValueError
        if not isinstance(email,str)or email.strip() :
            raise ValueError
        
        self._id_paciente = id_paciente
        self._nombre = nombre.strip()
        self._apellido = apellido.strip()
        self._edad = edad
        self._direccion = direccion.strip()
        self._telefono = telefono.strip()
        self._email = email.strip()
    
    def obtener_id_paciente(self):
        return self._id_paciente
    
    def obtener_nombre(self):
        return self._nombre
    
    def obtener_apellido(self):
        return self._apellido
    
    def obtener_edad(self):
        return self._edad
    
    def obtener_direccion(self):
        return self._direccion
    
    def obtener_telefono(self):
        return self._telefono
    
    def obtener_email(self):
        return self._email
    