from gestorAplicacion.servicios.Habitacion import Habitacion
from gestorAplicacion.servicios.Hotel import Hotel
from gestorAplicacion.servicios.Servicio import Servicio
from gestorAplicacion.servicios.GestionReserva import GestionReserva
from gestorAplicacion.entidades.Persona import Persona
from gestorAplicacion.entidades.Empleado import Empleado
from gestorAplicacion.entidades.Cliente import Cliente
from capaPersistencia.serializador import Serializador
from capaPersistencia.deserializador import Deserializador
from format import FieldFrame
from ffOut import ffOut
from ventana_principal import mainWin
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Tk, Entry, Button, PhotoImage, Menu, messagebox
import os

if __name__==  "__main__":

    '''deserializado= Deserializador.deserializar()

    hoteles=deserializado["hoteles"]
    #empleados=deserializado["empleados"]
    #clientes=deserializado["clientes"]

    serv1= Servicio("Desayuno", 2.99, "6:00", "10:00")
    serv2= Servicio("Actividad tematica", 6.99, "10:00", "15:30")
    serv3= Servicio("Sesion de masaje", 10.50)

    hotel1= Hotel("Sol caribe", "<direccion>")
    hotel1.setComentarios("muy bueno", "excelente")
    hotel1.setServicios(Servicio.getServicios())
    hotel1.setCalificacion(4.0)

    for i in range(6):
        hab= Habitacion(hotel1,(100+i),4,100, "estandar", False)
        hotel1.addHabitaciones(hab)

    hoteles=Hotel.getHoteles()
    empleados= Empleado.getEmpleados()
    clientes= Cliente.getClientes()
    Serializador.serializar(hoteles=hoteles, empleados=empleados,clientes=clientes)'''

    
    #interfaz grafica de usuario aqui:
    #Definicion de cambio de texto e imagenes dentro de los frames p5 y p6
def cambio_hj_vida():
    if hj_vida[
        "text"] == "Thomas Monnier Granda es un dedicado estudiante de ingeniería de sistemas, \n\nes conocido por su entusiasmo contagioso y su amor por los desafíos. \n\nApasionado por la inteligencia artificial, busca constantemente\n\n oportunidades para aplicarsus conocimientos en proyectos innovadores.\n\n Fuera de la informática, disfruta de la fotografía y \n\nsueña con combinar su pasión por la tecnología\n\n con el arte visual.":
        hj_vida.config(
            text="Juan David Robayo es un estudiante apasionado de ingeniería de sistemas, \n\nencuentra inspiración en la resolución de problemas complejos. \n\nSu habilidad para pensar de manera lógica y creativa\n\n  lo ha llevado a destacarse. Además de su dedicación académica,\n\n  el disfruta del ajedrez y ve cada desafío \n\ncomo una oportunidad para mejorar sus habilidades estratégicas,\n\n su mayor meta en su vida es pasar la materia de \n\nprogramación orientada a objetos,\n\n el sabe que el profe le hará el favor de pasarlo.",
            font=("Helvetica", 7, 'bold italic'))
        imagen1.config(image =  nueva_imagen_1)
        imagen2.config(image =nueva_imagen_2)
        imagen3.config(image = nueva_imagen_3)
        imagen4.config(image= nueva_imagen_4)
    elif hj_vida[
        "text"] == "Juan David Robayo es un estudiante apasionado de ingeniería de sistemas, \n\nencuentra inspiración en la resolución de problemas complejos. \n\nSu habilidad para pensar de manera lógica y creativa\n\n  lo ha llevado a destacarse. Además de su dedicación académica,\n\n  el disfruta del ajedrez y ve cada desafío \n\ncomo una oportunidad para mejorar sus habilidades estratégicas,\n\n su mayor meta en su vida es pasar la materia de \n\nprogramación orientada a objetos,\n\n el sabe que el profe le hará el favor de pasarlo.":
        hj_vida.config(
            text="Marcos Nuñes Isaza es un estudiante de ingeniería de sistemas, \n\nse destaca por su enfoque meticuloso en cada tarea.\n\n Su interés por la ciberseguridad lo motiva a explorar constantemente\n\n nuevas formas de proteger la información.\n\n En su tiempo libre, él es un ávido lector\n\n y se embarca en la creación de pequeños proyectos de\n\n desarrollo de software para ampliar su experiencia práctica.\n\nTiene como objetivo superar la materia de Programación Orientada a Objetos\n\n y confía en su profesor.",
            font=("Helvetica", 7, 'bold italic'))
        imagen1.config(image=nueva_imagen_3)
        imagen2.config(image=nueva_imagen_1)
        imagen3.config(image=nueva_imagen_2)
        imagen4.config(image=nueva_imagen_4)
    else:
        hj_vida.config(
            text="Thomas Monnier Granda es un dedicado estudiante de ingeniería de sistemas, \n\nes conocido por su entusiasmo contagioso y su amor por los desafíos. \n\nApasionado por la inteligencia artificial, busca constantemente\n\n oportunidades para aplicarsus conocimientos en proyectos innovadores.\n\n Fuera de la informática, disfruta de la fotografía y \n\nsueña con combinar su pasión por la tecnología\n\n con el arte visual.")
        imagen1.config(image=nueva_imagen_4)
        imagen2.config(image=nueva_imagen_3)
        imagen3.config(image=imagen_principal)
        imagen4.config(image=nueva_imagen_1)


