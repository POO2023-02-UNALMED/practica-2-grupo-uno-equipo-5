from gestorAplicacion.servicios.Habitacion import  Habitacion
from gestorAplicacion.servicios.Hotel import Hotel
from gestorAplicacion.servicios.Servicio import Servicio
from capaPersistencia.serializador import Serializador
from capaPersistencia.deserializador import Deserializador
import tkinter as tk
from tkinter import Tk, Entry, Button, PhotoImage
import os

if __name__=="__main__":
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

    #interfaz grafica de usuario aqui:
    #Definicion de cambio de texto e imagenes dentro de los frames p5 y p6
def cambio_hj_vida():
    if hj_vida["text"] == "Thomas Monnier Granda es un dedicado estudiante de ingeniería de sistemas, \n\nes conocido por su entusiasmo contagioso y su amor por los desafíos. \n\nApasionado por la inteligencia artificial, busca constantemente\n\n oportunidades para aplicarsus conocimientos en proyectos innovadores.\n\n Fuera de la informática, disfruta de la fotografía y \n\nsueña con combinar su pasión por la tecnología\n\n con el arte visual.":
        hj_vida.config(text="Juan David Robayo es un estudiante apasionado de ingeniería de sistemas, \n\nencuentra inspiración en la resolución de problemas complejos. \n\nSu habilidad para pensar de manera lógica y creativa\n\n  lo ha llevado a destacarse. Además de su dedicación académica,\n\n  el disfruta del ajedrez y ve cada desafío \n\ncomo una oportunidad para mejorar sus habilidades estratégicas,\n\n su mayor meta en su vida es pasar la materia de \n\nprogramación orientada a objetos,\n\n el sabe que el profe le hará el favor de pasarlo.", font=("Helvetica", 7, 'bold italic'))
        imagen1.config(image=PhotoImage(file="Juan1.png"))
        imagen2.config(image=PhotoImage(file="Juan2.png"))
        imagen3.config(image=PhotoImage(file="Juan3.png"))
        imagen4.config(image=PhotoImage(file="Juan4.png"))
    elif hj_vida["text"] == "Juan David Robayo es un estudiante apasionado de ingeniería de sistemas, \n\nencuentra inspiración en la resolución de problemas complejos. \n\nSu habilidad para pensar de manera lógica y creativa\n\n  lo ha llevado a destacarse. Además de su dedicación académica,\n\n  el disfruta del ajedrez y ve cada desafío \n\ncomo una oportunidad para mejorar sus habilidades estratégicas,\n\n su mayor meta en su vida es pasar la materia de \n\nprogramación orientada a objetos,\n\n el sabe que el profe le hará el favor de pasarlo.":
        hj_vida.config(text="Marcos Nuñes Isaza es un estudiante de ingeniería de sistemas, \n\nse destaca por su enfoque meticuloso en cada tarea.\n\n Su interés por la ciberseguridad lo motiva a explorar constantemente\n\n nuevas formas de proteger la información.\n\n En su tiempo libre, él es un ávido lector\n\n y se embarca en la creación de pequeños proyectos de\n\n desarrollo de software para ampliar su experiencia práctica.\n\nTiene como objetivo superar la materia de Programación Orientada a Objetos\n\n y confía en su profesor.", font=("Helvetica", 7, 'bold italic'))
        imagen1.config(image=PhotoImage(file="Marco1.png"))
        imagen2.config(image=PhotoImage(file="Marco2.png"))
        imagen3.config(image=PhotoImage(file="Marco3.png"))
        imagen4.config(image=PhotoImage(file="Marco4.png"))
    else:
        hj_vida.config(text="Thomas Monnier Granda es un dedicado estudiante de ingeniería de sistemas, \n\nes conocido por su entusiasmo contagioso y su amor por los desafíos. \n\nApasionado por la inteligencia artificial, busca constantemente\n\n oportunidades para aplicarsus conocimientos en proyectos innovadores.\n\n Fuera de la informática, disfruta de la fotografía y \n\nsueña con combinar su pasión por la tecnología\n\n con el arte visual.")
        imagen1.config(image=PhotoImage(file="Tomas1.png"))
        imagen2.config(image=PhotoImage(file="Tomas2.png"))
        imagen3.config(image=PhotoImage(file="Tomas3.png"))
        imagen4.config(image=PhotoImage(file="Tomas4.png"))

def ir_a_ventana_principal():
    # Crear la siguiente ventana (Ventana Principal de cualquier usuario)
    ventana_principal = tk.Toplevel()
    ventana_principal.title("Ventana Principal de Usuario")

