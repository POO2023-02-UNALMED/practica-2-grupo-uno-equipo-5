from gestorAplicacion.servicios.GestionReserva import Servicio
from gestorAplicacion.servicios.GestionReserva import ServiciosHotel
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
        self.servicio_var = tk.StringVar()
        self.hora_inicio_var = tk.StringVar()
        self.hora_fin_var = tk.StringVar()

        # Lista de servicios disponibles
        servicios_disponibles = [servicio.value for servicio in ServiciosHotel]

        # Etiqueta y lista desplegable para seleccionar el servicio
        tk.Label(root, text="Servicio:").grid(row=0, column=0, padx=10, pady=5)
        servicio_combobox = ttk.Combobox(root, textvariable=self.servicio_var, values=servicios_disponibles)
        servicio_combobox.grid(row=0, column=1, padx=10, pady=5)
        servicio_combobox.set("Seleccione un servicio")

        # Etiquetas y campos de entrada para la hora de inicio y fin
        tk.Label(root, text="Hora de Inicio:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.hora_inicio_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Hora de Fin:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.hora_fin_var).grid(row=2, column=1, padx=10, pady=5)

        # Botón para enviar la solicitud
        tk.Button(root, text="Enviar Solicitud", command=self.enviar_solicitud).grid(row=3, column=0, columnspan=2, pady=10)

    def enviar_solicitud(self):
        # Obtener los valores ingresados por el usuario
        servicio_enum = ServiciosHotel[self.servicio_var.get()]
        hora_inicio = self.hora_inicio_var.get()
        hora_fin = self.hora_fin_var.get()

        # Verificar si se proporcionó la información necesaria
        if servicio_enum and hora_inicio and hora_fin:
            # Crear un nuevo objeto Servicio con el Enum y los atributos proporcionados
            nuevo_servicio = Servicio(servicio_enum, 0, hora_inicio, hora_fin)

            # Mostrar la información del servicio
            mensaje = str(nuevo_servicio)
            messagebox.showinfo("Solicitud Enviada", mensaje)
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SolicitudServicioApp(root)
    root.mainloop()