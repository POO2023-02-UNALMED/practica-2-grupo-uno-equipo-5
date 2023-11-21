import pickle
#from src.gestorAplicacion.entidades import Persona,Cliente,Empleado
#from src.gestorAplicacion.servicios import GestionReserva,Habitacion,Hotel,Pago,Servicio

class Deserializador:
    @staticmethod
    def deserializar():
        pklEmpleados= open("src/capaPersistencia/temp/empleados.pkl","rb")
        pklClientes= open("src/capaPersistencia/temp/clientes.pkl","rb")
        pklHoteles= open("src/capaPersistencia/temp/hoteles.pkl","rb")


        #pkle= pickle.load(pklEmpleados)
        #pklc= pickle.load(pklClientes)
        pklh= pickle.load(pklHoteles)
 
        pklEmpleados.close()
        pklClientes.close()
        pklHoteles.close()


        result={
            #"empleados": pkle,
            #"clientes": pklc,
            "hoteles": pklh,
            #"reservas": pklr
        }

        return result
    

        