import tkinter as tk

from tkinter import Tk, Frame, Menu, Label, Button, Toplevel, messagebox,ttk
from gestorAplicacion.servicios.Servicio import ServiciosHotel

import os
from PIL import Image, ImageTk

from Cliente import Cliente

class cliente_own(Cliente):
    def __init__(self, cliente):
        self.cliente = cliente

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
        tk.Button(root, text="Obtener Información", command=self.obtener_informacion).grid(row=1, column=0,
                                                                                           columnspan=2, pady=10)

        # Área de texto para mostrar la información del cliente
        self.info_text = tk.Text(root, height=10, width=50)
        self.info_text.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        # Botones para acciones adicionales
        tk.Button(root, text="Cancelar Reserva", command=self.cancelar_reserva).grid(row=3, column=0, pady=10)
        tk.Button(root, text="Cancelar Servicio", command=self.cancelar_servicio).grid(row=3, column=1, pady=10)
        tk.Button(root, text="Consultar Puntos", command=self.consultar_puntos).grid(row=4, column=0, columnspan=2,
                                                                                     pady=10)

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
        r = self.cliente_encontrado.reserva
        self.cliente_encontrado.cancelarReserva(r)

    def cancelar_servicio(self):
        e = self.cliente_encontrado.reserva
        s = e._serviciosAdicionales_[-1]
        self.cliente_encontrado.cancelarServicio(s)

    def consultar_puntos(self):
        p = self.cliente_encontrado.getPuntos()
        messagebox.showinfo("Puntos del Cliente", f"Total de puntos: {p}")




def show_signup_window():
    def register():
        try:
            # Obtener los valores ingresados en los Entry
            email = entry_email.get()
            name = entry_name.get()
            age = entry_age.get()
            gender = entry_gender.get()
            tipo_cedula = entry_tipo_cedula.get()
            numero_cedula = entry_numero_cedula.get()
            telefono = entry_telefono.get()

            # Validar que todos los campos estén llenos
            if not (email and name and age and gender and tipo_cedula and numero_cedula and telefono):
                raise ValueError("Por favor, complete todos los campos.")

            # Validar el formato del email
            if "@" not in email or (".com" not in email and ".es" not in email):
                raise ValueError("Formato de email incorrecto. Debe contener '@' y '.com' o '.es'.")

            # Convertir a int y validar el tipo de cédula y teléfono
            numero_cedula = int(numero_cedula)
            telefono = int(telefono)

            # Crear un nuevo objeto Cliente con los valores proporcionados
            nuevo_cliente = Cliente(
                nombre=name, tipo_cedula=tipo_cedula, numero_cedula=numero_cedula,
                sexo=gender, edad=age, telefono=telefono, correo=email
            )
            clientes.append(nuevo_cliente)

            # Aquí puedes hacer algo con el nuevo cliente, como almacenarlo en una lista, base de datos, etc.
            # Por ahora, solo lo imprimiremos.
            print("Nuevo cliente registrado:", nuevo_cliente)

            # Cerrar la ventana de registro después de registrarse
            signup_window.destroy()

        except ValueError as e:
            # Mostrar un mensaje de error específico según el tipo de error
            if "invalid literal for int()" in str(e):
                messagebox.showerror("Error", "Número de cédula y teléfono deben ser solo números.")
            else:
                messagebox.showerror("Error", str(e))
    # Crear la ventana de registro
    signup_window = tk.Toplevel()
    signup_window.title("User Registration")

    # Crear y agregar widgets para el registro
    frame = tk.Frame(signup_window, padx=20, pady=20)
    frame.pack(expand=True)

    label_email = tk.Label(frame, text="Email:")
    label_email.grid(row=0, column=0, sticky="e", pady=5)

    entry_email = tk.Entry(frame)
    entry_email.grid(row=0, column=1, pady=5)

    label_name = tk.Label(frame, text="Name:")
    label_name.grid(row=1, column=0, sticky="e", pady=5)

    entry_name = tk.Entry(frame)
    entry_name.grid(row=1, column=1, pady=5)

    label_age = tk.Label(frame, text="Age:")
    label_age.grid(row=2, column=0, sticky="e", pady=5)

    entry_age = tk.Entry(frame)
    entry_age.grid(row=2, column=1, pady=5)

    label_gender = tk.Label(frame, text="Gender:")
    label_gender.grid(row=3, column=0, sticky="e", pady=5)

    entry_gender = tk.Entry(frame)
    entry_gender.grid(row=3, column=1, pady=5)

    label_tipo_cedula = tk.Label(frame, text="Type of ID:")
    label_tipo_cedula.grid(row=4, column=0, sticky="e", pady=5)

    entry_tipo_cedula = tk.Entry(frame)
    entry_tipo_cedula.grid(row=4, column=1, pady=5)

    label_numero_cedula = tk.Label(frame, text="ID Number:")
    label_numero_cedula.grid(row=5, column=0, sticky="e", pady=5)

    entry_numero_cedula = tk.Entry(frame)
    entry_numero_cedula.grid(row=5, column=1, pady=5)

    label_telefono = tk.Label(frame, text="Phone Number:")
    label_telefono.grid(row=6, column=0, sticky="e", pady=5)

    entry_telefono = tk.Entry(frame)
    entry_telefono.grid(row=6, column=1, pady=5)

    button_register = tk.Button(frame, text="Register", command=register)
    button_register.grid(row=7, column=1, pady=10, sticky="e")

