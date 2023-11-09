class Habitacion:
    def __init__(self,hotel=None,numHabitacion=0,capacidad=0,precio=0,tipo=None,ocupacion=False):
        self._hotel_=hotel
        self._numHabitacion_=numHabitacion
        self._capacidad_=capacidad
        self._precio_=precio
        self._tipo_=tipo
        self._ocupacion_=ocupacion

    def getHotel(self):
        return self._hotel_

    def getNumero(self):
        return self._numHabitacion_
    
    def getCapacidad(self):
        return self._capacidad_
    
    def getPrecio(self):
        return self._precio_
    
    def getTipo(self):
        return self._tipo_
    
    def getOcupacion(self):
        return self._ocupacion_