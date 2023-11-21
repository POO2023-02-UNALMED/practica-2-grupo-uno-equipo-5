import tkinter as tk
from tkinter import Frame
from ffOut import ffOut

class FieldFrame(Frame):
    def __init__(self, master=None, criterios=None):
        super().__init__(master)
        self.master = master
        self.criterios = criterios
        self.entries = []

        self.crear_interfaz()

    def crear_interfaz(self):
        for i, criterio in enumerate(self.criterios):
            # Crear un label
            label = tk.Label(self, text=criterio)
            label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

            # Crear un entry
            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky=tk.E)
            self.entries.append(entry)

        # Botón para obtener los valores
        boton_obtener_valores = tk.Button(self, text="Obtener Valores", command=self.obtener_valores)
        boton_obtener_valores.grid(row=len(self.criterios), columnspan=2, pady=10)

    def obtener_valores(self):
        valores = {criterio: entry.get() for criterio, entry in zip(self.criterios, self.entries)}
        return valores
    