# ... Resto del código .

class Principal():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Menú Desplegable con Botones")
        self.ventana.geometry("1000x500")

        # Bloque div con menú desplegable
        hotel_label = tk.Label(self.ventana, text="Hotel", font=("Helvetica", 24))
        hotel_label.pack(pady=20, padx=0)
        bloque_div = tk.Frame(self.ventana, width=100, padx=int(self.ventana.winfo_reqwidth() * 0.7), height=1, bd=1,
                              relief="solid")
        bloque_div.pack(pady=(20, 0), )
        bloque_div2 = tk.Frame(self.ventana, padx=int(self.ventana.winfo_reqwidth() * 0.5), width=100, height=100, bd=1,
                               relief="solid")
        bloque_div2.pack()
        self.notebook = ttk.Notebook(bloque_div2)
        self.notebook.pack(expand=1, fill="both")

        # Pestaña principal
        pestaña_principal = ttk.Frame(self.notebook)
        self.notebook.add(pestaña_principal)

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
        menu.add_command(label=opciones[1], command=self.ventana.destroy)
        menu.add_command(label=opciones[2])

        # Asociar el menú a la ventana principal
        self.ventana.config(menu=menu)

        # Botón Proceso y Consulta sin menú desplegable
        btn_proceso_consulta = tk.Button(bloque_div, text="Proceso y Consulta", command=self.procesar)
        btn_proceso_consulta.pack(side="left", padx=0, fill="y")

        # Botón Ayuda sin menú desplegable
        btn_ayuda = tk.Button(bloque_div, text="Ayuda", command=lambda: self.opcion_seleccionada("Ayuda"))
        btn_ayuda.pack(side="left", padx=0, fill="y")

        # Iniciar el bucle de eventos de Tkinter
        self.ventana.mainloop()

    def opcion_seleccionada(self, opcion):

        print(str(opcion))

    def procesar(self):
        self.mostrar_ventana_detalle("Proceso")

    def mostrar_ventana_detalle(self, tipo):
        # Obtener la pestaña principal
        pestaña_principal = self.notebook.nametowidget(self.notebook.select())

        # Limpiar el contenido actual de la pestaña principal
        for widget in pestaña_principal.winfo_children():
            widget.destroy()

        # Contenido de la pestaña principal
        tk.Label(pestaña_principal, text=f"Nombre del {tipo}", padx=20, pady=10, bd=1, relief="solid").pack()

        tk.Label(pestaña_principal, text=f"Descripción del detalle del {tipo}", padx=100, pady=10, bd=1,
                 relief="solid").pack()

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

        btn_aceptar = tk.Button(div_frame, text="Aceptar",
                                command=lambda: messagebox.showinfo("Aceptar", "Datos aceptados"))
        btn_aceptar.grid(row=5, column=0, padx=5, pady=5)

        btn_cerrar = tk.Button(div_frame, text="Cerrar", command=lambda: self.limpiar_contenido())
        btn_cerrar.grid(row=5, column=1, padx=5, pady=5)

    def limpiar_contenido(self):
        # Limpiar el contenido actual de la pestaña principal
        for widget in self.pestaña_principal.winfo_children():
            widget.destroy()

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Buscar en la lista de clientes
    cliente_encontrado = None
    for cliente in clientes:
        if username == cliente.get_nombre() and password == cliente.get_num_documento():
            cliente_encontrado = cliente

            break

    # Verificar si se encontró un cliente
    if cliente_encontrado:
        mi_gui = GUI(cliente)

    else:
        messagebox.showerror("Login Error", "Invalid username or password")

