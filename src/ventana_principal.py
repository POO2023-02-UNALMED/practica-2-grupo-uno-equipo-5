import tkinter as tk
from tkinter import ttk, messagebox

class mainWin:
    ventana = tk.Tk()
    ventana.title("Menú Desplegable con Botones")
    ventana.geometry("1000x500")

    # Bloque div con menú desplegable
    hotel_label = tk.Label(ventana, text="Hotel", font=("Helvetica", 24))
    hotel_label.pack(pady=20, padx=0)
    bloque_div = tk.Frame(ventana, width=100, padx=int(ventana.winfo_reqwidth() * 0.7), height=1, bd=1, relief="solid")
    bloque_div.pack(pady=(20, 0), )
    bloque_div2 = tk.Frame(ventana, padx=int(ventana.winfo_reqwidth() * 0.5), width=100, height=100, bd=1, relief="solid")
    bloque_div2.pack()
    notebook = ttk.Notebook(bloque_div2)
    notebook.pack(expand=1, fill="both")

    # Pestaña principal
    pestaña_principal = ttk.Frame(notebook)
    notebook.add(pestaña_principal)

    # Opciones para el menú desplegable
    opciones = ["Archivo", "Salir", "Aplicacion"]

    # Variable de control para la opción seleccionada
    opcion_seleccionada = tk.StringVar()
    opcion_seleccionada.set(opciones[0])

    # Menú desplegable usando tkinter.Menubutton
    menu_desplegable = tk.Menubutton(bloque_div, textvariable=opcion_seleccionada, relief=tk.RAISED)
    menu_desplegable.pack(side="left", fill="y")  # Ajuste aquí para cambiar la altura

    # Crear el menú
    menu = tk.Menu(menu_desplegable, tearoff=0)
    menu_desplegable["menu"] = menu
    menu.add_command(label=opciones[1],command=ventana.destroy)
    menu.add_command(label = opciones[2])
    # Agregar botones al menú

    # Botón Proceso y Consulta sin menú desplegable
    btn_proceso_consulta = tk.Button(bloque_div, text="Proceso y Consulta", command=lambda: mainWin.mostrar_ventana_detalle("Proceso"))
    btn_proceso_consulta.pack(side="left", padx=0, fill="y")
    # Botón Ayuda sin menú desplegable
    btn_ayuda = tk.Button(bloque_div, text="Ayuda", command=lambda: mainWin.opcion_seleccionada("Ayuda"))
    btn_ayuda.pack(side="left", padx=0, fill="y")

    @staticmethod
    def iniciar():
        # Iniciar el bucle de eventos de Tkinter
        mainWin.ventana.mainloop()
    @staticmethod
    def opcion_seleccionada(opcion):
        print(str(opcion))
    
    @staticmethod
    def mostrar_ventana_detalle(tipo):
        # Obtener la pestaña principal
        pestaña_principal = mainWin.notebook.nametowidget(mainWin.notebook.select())

        # Limpiar el contenido actual de la pestaña principal
        for widget in pestaña_principal.winfo_children():
            widget.destroy()

        # Contenido de la pestaña principal
        tk.Label(pestaña_principal, text=f"Nombre del {tipo}", padx=20, pady=10, bd=1, relief="solid").pack()

        tk.Label(pestaña_principal, text=f"Descripción del detalle del {tipo}", padx=100, pady=10, bd=1, relief="solid").pack()

        div_frame = tk.Frame(pestaña_principal, padx=80, pady=20, bd=1, relief="solid")
        div_frame.pack()

        tk.Label(div_frame, text="Criterio").grid(row=0, column=0, padx=5, pady=5)
        entry_criterio = tk.Entry(div_frame)
        entry_criterio.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(div_frame, text="Código").grid(row=1, column=0, padx=5, pady=5)
        entry_codigo = tk.Entry(div_frame, state="readonly")
        entry_codigo.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(div_frame, text="Nombre").grid(row=2, column=0, padx=5, pady=5)
        entry_nombre = tk.Entry(div_frame, state="readonly")
        entry_nombre.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(div_frame, text="Descripción").grid(row=3, column=0, padx=5, pady=5)
        entry_descripcion = tk.Entry(div_frame, state="readonly")
        entry_descripcion.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(div_frame, text="Ubicación").grid(row=4, column=0, padx=5, pady=5)
        entry_ubicacion = tk.Entry(div_frame, state="readonly")
        entry_ubicacion.grid(row=4, column=1, padx=5, pady=5)

        btn_aceptar = tk.Button(div_frame, text="Aceptar", command=lambda: messagebox.showinfo("Aceptar", "Datos aceptados"))
        btn_aceptar.grid(row=5, column=0, padx=5, pady=5)

        btn_cerrar = tk.Button(div_frame, text="Cerrar", command=lambda: mainWin.limpiar_contenido())
        btn_cerrar.grid(row=5, column=1, padx=5, pady=5)


    @staticmethod
    def procesar():
        mainWin.mostrar_ventana_detalle("Proceso")

    def limpiar_contenido():
        # Limpiar el contenido actual de la pestaña principal
        for widget in mainWin.pestaña_principal.winfo_children():
            widget.destroy()