def cambiar_imagen_principal(event):
    global indice_imagen_actual
    indice_imagen_actual = (indice_imagen_actual + 1) % len(lista_imagenes)
    fotoprin.config(image=lista_imagenes[indice_imagen_actual])


#Cracion de ventanas
kick = Tk()
kick.title("Hotel Sol Caribe")
kick.resizable(1, 1)
kick.geometry('800x600')

ruta_carpeta = os.path.dirname(os.path.abspath(__file__))
imagen_principal = PhotoImage(file=os.path.join(ruta_carpeta, "Marco1.png"))
nueva_imagen_1 = PhotoImage(file=os.path.join(ruta_carpeta, "Marco2.png"))
nueva_imagen_2 = PhotoImage(file=os.path.join(ruta_carpeta, "Marco3.png"))
nueva_imagen_3 = PhotoImage(file=os.path.join(ruta_carpeta, "Marco4.png"))
nueva_imagen_4 = PhotoImage(file=os.path.join(ruta_carpeta, "Marco5.png"))
nueva_imagen_5 = PhotoImage(file=os.path.join(ruta_carpeta, "Tomas3.png"))

lista_imagenes = [imagen_principal, nueva_imagen_1, nueva_imagen_2, nueva_imagen_3, nueva_imagen_4, nueva_imagen_5]
indice_imagen_actual = 0

#creacion de frames y su distribucion
all_frame = tk.Frame(kick, bg="#D3F1F9")
all_frame.pack(fill="both", expand=True)

top_frame= tk.Frame(all_frame, bg="#15ADD6", height=50)
top_frame.pack(fill='x')

p1_frame = tk.Frame(all_frame, bg="#92BAC5")
p1_frame.place(x=20, y=30, width=370, height=560)


p2_frame = tk.Frame(all_frame, bg="#92BAC5")
p2_frame.place(x=405, y=30, width=370, height=560)

p3_frame= tk.Frame(p1_frame, bg="black")
p3_frame.place(x=5, y=5, width=360, height=220)
welcome = tk.Label(p3_frame, text="¡Bienvenido al portal de reservas del Hotel Sol Caribe!\n\nEstamos encantados de que consideres hospedarte con nosotros.\n\n Descubre, explora y disfruta de una estancia inolvidable. \n\nSi necesitas ayuda con la reserva, estamos aquí para asistirte.\n\n ¡Esperamos darte la bienvenida pronto!",fg="white", bg="black", justify="center", font=("Helvetica", 8, 'bold italic'))
welcome.pack(expand=True)


p4_frame= tk.Frame(p1_frame, bg="black")
p4_frame.place(x=5, y=235, width=360, height=320)
fotoprin=tk.Label(p4_frame,bg="red", )
fotoprin.pack(side="top", pady=10)
fotoprin.bind("<Enter>", lambda event: cambiar_imagen_principal(event))

p5_frame= tk.Frame(p2_frame, bg="black")
p5_frame.place(x=5, y=5, width=360, height=220)
hj_vida = tk.Button(p5_frame, text="Thomas Monnier Granda es un dedicado estudiante de ingeniería de sistemas, \n\nes conocido por su entusiasmo contagioso y su amor por los desafíos. \n\nApasionado por la inteligencia artificial, busca constantemente\n\n oportunidades para aplicarsus conocimientos en proyectos innovadores.\n\n Fuera de la informática, disfruta de la fotografía y \n\nsueña con combinar su pasión por la tecnología\n\n con el arte visual.",font=("Helvetica", 7, 'bold italic'), command=cambio_hj_vida)
hj_vida.pack(fill="both", expand=True)

p6_frame= tk.Frame(p2_frame, bg="black")
p6_frame.place(x=5, y=235, width=360, height=320)
imagen1=tk.Label(p6_frame,bg="red", image=PhotoImage(file="Tomas1.png"))
imagen1.grid(row=0, column=0, padx=5, pady=5)
imagen2=tk.Label(p6_frame,bg="red", image=PhotoImage(file="Tomas2.png"))
imagen2.grid(row=0, column=1, padx=5, pady=5)
imagen3=tk.Label(p6_frame,bg="red", image=PhotoImage(file="Tomas3.png"))
imagen3.grid(row=1, column=0, padx=5, pady=5)
imagen4=tk.Label(p6_frame,bg="red", image=PhotoImage(file="Tomas4.png"))
imagen4.grid(row=1, column=1, padx=5, pady=5)


kick.mainloop()

    