class hj_vida:
    def cambio_hj_vida(self):
        if self.hj_vida["text"] == "Thomas Monnier Granda es un dedicado estudiante de ingeniería de sistemas, \n\nes conocido por su entusiasmo contagioso y su amor por los desafíos. \n\nApasionado por la inteligencia artificial, busca constantemente\n\n oportunidades para aplicarsus conocimientos en proyectos innovadores.\n\n Fuera de la informática, disfruta de la fotografía y \n\nsueña con combinar su pasión por la tecnología\n\n con el arte visual.":
            self.hj_vida.config(
                text="Juan David Robayo es un estudiante apasionado de ingeniería de sistemas, \n\nencuentra inspiración en la resolución de problemas complejos. \n\nSu habilidad para pensar de manera lógica y creativa\n\n  lo ha llevado a destacarse. Además de su dedicación académica,\n\n  el disfruta del ajedrez y ve cada desafío \n\ncomo una oportunidad para mejorar sus habilidades estratégicas,\n\n su mayor meta en su vida es pasar la materia de \n\nprogramación orientada a objetos,\n\n el sabe que el profe le hará el favor de pasarlo.",
                font=("Helvetica", 7, 'bold italic'))
            self.imagen1.config(image=self.nueva_imagen_1)
            self.imagen2.config(image=self.nueva_imagen_2)
            self.imagen3.config(image=self.nueva_imagen_3)
            self.imagen4.config(image=self.nueva_imagen_4)
        elif self.hj_vida["text"] == "Juan David Robayo es un estudiante apasionado de ingeniería de sistemas, \n\nencuentra inspiración en la resolución de problemas complejos. \n\nSu habilidad para pensar de manera lógica y creativa\n\n  lo ha llevado a destacarse. Además de su dedicación académica,\n\n  el disfruta del ajedrez y ve cada desafío \n\ncomo una oportunidad para mejorar sus habilidades estratégicas,\n\n su mayor meta en su vida es pasar la materia de \n\nprogramación orientada a objetos,\n\n el sabe que el profe le hará el favor de pasarlo.":
            self.hj_vida.config(
                text="Marcos Nuñes Isaza es un estudiante de ingeniería de sistemas, \n\nse destaca por su enfoque meticuloso en cada tarea.\n\n Su interés por la ciberseguridad lo motiva a explorar constantemente\n\n nuevas formas de proteger la información.\n\n En su tiempo libre, él es un ávido lector\n\n y se embarca en la creación de pequeños proyectos de\n\n desarrollo de software para ampliar su experiencia práctica.\n\nTiene como objetivo superar la materia de Programación Orientada a Objetos\n\n y confía en su profesor.",
                font=("Helvetica", 7, 'bold italic'))
            self.imagen1.config(image=self.nueva_imagen_3)
            self.imagen2.config(image=self.nueva_imagen_1)
            self.imagen3.config(image=self.nueva_imagen_2)
            self.imagen4.config(image=self.nueva_imagen_4)
        else:
            self.hj_vida.config(
                text="Thomas Monnier Granda es un dedicado estudiante de ingeniería de sistemas, \n\nes conocido por su entusiasmo contagioso y su amor por los desafíos. \n\nApasionado por la inteligencia artificial, busca constantemente\n\n oportunidades para aplicarsus conocimientos en proyectos innovadores.\n\n Fuera de la informática, disfruta de la fotografía y \n\nsueña con combinar su pasión por la tecnología\n\n con el arte visual.")
            self.imagen1.config(image=self.nueva_imagen_4)
            self.imagen2.config(image=self.nueva_imagen_3)
            self.imagen3.config(image=self.imagen_principal)
            self.imagen4.config(image=self.nueva_imagen_1)

    def ir_a_ventana_principal(self):
        # Crear la siguiente ventana (Ventana Principal de cualquier usuario)
        log_in = tk.Toplevel()
        log_in.title("Inicio")
        log_in.geometry("180x150")
        lbl = tk.Label(log_in, text="Seleccione su tipo de cliente:")
        option1 = tk.Button(log_in, text="Cliente nuevo")
        option2 = tk.Button(log_in, text="cliente antiguo", command=self.seleccionar)
        lbl.grid(row=0, column=1, padx=10, pady=10)
        option1.grid(row=1, column=1, padx=10, pady=10)
        option2.grid(row=2, column=1, padx=10, pady=10)

    def cambiar_imagen_principal(self, event):
        global indice_imagen_actual
        indice_imagen_actual = (indice_imagen_actual + 1) % len(self.lista_imagenes)
        self.fotoprin.config(image=self.lista_imagenes[indice_imagen_actual])

    def salir_aplicacion(self):
        respuesta = messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?")
        if respuesta:
            self.kick.destroy()

    def descripcion_sistema(self):
        # Puedes mostrar la descripción en algún widget de la ventana principal
        # por ejemplo, creando una etiqueta temporal o una nueva ventana
        descripcion = "¡Bienvenido al sistema del Hotel Sol Caribe! \nEste sistema te permite realizar reservas y más."
        tk.messagebox.showinfo("Descripción del Sistema", descripcion)

    def __init__(self):
        # Creacion de ventanas
        self.kick = tk.Toplevel()
        self.kick.title("Hotel Sol Caribe")
        self.kick.resizable(1, 1)
        self.kick.geometry('800x600')
        self.kick.configure(bg="#15ADD6")
        ruta_carpeta = os.path.dirname(os.path.abspath(__file__))
        img_nombre = Image.open("src/uiMain/Juan1 copy.png")
        img = img_nombre.resize((163, 150), Image.BILINEAR)
        self.imagen_principal = ImageTk.PhotoImage(img)

        img_nombre = Image.open("src/uiMain/Marco1.png")
        img = img_nombre.resize((163, 150), Image.BILINEAR)
        self.nueva_imagen_1 = ImageTk.PhotoImage(img)

        img_nombre = Image.open("src/uiMain/Marco3.png")
        img = img_nombre.resize((163, 150), Image.BILINEAR)
        self.nueva_imagen_2 = ImageTk.PhotoImage(img)

        img_nombre = Image.open("src/uiMain/Marco4.png")
        img = img_nombre.resize((163, 150), Image.BILINEAR)
        self.nueva_imagen_3 = ImageTk.PhotoImage(img)

        img_nombre = Image.open("src/uiMain/Juan1 copy.png")
        img = img_nombre.resize((163, 150), Image.BILINEAR)
        self.nueva_imagen_4 = ImageTk.PhotoImage(img)

        img_nombre = Image.open("src/uiMain/Tomas3.png")
        img = img_nombre.resize((163, 150), Image.BILINEAR)
        self.nueva_imagen_5 = ImageTk.PhotoImage(img)

        img_hotel = Image.open("src/uiMain/hotel1.png")
        img = img_hotel.resize((300, 300), Image.BILINEAR)
        hotel1 = ImageTk.PhotoImage(img)

        img_hotel = Image.open("src/uiMain/hotel2.png")
        img = img_hotel.resize((300, 300), Image.BILINEAR)
        hotel2 = ImageTk.PhotoImage(img)

        img_hotel = Image.open("src/uiMain/hotel3.png")
        img = img_hotel.resize((300, 300), Image.BILINEAR)
        hotel3 = ImageTk.PhotoImage(img)

        img_hotel = Image.open("src/uiMain/hotel4.png")
        img = img_hotel.resize((300, 300), Image.BILINEAR)
        hotel4 = ImageTk.PhotoImage(img)

        img_hotel = Image.open("src/uiMain/hotel5.png")
        img = img_hotel.resize((300, 300), Image.BILINEAR)
        hotel5 = ImageTk.PhotoImage(img)

        self.lista_imagenes = [hotel1, hotel2, hotel3, hotel4, hotel5]
        indice_imagen_actual = 0

        # creacion de frames y su distribucion
        all_frame = tk.Frame(self.kick, bg="#D3F1F9")
        all_frame.pack(fill="both", expand=True)

        top_frame = tk.Frame(all_frame, bg="#15ADD6", height=50)
        top_frame.pack(fill='x')
        barra_menu = Menu(self.kick)
        menu_inicio = Menu(barra_menu, tearoff=0)
        menu_inicio.add_command(label="Salir de la aplicación", command=self.salir_aplicacion)
        menu_inicio.add_command(label="Descripción del sistema", command=self.descripcion_sistema)
        barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
        self.kick.config(menu=barra_menu)

        p1_frame = tk.Frame(all_frame, bg="#92BAC5")
        p1_frame.place(x=20, y=30, width=370, height=560)

        p2_frame = tk.Frame(all_frame, bg="#92BAC5")
        p2_frame.place(x=405, y=30, width=370, height=560)

        p3_frame = tk.Frame(p1_frame, bg="black")
        p3_frame.place(x=5, y=5, width=360, height=220)
        welcome = tk.Label(p3_frame,
                           text="¡Bienvenido al portal de reservas del Hotel Sol Caribe!\n\nEstamos encantados de que consideres hospedarte con nosotros.\n\n Descubre, explora y disfruta de una estancia inolvidable. \n\nSi necesitas ayuda con la reserva, estamos aquí para asistirte.\n\n ¡Esperamos darte la bienvenida pronto!",
                           fg="white", bg="black", justify="center", font=("Helvetica", 8, 'bold italic'))
        welcome.pack(expand=True)

        p4_frame = tk.Frame(p1_frame, bg="black")
        p4_frame.place(x=5, y=235, width=360, height=320)
        boton_ingreso = tk.Button(p4_frame, text="Ingresar al Sistema", bg="#1A8CAC", command=self.ir_a_ventana_principal,
                                  font=("Helvetica", 10))
        boton_ingreso.pack(side="bottom", fill="x")
        self.fotoprin = tk.Label(p4_frame, bg="red", )
        self.fotoprin.pack(side="top", pady=10)
        self.fotoprin.bind("<Enter>", lambda event: self.cambiar_imagen_principal(event))

        p5_frame = tk.Frame(p2_frame, bg="black")
        p5_frame.place(x=5, y=5, width=360, height=220)
        self.hj_vida = tk.Button(p5_frame,
                            text="Thomas Monnier Granda es un dedicado estudiante de ingeniería de sistemas, \n\nes conocido por su entusiasmo contagioso y su amor por los desafíos. \n\nApasionado por la inteligencia artificial, busca constantemente\n\n oportunidades para aplicarsus conocimientos en proyectos innovadores.\n\n Fuera de la informática, disfruta de la fotografía y \n\nsueña con combinar su pasión por la tecnología\n\n con el arte visual.",
                            font=("Helvetica", 7, 'bold italic'), command=self.cambio_hj_vida)
        self.hj_vida.pack(fill="both", expand=True)

        p6_frame = tk.Frame(p2_frame, bg="black")
        p6_frame.place(x=5, y=235, width=360, height=320)
        self.imagen1 = tk.Label(p6_frame, bg="red", image=self.nueva_imagen_1)
        self.imagen1.grid(row=0, column=0, padx=5, pady=5)
        self.imagen2 = tk.Label(p6_frame, bg="red", image=self.nueva_imagen_2)
        self.imagen2.grid(row=0, column=1, padx=5, pady=5)
        self.imagen3 = tk.Label(p6_frame, bg="red", image=self.nueva_imagen_3)
        self.imagen3.grid(row=1, column=0, padx=5, pady=5)
        self.imagen4 = tk.Label(p6_frame, bg="red", image=self.nueva_imagen_4)
        self.imagen4.grid(row=1, column=1, padx=5, pady=5)

