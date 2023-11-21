import tkinter as tk
from tkinter import messagebox
from gestorAplicacion.entidades.Cliente import Cliente

class InterfazClienteInfo:
    def __init__(self, root):
        self.root = root
        self.root.title("Información del Cliente")

        # Variable para almacenar el nombre del cliente
        self.nombre_var = tk.StringVar()

        # Etiqueta y campo de entrada para el nombre del cliente
        tk.Label(root, text="Nombre del Cliente:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.nombre_var).grid(row=0, column=1, padx=10, pady=5)

        # Botón para obtener la información del cliente
        tk.Button(root, text="Obtener Información", command=self.obtener_informacion).grid(row=1, column=0, columnspan=2, pady=10)

        # Área de texto para mostrar la información del cliente
        self.info_text = tk.Text(root, height=10, width=50)
        self.info_text.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        # Botones para acciones adicionales
        tk.Button(root, text="Cancelar Reserva", command=self.cancelar_reserva).grid(row=3, column=0, pady=10)
        tk.Button(root, text="Cancelar Servicio", command=self.cancelar_servicio).grid(row=3, column=1, pady=10)
        tk.Button(root, text="Consultar Puntos", command=self.consultar_puntos).grid(row=4, column=0, columnspan=2, pady=10)
    
    def iniciar(self):
            self.root.mainloop()

    def obtener_informacion(self):
        nombre_cliente = self.nombre_var.get()

        if nombre_cliente:
            self.cliente_encontrado = Cliente.getClienteByNombre(nombre_cliente)

            if self.cliente_encontrado:
                # Mostrar información del cliente en el área de texto
                info_cliente = str(self.cliente_encontrado)
                self.info_text.delete(1.0, tk.END)  # Limpiar el área de texto
                self.info_text.insert(tk.END, info_cliente)
            else:
                messagebox.showerror("Error", f"No se encontró un cliente con el nombre {nombre_cliente}")
        else:
            messagebox.showerror("Error", "Por favor, ingrese el nombre del cliente.")

    def cancelar_reserva(self):
        r=self.cliente_encontrado.reserva
        self.cliente_encontrado.cancelarReserva(r)


    def cancelar_servicio(self):
       e=self.cliente_encontrado.reserva
       s=e._serviciosAdicionales_[-1]
       self.cliente_encontrado.cancelarServicio(s)

    def consultar_puntos(self):
        p=self.cliente_encontrado.getPuntos()
        messagebox.showinfo("Puntos del Cliente", f"Total de puntos: {p}")
        