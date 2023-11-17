import gestorAplicacion
from gestorAplicacion.entidades.Persona import Persona

class Cliente(Persona):
    clientes=[]

    def __init__(self, nombre, edad, sexo, tipo_documento, num_documento, telefono=0, direccion=None, correo=None, idCliente=None, hotel=None, memebresia=None, equipaje=None, habitacion=0):
        super.__init__(nombre, edad, sexo, tipo_documento, num_documento, telefono, direccion, correo)
        self.idCliente=idCliente
        self.nombre = nombre
        self.tipo_documento=tipo_documento
        self.num_documento=num_documento
        self.telefono=telefono
        self.hotel=hotel
        self.membresia=memebresia
        self.equipaje=equipaje
        self.habitacion=habitacion

     
