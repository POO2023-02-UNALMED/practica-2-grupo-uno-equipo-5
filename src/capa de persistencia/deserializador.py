import pickle
from src.gestorAplicacion.entidades import Persona,Cliente,Empleado
from src.gestorAplicacion.servicios import GestionReserva,Habitacion,Hotel,Pago,Servicio

class Deserializador:
    def deserializar():
        pklEntidades= open("src/capa de persistencia/personas.pkl","rb")
        pklServicios= open("src/capa de persistencia/servicios.pkl","rb")

        pklE= pickle.load(pklEntidades)
        pklS= pickle.load(pklServicios)

        pklEntidades.close()
        pklServicios.close()
        