class GUI:
    def __init__(self,cliente):
        self.cliente = cliente
        self.ventana_2 = tk.Tk()
        self.ventana_2.title("Menú Principal")
        self.ventana_2.geometry("400x400")

        # Botón "Reservar Hotel"
        btn_reservar_hotel = tk.Button(self.ventana_2, text="Reservar Servicios", command=self.reservar_hotel)
        btn_reservar_hotel.pack(pady=20)

        # Botón "Principal"
        btn_principal = tk.Button(self.ventana_2, text="Principal", command=Principal)
        btn_principal.pack(pady=20)

        # Botón "Manual"
        btn_manual = tk.Button(self.ventana_2, text="Manual", command=self.abrir_manual)
        btn_manual.pack(pady=20)

        btn_cliente = tk.Button(self.ventana_2, text="Cliente", command=self.abrir_cliente)
        btn_cliente.pack(pady=20)
        # Iniciar el bucle de eventos de Tkinter
        self.ventana_2.mainloop()
    def abrir_cliente(self):
        root_3 = tk.Tk()
        app = InterfazClienteInfo(root_3)
        root_3.mainloop()
    def reservar_hotel(self):
        root_2 = tk.Tk()
        app_2 = SolicitudServicioApp(root_2)
        root_2.mainloop()
    def abrir_principal(self):
        # Puedes poner aquí la lógica para la función "Principal"
        principal = Principal()

    def abrir_manual(self):
        app = hj_vida()


        # Puedes poner aquí la lógica para la función "Manual"


