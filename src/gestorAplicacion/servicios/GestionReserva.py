class GestionReserva:

    reservas=[]

#constructor
    def __init__(self,cliente=None,habitacion=None,numeroNoches=0, estado=False, hotel=None):
        self._cliente_=cliente
        self._habitacion_=habitacion
        self._nochesEstadia_=numeroNoches
        self._estado_=estado
        self._hotel=hotel
        self._serviciosAdicionales_=[]
        GestionReserva.reservas.append(self)

        if habitacion:
            habitacion.setOcupacion(True)

#metodos get  
    def getCliente(self):
        return self._cliente_
    
    def getHabitacion(self):
        return self._habitacion_
    
    def getEstadia(self):
        return self._nochesEstadia_
    
    def getEstado(self):
        return self._estado_
    
    def getHotel(self):
        return self._hotel
    
    def getServiciosA(self):
        return self._serviciosAdicionales_

    def getFactura(self):
        self.calcularFactura()
        return self._factura_

 #metodos set   
    def setCliente(self, cliente):
        self._cliente_=cliente
    
    def setHabitacion(self, habitacion):
        self._habitacion_=habitacion

    def setEstadia(self, estadia):
        self._nochesEstadia_=estadia

    def setEstado(self, estado):
        self._estado_=estado

    def setHotel(self, hotel):
        self._hotel_=hotel

#metodos de instancia
    def addServicios(self,args):
        for i in args:
            self._serviciosAdicionales_.append(i)
 
    def calcularFactura(self):
        self._factura_= self._nochesEstadia_*self._habitacion_.getPrecio()
        for i in self._serviciosAdicionales_:
            self._factura_+=i.getPrecio()

    def borrarReserva(self):
        GestionReserva.reservas.remove(self)
        self._habitacion_.setOcupacion(False)

#metodo de clase
    @classmethod
    def getReservas(cls):
        return cls.reservas
    
#to Str
    def __str__(self):
        return ("Reservas\n"+
                "  -Cliente: "+self._cliente_.__str__()+"\n"+
                "  -Habitacion: "+self._habitacion_+"\n"+
                "  -Estadia: "+self._nochesEstadia_+" noches\n"+
                "  -Servicios Adivionales: "+self._serviciosAdicionales_+
                "--------------------------------------------------------\n")