import gestorAplicacion
from gestorAplicacion.entidades.Persona import Persona

class Empleado(Persona):
    empleados=[]

    def __init__(self, nombre, edad, sexo, tipo_documento, num_documento, telefono, direccion, correo, calificacion, IDEmpleado, rol, sueldo):
        super().__init__(nombre, edad, sexo, tipo_documento, num_documento, telefono, direccion, correo)
        self.IDEmpleado = IDEmpleado
        self.rol = rol
        self.sueldo = sueldo
        Empleado.empleados.append(self)

    def getIDEmpleado(self):
        return self.IDEmpleado

    def setIDEmpleado(self, IDEmpleado):
        self.IDEmpleado = IDEmpleado

    def getRol(self):
        return self.rol

    def setRol(self, rol):
        self.rol = rol

    def getSueldo(self):
        return self.sueldo

    def setSueldo(self, sueldo):
        self.sueldo = sueldo

    def personaRol(self):
        return "Hola"

    def ascender(self):
        pass
    
    @classmethod
    def getEmpleados(cls):
        return cls.empleados
    
    
    def __str__(self):
        return f"Empleado\nIDEmpleado: {self.IDEmpleado}\nNombre: {self.getNombre()}\nRol: {self.rol}\nSueldo: {self.sueldo}"

