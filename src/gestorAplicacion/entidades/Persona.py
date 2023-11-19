import gestorAplicacion
#from multimethod import multimethod
from abc import ABC, abstractmethod


class Persona:
#    @multimethod 
    def __init__(self, nombre, edad, sexo, tipo_documento, num_documento, telefono, direccion=None, correo=None):
        self.nombre = nombre
        self.edad=edad
        self.sexo=sexo
        self.tipo_documento=tipo_documento
        self.num_documento=num_documento
        self.telefono=telefono
        self.direccion=direccion
        self.correo=correo
    
#    @multimethod
#    def __init__(self, nombre, tipo_documento, num_documento,  telefono):
#        self.nombre=nombre
#        self.tipo_documento=tipo_documento
#        self.num_documento=num_documento
#        self.telefono=telefono
    
    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_sexo(self):
        return self.sexo

    def get_tipo_documento(self):
        return self.tipo_documento

    def get_num_documento(self):
        return self.num_documento

    def get_telefono(self):
        return self.telefono

    def get_direccion(self):
        return self.direccion

    def get_correo(self):
        return self.correo

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_tipo_documento(self, tipo_documento):
        self.tipo_documento = tipo_documento

    def set_num_documento(self, num_documento):
        self.num_documento = num_documento

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_correo(self, correo):
        self.correo = correo
    
    #metodos abstractos 

    @abstractmethod  
    def __str__():
        pass

    @abstractmethod
    def personaRol():
        pass 
   