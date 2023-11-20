from gestorAplicacion.servicios.Habitacion import  Habitacion
from gestorAplicacion.servicios.Hotel import Hotel
from gestorAplicacion.servicios.Servicio import Servicio
from capaPersistencia.serializador import Serializador
from capaPersistencia.deserializador import Deserializador

if __name__=="__main__":
    serv1= Servicio("Desayuno", 2.99, "6:00", "10:00")
    serv2= Servicio("Actividad tematica", 6.99, "10:00", "15:30")
    serv3= Servicio("Sesion de masaje", 10.50)

    hotel1= Hotel("Sol caribe", "<direccion>")
    hotel1.setComentarios("muy bueno", "excelente")
    hotel1.setServicios(Servicio.getServicios())
    hotel1.setCalificacion(4.0)

    for i in range(6):
        hab= Habitacion(hotel1,(100+i),4,100, "estandar", False)
        hotel1.addHabitaciones(hab)

    #interfaz grafica de usuario aqui:
    
