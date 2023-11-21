from enum import Enum

class ServiciosHotel(Enum):
    RESTAURANTE = "Restaurante"
    SPA = "Spa"
    HABITACION = "Servicio a la Habitación"
    PISCINA = "Piscina"
  

class Servicio:
    servicios = []

    def __init__(self, servicio_enum, precio, horaInicio=None, horaFin=None):
        if isinstance(servicio_enum, ServiciosHotel):
            self._nombre_ = servicio_enum.value  # Nombre del servicio es el valor del Enum
            self._precio_ = precio
            self._horaIni_ = horaInicio
            self._horaFin_ = horaFin
            Servicio.servicios.append(self)
        else:
            raise ValueError("El parámetro 'servicio_enum' debe ser un miembro de la enumeración ServiciosHotel.")
    #metodos get
    def getNombre(self):
        return self._nombre_
    
    def getPrecio(self):
        return self._precio_
    
    def getHorario(self):
        if (self._horaIni_!=None) and (self._horaFin_!=None):
            return "Hora Inicio: "+self._horaIni_+"\nHora finalizacion: "+self._horaFin_
        
    #metodos set
    def setNombre(self,nombre):
        self._nombre_=nombre

    def setPrecio(self, precio):
        self._precio_=precio

    def setHorario(self, horaI, horaF):
        self._horaIni_=horaI
        self._horaFin_=horaF
    
    #metodo cls
    @classmethod
    def getServicios(cls):
        return cls.servicios
    #metodo toString
    def __str__(self):
        return f"Servicio: {self._nombre_}, Precio: {self._precio_}, {self.getHorario()}"