precios_servicios = {
    'RESTAURANTE': 500,
    'SPA': 1000,
    'PISCINA': 1000,
    'HABITACION': 2000
}

class Pago:
    pass
class PagoServicioApp:
    def __init__(self, root, monto_a_pagar):
        self.root = root
        self.root.title("Pago de Servicio")
        self.root.geometry("300x150")

        tk.Label(root, text="Monto a pagar: ${:.2f}".format(monto_a_pagar), font=("Helvetica", 12)).pack(pady=20)

        tk.Button(root, text="Pagar", command=self.procesar_pago, bg="green", fg="white").pack(pady=10)

    def procesar_pago(self):
        messagebox.showinfo("Pago Exitoso", "¡Pago realizado con éxito!")
        self.root.destroy()

class SolicitudServicioApp:
    servicios_disponibles = [("RESTAURANTE", 500), ("SPA", 1000), ("PISCINA", 1000), ("HABITACION", 2000)]

    def __init__(self, root):
        self.root = root
        self.root.title("Solicitud de Servicio")
        self.root.geometry("500x500")

        self.nombre_var = tk.StringVar()
        self.monto_a_pagar = tk.DoubleVar()

        servicios_disponibles = [(servicio.name, servicio.value[1]) for servicio in ServiciosHotel]

        tk.Label(root, text="Nombre del Cliente:", font=("Helvetica", 12)).pack(pady=10)
        tk.Entry(root, textvariable=self.nombre_var).pack(pady=10)

        tk.Label(root, text="Servicios disponibles:", font=("Helvetica", 12)).pack(pady=10)

        self.servicios_var = []
        for servicio in servicios_disponibles:
            var = tk.IntVar()
            checkbutton = tk.Checkbutton(root, text=f"{servicio[0]} - ${servicio[1]}", variable=var, command=self.calcular_monto)
            checkbutton.pack(anchor="w", padx=10, pady=2)
            self.servicios_var.append((servicio[0], servicio[1], var))

        tk.Label(root, text="Monto a pagar: $0.00", font=("Helvetica", 12)).pack(pady=10)

        tk.Button(root, text="Enviar Solicitud", command=self.enviar_solicitud, bg="blue", fg="white").pack(pady=20)

    def calcular_monto(self):
        self.root.update_idletasks()

    def enviar_solicitud(self):
        nombre_cliente = self.nombre_var.get()

        monto_total = 0  # Verificar si se proporcionó el nombre del cliente
        if nombre_cliente:
            # Filtrar los servicios seleccionados
            servicios_seleccionados = [(servicio[0], servicio[1]) for servicio in self.servicios_var if
                                       servicio[2].get() == 1]
            for i in range(0, len(servicios_seleccionados)):
                monto_total = int(precios_servicios[servicios_seleccionados[i][0]]) + monto_total

            if servicios_seleccionados:
                # Crear una nueva ventana para el pago
                ventana_pago = tk.Toplevel(self.root)
                pago_app = PagoServicioApp(ventana_pago, monto_total)
            else:
                messagebox.showerror("Error", "Por favor, seleccione al menos un servicio.")
        else:
            messagebox.showerror("Error", "Por favor, ingrese el nombre del cliente.")

