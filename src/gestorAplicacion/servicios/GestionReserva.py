class GestionReserva:
    def __init__(self,cliente=None,habitacion=None,numeroNoches=0, estado=False, hotel=None):
        self._cliente_=cliente
        self._habitacion_=habitacion
        self._nochesEstadia_=numeroNoches
        self._estado_=estado
        self._hotel=hotel
        self._serviciosAdicionales_=[]
        
        #reservas.add(self)
    
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
    
    def calcularFactura(self):
        self._factura_= self._nochesEstadia_*self._habitacion_.getPrecio()
        for i in self._serviciosAdicionales_:
            self._factura_+=i.getPrecio()

    def getFactura(self):
        self.calcularFactura()
        return self._factura_