def ir_a_ventana_principal():
    # Crear la siguiente ventana (Ventana Principal de cualquier usuario)
    log_in = tk.Toplevel()
    log_in.title("Inicio")
    log_in.geometry("180x150")
    lbl= tk.Label(log_in, text="Seleccione su tipo de cliente:")
    option1= tk.Button(log_in, text="Cliente nuevo", command=show_signup_window)
    option2= tk.Button(log_in, text="cliente antiguo", command =seleccionar)
    lbl.grid(row=0, column=1, padx=10, pady=10)
    option1.grid(row=1, column=1, padx=10, pady=10)
    option2.grid(row=2, column=1, padx=10, pady=10)

def cambiar_imagen_principal(event):
    global indice_imagen_actual
    indice_imagen_actual = (indice_imagen_actual + 1) % len(lista_imagenes)
    fotoprin.config(image=lista_imagenes[indice_imagen_actual])

'''def registrar(event):
    ventana= Tk()
    ventana.title("registrar usuario")
    ventana.geometry("300x300")
    criterios=["nombre", "tipo_cedula", "numero_cedula", "telefono"]
    ff= FieldFrame(master=ventana, criterios=criterios)
    ff.pack()
    otra_clase = ffOut(ff)
    boton_obtener_y_guardar = tk.Button(ventana, text="Guardar Valores", command= otra_clase.guardar_valores)
    boton_obtener_y_guardar.pack(pady=10)
    continuar= tk.Button(ventana, text="continuar", command= show_signup_window)
    continuar.pack()
    ventana.mainloop()'''

def register():
    # Perform user registration (you can add your logic here)
    messagebox.showinfo("Registration", "Registration successful!")

def show_signup_window():
    # Create a Toplevel window for sign-up
    signup_window = tk.Toplevel()
    signup_window.title("User Registration")

    # Create and add widgets for registration
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

    button_register = tk.Button(frame, text="Register", command=register)
    button_register.grid(row=4, column=1, pady=10, sticky="e")

    button_enter= tk.Button(frame, text="Ingresar", command= mainWin.iniciar)
    button_enter.pack()


def seleccionar():
    pass

def salir_aplicacion():
    respuesta = messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?")
    if respuesta:
        kick.destroy()

def descripcion_sistema():
    # Puedes mostrar la descripción en algún widget de la ventana principal
    # por ejemplo, creando una etiqueta temporal o una nueva ventana
    descripcion = "¡Bienvenido al sistema del Hotel Sol Caribe! \nEste sistema te permite realizar reservas y más."
    tk.messagebox.showinfo("Descripción del Sistema", descripcion)



