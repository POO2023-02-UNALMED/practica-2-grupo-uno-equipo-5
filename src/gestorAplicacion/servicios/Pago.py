class Pago:
    pagos=[]

    def __init__(self, total, tipoServicio, fecha, medioPago="EFECTIVO"):
        self._total_=total
        self._tipoServicio_=tipoServicio
        self._fecha_=fecha
        self._medioPago_=medioPago

    #metodos get
    def getTotal(self):
        return self._total_
    
    def getTipoServicio(self):
        return self._tipoServicio_
    
    def getFecha(self):
        return self._fecha_
    
    def getMedioPago(self):
        return self._medioPago_
    
    #metodos set

    def setTotal(self, total):
        self._total_=total

    def setTipoServicio(self, tps):
        self._tipoServicio_=tps

    def setFecha(self, fecha):
        self._fecha_=fecha

    def setMedioPago(self, medio):
        self._medioPago_=medio

    #cls method
    @classmethod
    def getPagos(cls):
        return cls.pagos
    
    #toString
    def __str__(self):
        return ""