def signup():
    show_signup_window()


# Create the main window

# Start the Tkinter event loop
if __name__ == "__main__":
    clientes = []
    cliente1 = Cliente(nombre="Juan Pérez", tipo_cedula="Cédula de Ciudadanía", numero_cedula="123456789",
                       sexo="Masculino", edad=30, telefono="555-1234", correo="juan@example.com",
                       direccion="Calle 123", idCliente=1)

    cliente2 = Cliente(nombre="Ana Gómez", tipo_cedula="Cédula de Extranjería", numero_cedula="987654321",
                       sexo="Femenino", edad=25, telefono="555-5678", correo="ana@example.com",
                       direccion="Avenida XYZ", idCliente=2)

    clientes.append(cliente1)
    clientes.append(cliente2)
    root = tk.Tk()
    root.geometry("400x300")
    root.title("Login and Sign Up Example")

    # Create and add widgets to the window
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True)

    label_username = tk.Label(frame, text="Username:")
    label_username.grid(row=0, column=0, sticky="e", pady=5)

    entry_username = tk.Entry(frame)
    entry_username.grid(row=0, column=1, pady=5)

    label_password = tk.Label(frame, text="Password:")
    label_password.grid(row=1, column=0, sticky="e", pady=5)

    entry_password = tk.Entry(frame, show="*")  # Entry widget with password masking
    entry_password.grid(row=1, column=1, pady=5)

    button_login = tk.Button(frame, text="Login", command=login)
    button_login.grid(row=2, column=1, pady=10, sticky="w")

    button_signup = tk.Button(frame, text="Sign Up", command=signup)
    button_signup.grid(row=2, column=1, pady=10, sticky="e")
    root.mainloop()
