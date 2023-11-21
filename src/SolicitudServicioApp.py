from gestorAplicacion.servicios.Servicio import Servicio
from gestorAplicacion.servicios.Servicio import ServiciosHotel
from gestorAplicacion.entidades.Cliente import Cliente
from capaPersistencia.serializador import Serializador
from capaPersistencia.deserializador import Deserializador
import tkinter as tk
from tkinter import Tk, messagebox, ttk


class SolicitudServicioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Solicitud de Servicio")

        # Variables para almacenar la información de la solicitud
        self.nombre_var = tk.StringVar()
        self.servicio_var = tk.StringVar()
        self.hora_inicio_var = tk.StringVar()
        self.hora_fin_var = tk.StringVar()

        # Lista de servicios disponibles
        servicios_disponibles = [servicio.value for servicio in ServiciosHotel]

        # Etiqueta y lista desplegable para seleccionar el servicio
        tk.Label(root, text="Nombre del Cliente:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.nombre_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Servicio:").grid(row=1, column=0, padx=10, pady=5)
        servicio_combobox = ttk.Combobox(root, textvariable=self.servicio_var, values=servicios_disponibles)
        servicio_combobox.grid(row=1, column=1, padx=10, pady=5)
        servicio_combobox.set("Seleccione un servicio")

        tk.Label(root, text="Hora de Inicio:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.hora_inicio_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Hora de Fin:").grid(row=3, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.hora_fin_var).grid(row=3, column=1, padx=10, pady=5)

        tk.Button(root, text="Enviar Solicitud", command=self.enviar_solicitud).grid(row=4, column=0, columnspan=2, pady=10)

       
    def enviar_solicitud(self):
        # Obtener los valores ingresados por el usuario
        nombre_cliente = self.nombre_var.get()
        servicio_enum = ServiciosHotel.get(self.servicio_var.get())
        hora_inicio = self.hora_inicio_var.get()
        hora_fin = self.hora_fin_var.get()

        # Verificar si se proporcionó la información necesaria
        if nombre_cliente and servicio_enum and hora_inicio and hora_fin:
            # Utiliza el método estático getClienteByNombre
            cliente_encontrado = Cliente.getClienteByNombre(nombre_cliente)

            # Verifica si se encontró el cliente
            if cliente_encontrado:
                # Si el servicio es "Servicio de Equipaje", mostrar una ventana para ingresar la cantidad
                if servicio_enum == ServiciosHotel.EQUIPAJE:
                    self.solicitar_cantidad_equipaje(cliente_encontrado)
                else:
                    # Obtener la reserva del cliente
                    reserva = cliente_encontrado.reserva
                    if reserva is not None:
                        # Si la reserva existe, crear un nuevo objeto Servicio y agregarlo a la lista de servicios de la reserva
                        servicio = Servicio(servicio_enum, 100, hora_inicio, hora_fin)
                        reserva._serviciosAdicionales_.append(servicio)
                        cliente_encontrado.solicitarServicio(servicio)

                        mensaje = f"Solicitud de servicio:\nCliente: {nombre_cliente}\nServicio: {servicio_enum}\nHora de Inicio: {hora_inicio}\nHora de Fin: {hora_fin}"
                        messagebox.showinfo("Solicitud Enviada", mensaje)
                    else:
                        messagebox.showinfo("Información", f"El cliente {nombre_cliente} no tiene reservas para este servicio.")
            else:
                messagebox.showerror("Error", f"No se encontró un cliente con el nombre {nombre_cliente}")
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def solicitar_cantidad_equipaje(self, cliente):
        # Función para solicitar la cantidad de equipaje mediante una ventana emergente
        cantidad_equipaje_var = tk.StringVar()
        cantidad_equipaje_entry = tk.Entry(self.root, textvariable=cantidad_equipaje_var)
        tk.Label(self.root, text="Cantidad de Equipaje:").grid(row=5, column=0, padx=10, pady=5)
        cantidad_equipaje_entry.grid(row=5, column=1, padx=10, pady=5)
        

        def administrar_servicio_equipaje():
            cantidad_equipaje = cantidad_equipaje_var.get()
            cliente.equipaje=cantidad_equipaje
            mensaje = f"Equipaje llevado a la habitación {cliente.reserva.getHabitacion().getNumero()}"
            messagebox.showinfo("Servicio de Equipaje", mensaje)
            self.root.destroy()

        tk.Button(self.root, text="Administrar Servicio", command=administrar_servicio_equipaje).grid(row=6, column=0, columnspan=2, pady=10)

'''if __name__ == "__main__":
    root = tk.Tk()
    app = SolicitudServicioApp(root)
    root.mainloop()'''