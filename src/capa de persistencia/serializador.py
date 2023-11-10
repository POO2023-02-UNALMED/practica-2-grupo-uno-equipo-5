import pickle
from src.gestorAplicacion.entidades import Persona,Cliente,Empleado
from src.gestorAplicacion.servicios import GestionReserva,Habitacion,Hotel,Pago,Servicio

class Serializador:

    def serializar():
        pklEntidades= open("src/capa de persistencia/personas.pkl","wb")
        pklServicios= open("src/capa de persistencia/servicios.pkl","wb")

        #hacer dump de cada servicio (con funciones lambda para que no tarde 3 años en compilar)
        map(lambda i: pickle.dump(i, pklServicios),GestionReserva.getReservas())
        map(lambda i: pickle.dump(i, pklServicios),Habitacion.getHabitaciones())
        map(lambda i: pickle.dump(i, pklServicios),Hotel.getHoteles())
        map(lambda i: pickle.dump(i, pklServicios), Pago.getPagos())
        map(lambda i: pickle.dump(i, pklServicios), Servicio.getServicios)

        #dump de entidades como Persona es abstracta podemos hacer unicamente el dump de sus hijas
        map(lambda i: pickle.dump(i, pklEntidades),Cliente.getPersonas())
        map(lambda i: pickle.dump(i, pklEntidades), Empleado.getEmpleados())

        #nota, cada clase debe tener una lista como atributo de clase en donde almacene las instancias a medida que se creen

        pklEntidades.close()
        pklServicios.close()