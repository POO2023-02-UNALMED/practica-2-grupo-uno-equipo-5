import gestorAplicacion
#from multimethod import multimethod
from abc import ABC, abstractmethod


class Persona:
    #@multimethod 
    def __init__(self, nombre, edad, sexo, tipo_documento, num_documento, telefono, direccion=None, correo=None):
        self.nombre = nombre
        self.edad=edad
        self.sexo=sexo
        self.tipo_documento=tipo_documento
        self.num_documento=num_documento
        self.telefono=telefono
        self.direccion=direccion
        self.correo=correo
    
    '''@multimethod
    def __init__(self, nombre, tipo_documento, num_documento,  telefono):
        self.nombre=nombre
        self.tipo_documento=tipo_documento
        self.num_documento=num_documento
        self.telefono=telefono'''
    
    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getSexo(self):
        return self.sexo

    def getTipoDocumento(self):
        return self.tipo_documento

    def geNumDocumento(self):
        return self.num_documento

    def getTelefono(self):
        return self.telefono

    def getDireccion(self):
        return self.direccion

    def getCorreo(self):
        return self.correo

    # Setters
    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setSexo(self, sexo):
        self.sexo = sexo

    def setTipoDocumento(self, tipo_documento):
        self.tipo_documento = tipo_documento

    def setNumDocumento(self, num_documento):
        self.num_documento = num_documento

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setCorreo(self, correo):
        self.correo = correo
    
    #metodos abstractos 

    @abstractmethod  
    def __str__():
        pass

    @abstractmethod
    def personaRol():
        pass 
   