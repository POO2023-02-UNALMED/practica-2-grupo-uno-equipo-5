import pickle
#from src.gestorAplicacion.entidades import Persona,Cliente,Empleado
#from src.gestorAplicacion.servicios import GestionReserva,Habitacion,Hotel,Pago,Servicio

class Deserializador:
    def deserializar():
        pklEntidades= open("src/capaPersistencia/temp/personas.pkl","rb")
        pklServicios= open("src/capaPersistencia/temp/servicios.pkl","rb")

        #pklE= pickle.load(pklEntidades)
        pklS= pickle.load(pklServicios)

        pklEntidades.close()
        pklServicios.close()
        print("deserializacion exitosa")
        