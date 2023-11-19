from gestorAplicacion import gestorAplicacion

class Hotel:
    hoteles=[]

    def __init__(self, nombre="", direccion="", tarifas=[], servicios=[], comentarios="", calificacion=0):
        self._nombre_=nombre
        self._direccion_=direccion
        self._tarifas_=tarifas
        self._servicios_=servicios
        self._habitaciones_=[]
        self._comentarios_=comentarios
        self._calificacion_=calificacion
        self._numCalificaciones_=0
        Hotel.hoteles.append(self)

    #metodos get
    def getNombre(self):
        return self._nombre_
    
    def getDireccion(self):
        return self._direccion_
    
    def getTarifas(self):
        return self._tarifas_
    #metodos set
    def setNombre(self,nombre):
        self._nombre_=nombre
     
    def setDireccion(self,direccion):
        self._direccion_=direccion

    def setTarifas(self, tarifas):
        self._tarifas_= tarifas

    def setServicios(self, servicios):
        self._servicios_=servicios

    def setComentarios(self, args):
        for i in args:
            self._comentarios_.append(i)

    def setCalificacion(self, calificacion):
        self._calificacion_=calificacion
    
    #metodos de instacia
    def addResena(self, comentario, calificacion):
        self._comentarios_=[comentario]
        self._numCalificaciones_+=1
        self._calificacion_= (self._calificacion_ + calificacion)/2

    def addHabitaciones(self, habitacion):
        self._habitaciones_.append(habitacion)
        self.setTarifas(habitacion.getPrecio())

    #cls method
    @classmethod
    def getHoteles(cls):
        return cls.hoteles
    
    def __str__(self):
        return "asdfghj"