#Cracion de ventanas
kick = tk.Toplevel()
kick.title("Hotel Sol Caribe")
kick.resizable(1, 1)
kick.geometry('800x600')
kick.configure(bg="#15ADD6")
ruta_carpeta = os.path.dirname(os.path.abspath(__file__))
img_nombre = Image.open("src/uiMain/Juan1 copy.png")
img = img_nombre.resize((163, 150), Image.BILINEAR)
imagen_principal = ImageTk.PhotoImage(img)

img_nombre = Image.open("src/uiMain/Marco1.png")
img = img_nombre.resize((163, 150), Image.BILINEAR)
nueva_imagen_1 = ImageTk.PhotoImage(img)

img_nombre = Image.open("src/uiMain/Marco3.png")
img = img_nombre.resize((163,150), Image.BILINEAR)
nueva_imagen_2 = ImageTk.PhotoImage(img)

img_nombre = Image.open("src/uiMain/Marco4.png")
img = img_nombre.resize((163, 150), Image.BILINEAR)
nueva_imagen_3 = ImageTk.PhotoImage(img)

img_nombre = Image.open("src/uiMain/Juan1 copy.png")
img = img_nombre.resize((163, 150), Image.BILINEAR)
nueva_imagen_4 = ImageTk.PhotoImage(img)

img_nombre = Image.open("src/uiMain/Tomas3.png")
img = img_nombre.resize((163, 150), Image.BILINEAR)
nueva_imagen_5 = ImageTk.PhotoImage(img)


lista_imagenes = [imagen_principal, nueva_imagen_1, nueva_imagen_2, nueva_imagen_3, nueva_imagen_4, nueva_imagen_5]
indice_imagen_actual = 0

# creacion de frames y su distribucion
all_frame = tk.Frame(kick, bg="#D3F1F9")
all_frame.pack(fill="both", expand=True)

top_frame = tk.Frame(all_frame, bg="#15ADD6", height=50)
top_frame.pack(fill='x')
barra_menu = Menu(kick)
menu_inicio = Menu(barra_menu, tearoff=0)
menu_inicio.add_command(label="Salir de la aplicación", command=salir_aplicacion)
menu_inicio.add_command(label="Descripción del sistema", command=descripcion_sistema)
barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
kick.config(menu=barra_menu)

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
boton_ingreso = tk.Button(p4_frame, text="Ingresar al Sistema", bg="#1A8CAC", command=ir_a_ventana_principal,font=("Helvetica", 10))
boton_ingreso.pack(side="bottom", fill="x")
fotoprin = tk.Label(p4_frame, bg="red", )
fotoprin.pack(side="top", pady=10)
fotoprin.bind("<Enter>", lambda event: cambiar_imagen_principal(event))

p5_frame = tk.Frame(p2_frame, bg="black")
p5_frame.place(x=5, y=5, width=360, height=220)
hj_vida = tk.Button(p5_frame,
                    text="Thomas Monnier Granda es un dedicado estudiante de ingeniería de sistemas, \n\nes conocido por su entusiasmo contagioso y su amor por los desafíos. \n\nApasionado por la inteligencia artificial, busca constantemente\n\n oportunidades para aplicarsus conocimientos en proyectos innovadores.\n\n Fuera de la informática, disfruta de la fotografía y \n\nsueña con combinar su pasión por la tecnología\n\n con el arte visual.",
                    font=("Helvetica", 7, 'bold italic'), command=cambio_hj_vida)
hj_vida.pack(fill="both", expand=True)

p6_frame = tk.Frame(p2_frame, bg="black")
p6_frame.place(x=5, y=235, width=360, height=320)
imagen1 = tk.Label(p6_frame, bg="red", image=nueva_imagen_1)
imagen1.grid(row=0, column=0, padx=5, pady=5)
imagen2 = tk.Label(p6_frame, bg="red", image=nueva_imagen_2)
imagen2.grid(row=0, column=1, padx=5, pady=5)
imagen3 = tk.Label(p6_frame, bg="red", image=nueva_imagen_3)
imagen3.grid(row=1, column=0, padx=5, pady=5)
imagen4 = tk.Label(p6_frame, bg="red", image=nueva_imagen_4)
imagen4.grid(row=1, column=1, padx=5, pady=5)

kick.mainloop()
