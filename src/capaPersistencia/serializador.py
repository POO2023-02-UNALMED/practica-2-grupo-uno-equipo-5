import pickle


class Serializador:
    @staticmethod
    def serializar(hoteles, empleados, clientes):
        pklEmpleados= open("src/capaPersistencia/temp/empleados.pkl","wb")
        pklClientes= open("src/capaPersistencia/temp/clientes.pkl","wb")
        pklHoteles= open("src/capaPersistencia/temp/hoteles.pkl","wb")

        for i in hoteles:
            print(i)
            pickle.dump(i, pklHoteles)
    

        for i in empleados:
            pickle.dump(i, pklEmpleados)

        for i in clientes:
            pickle.dump(i, pklClientes)

        #nota, cada clase debe tener una lista como atributo de clase en donde almacene las instancias a medida que se creen

        pklHoteles.close()
        pklClientes.close()
        pklEmpleados.close()
        print("serializacion exitosa")
