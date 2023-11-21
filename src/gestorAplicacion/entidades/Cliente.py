import gestorAplicacion
from gestorAplicacion.servicios.Pago import Pago
from gestorAplicacion.entidades.Persona import Persona
from gestorAplicacion.servicios.Servicio import Servicio
from typing import List
from datetime import datetime

class Cliente(Persona):
    clientes=[]

    def __init__(self, nombre, tipo_cedula, numero_cedula, telefono, idCliente=0, hotel=None, membresia=None, equipaje=None, habitacion=None):
        super().__init__(nombre, tipo_cedula, numero_cedula, telefono)
        self.idCliente = idCliente
        self.hotel = hotel
        self.puntos = 0
        self.membresia = membresia
        self.equipaje = equipaje
        self.habitacion = habitacion
        Cliente.addClientes(self)
        self.historial = []
        self.historiaComentario = ""
        self.reserva = None
        self.pagoCliente = None

    def solicitarServicio(self, servicio):
        self.reserva.aggServicio(Servicio.getServicios()[servicio])
        self.puntos += 1

    def cancelarServicio(self, servicio):
        del self.reserva.getServiciosAdicionales()[servicio]
        self.puntos -= 1

    @staticmethod
    def cargarClientes(cargaClientes):
        Cliente.clientes = cargaClientes

    def realizarReserva(self, reserva):
        self.reserva = reserva
        self.historial.append(reserva)
        self.puntos += 20

    def consultaReserva(self):
        return str(self.reserva)

    def cancelarReserva(self, reserva):
        if not self.historial:
            return False
        reserva.borrarReserva()
        self.historial.pop()
        self.reserva = None
        self.puntos -= 20
        return True

    def generarFactura(self):
        pagoReserva = self.habitacion.getPrecioxNoche() * self.reserva.getNochesXEstadia()
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        self.pagoCliente = Pago(pagoReserva, self.reserva.getServiciosAdicionales(), fecha_actual)
        if self.puntosRedimidos:
            self.pagoCliente.setDescuentoPuntos(self.getPuntos())
        return self.pagoCliente

    def getPagoCliente(self):
        return self.pagoCliente

    def redimirPuntos(self):
        self.puntosRedimidos = True

    def pagarFactura(self):
        self.reserva.setEstado(True)

    def getPuntos(self):
        return self.puntos
    
    @staticmethod
    def getClienteByNombre(nombre):
        for cliente in Cliente.clientes:
         if cliente.getNombre() == nombre:
            return cliente
        return None


    @staticmethod
    def getClientes():
        return Cliente.clientes

    @staticmethod
    def getClienteById(id):
        for cliente in Cliente.clientes:
            if cliente.getNum_documento() == id:
                return cliente
        return None

    @staticmethod
    def addClientes(cliente):
        Cliente.clientes.append(cliente)

    def __str__(self):
        return f"Cliente\nidCliente: {self.idCliente}\nNombre: {self.getNombre()}\nCC: {self.getNum_documento()}\nPuntos: {self.getPuntos()}"

    def personaRol(self):
        return "Cliente"


     
