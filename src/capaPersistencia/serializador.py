import pickle
from gestorAplicacion.entidades import Persona,Cliente,Empleado
from gestorAplicacion.servicios import GestionReserva,Habitacion,Hotel,Pago,Servicio

class Serializador:

    def serializar():
        pklEntidades= open("src/capaPersistencia/temp/personas.pkl","wb")
        pklServicios= open("src/capaPersistencia/temp/servicios.pkl","wb")
        
        hoteles=Hotel.Hotel.getHoteles()
        reservas= GestionReserva.GestionReserva.getReservas()
        #clientes= Cliente.Cliente.getClientes()
        #empleados= Empleado.Empleado.getEmpleados()

        for i in hoteles:
            pickle.dump(i, pklServicios)
        
        for i in reservas:
            pickle.dump(i, pklServicios)

        #for i in empleados:
        #    pickle.dump(i, pklEntidades)

        #for i in clientes:
        #    pickle.dump(i, pklEntidades)

        #nota, cada clase debe tener una lista como atributo de clase en donde almacene las instancias a medida que se creen

        pklEntidades.close()
        pklServicios.close()
        print("serializacion exitosa")
