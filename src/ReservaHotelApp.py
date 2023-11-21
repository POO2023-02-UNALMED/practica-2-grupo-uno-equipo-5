from gestorAplicacion.servicios.GestionReserva import GestionReserva
from gestorAplicacion.entidades.Cliente import Cliente
from capaPersistencia.serializador import Serializador
from capaPersistencia.deserializador import Deserializador
import tkinter as tk
from tkinter import messagebox

class ReservaHotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reserva de Hotel")

        # Variables para almacenar la información del cliente
        self.nombre_var = tk.StringVar()
        self.tipo_documento_var = tk.StringVar()
        self.numero_documento_var = tk.StringVar()
        self.telefono_var = tk.StringVar()

        # Variables para almacenar la información de la reserva
        self.habitacion_var = tk.StringVar()
        self.noches_var = tk.StringVar()

        # Etiquetas y campos de entrada para el cliente
        tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.nombre_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Tipo de Documento:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.tipo_documento_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Número de Documento:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.numero_documento_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Teléfono:").grid(row=3, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.telefono_var).grid(row=3, column=1, padx=10, pady=5)

        # Etiquetas y campos de entrada para la reserva
        tk.Label(root, text="Habitación:").grid(row=4, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.habitacion_var).grid(row=4, column=1, padx=10, pady=5)

        tk.Label(root, text="Número de Noches:").grid(row=5, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.noches_var).grid(row=5, column=1, padx=10, pady=5)

        # Botón para realizar la reserva
        tk.Button(root, text="Hacer Reserva", command=self.hacer_reserva).grid(row=6, column=0, columnspan=2, pady=10)

def hacer_reserva(self):
    # Obtener los valores ingresados por el usuario
    nombre_cliente = self.nombre_var.get()
    tipo_documento = self.tipo_documento_var.get()
    numero_documento = self.numero_documento_var.get()
    telefono = self.telefono_var.get()
    habitacion = self.habitacion_var.get()
    noches = self.noches_var.get()

    # Verificar si se proporcionó la información necesaria
    if nombre_cliente and tipo_documento and numero_documento and telefono and habitacion and noches:
        # Buscar una instancia de Cliente con el nombre proporcionado
        cliente_encontrado = Cliente.getClienteByNombre(nombre_cliente)

        # Verificar si se encontró el cliente
        if cliente_encontrado:
            # Crear una instancia de GestionReserva y asignar valores
            reserva = GestionReserva(cliente=cliente_encontrado, habitacion=habitacion, numero_noches=int(noches))
            cliente_encontrado.realizarReserva(reserva)

            mensaje = f"Reserva exitosa\nCliente: {nombre_cliente}\nHabitación: {habitacion}\nNoches: {noches}"
            messagebox.showinfo("Éxito", mensaje)
        else:
            messagebox.showerror("Error", f"No se encontró un cliente con el nombre {nombre_cliente}")
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ReservaHotelApp(root)
    root.mainloop()