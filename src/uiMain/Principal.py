#|==================================================================================================================================|
#|                                                                                                                                  |
#|  Copyright (c) 2025 Agencia de Viajes Mundo Aventura S.A.                                                                        |
#|                                                                                                                                  |
#|  + Nombre del módulo:                                                                                                            |
#|      Principal.py                                                                                                                |
#|  + Resumen:                                                                                                                      |
#|      En este módulo está programada la pestaña principal del programa, desde la cual se pueden acceder a las funcionalidades.    |
#|  + Codificado por:                                                                                                               |
#|      - Alejandro Pérez Barrera (2025-02-08) (Creador)                                                                            |
#|  + Última revisión: 2025-02-15-17-46, AlPerBara                                                                                   |
#|  + Novedades:                                                                                                                    |
#|      - Se agregan o ajustan funcionalidades, incluyendo el proceso de pago.                                                     |
#|==================================================================================================================================|

import tkinter as tk  # tkinter para crear la interfaz de usuario
from tkinter import messagebox  # Para mostrar cuadros de información

import Home  # Módulo para regresar a la ventana de inicio
import uiReservaHotel  # Funcionalidad de reservar hotel
import uiTransporte  # Funcionalidad de transporte
import uiPago  # Funcionalidad de pago

# Este método es para iniciar la ejecución de esta clase sin recibir error TypeError: 'module' object is not callable
def aterrizar():
    root = tk.Tk()
    Principal(root)
    root.mainloop()


class Principal:  # Ventana principal de acceso a funcionalidades
    def __init__(self, root):
        self.root = root  # Definir la raíz
        self.root.iconphoto(False, tk.PhotoImage(file="src/uiMain/media/iconos/icono_principal.png"))
        self.root.title("Rumbo Aventura")  # Título de la ventana
        self.root.geometry("800x600")
        # self.root.resizable(0,0)  # Verificar si la ventana debe ser no resizable

        # ========== MENÚ DE LA PARTE SUPERIOR ==========
        self.barra_menu = tk.Menu(self.root)  # Crear la barra de menú
        self.root.config(menu=self.barra_menu)  # Asignarla a la ventana

        # ----- Pestaña de archivo -----
        self.menu_archivo = tk.Menu(self.barra_menu, tearoff=0)
        self.menu_archivo.add_command(label="Aplicación", command=self.pop_up_aplicacion)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=self.return_inicio)
        self.barra_menu.add_cascade(label="Archivo", menu=self.menu_archivo)

        # ----- Pestaña Procesos y Consultas -----
        self.menu_procesos = tk.Menu(self.barra_menu, tearoff=0)
        self.menu_procesos.add_command(label="Reservar habitación de hotel", command=self.reservar_hotel)
        self.menu_procesos.add_separator()
        self.menu_procesos.add_command(label="Reservar Ruta de actividades y talleres")
        self.menu_procesos.add_separator()
        self.menu_procesos.add_command(label="Reservar medio de transporte", command=self.reservar_transporte)
        self.menu_procesos.add_separator()
        # Se asigna el comando para realizar pagos utilizando uiPago.go
        self.menu_procesos.add_command(label="Realizar pagos", command=uiPago.go())
        self.menu_procesos.add_separator()
        self.menu_procesos.add_command(label="Reservar Eventos")
        self.barra_menu.add_cascade(label="Procesos y Consultas", menu=self.menu_procesos)

        # ----- Pestaña de ayuda -----
        self.menu_ayuda = tk.Menu(self.barra_menu, tearoff=0)
        self.menu_ayuda.add_command(label="Acerca de", command=self.pop_up_ayuda)
        self.barra_menu.add_cascade(label="Ayuda", menu=self.menu_ayuda)

        # ========== FRAMES PARA COLOCAR LAS FUNCIONALIDADES ==========
        # Frame principal (área de la aplicación)
        self.frame_principal = tk.Frame(self.root, bg="cyan")
        self.frame_principal.pack(expand=True, fill="both", padx=10, pady=10)

        # Frame superior: nombre de la funcionalidad actual
        self.frame_superior = tk.Frame(self.frame_principal, bg="blue")
        self.frame_superior.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        self.label_superior = tk.Label(self.frame_superior, text="Sistema de reservaciones y pagos", font=("Arial", 20, "bold"))
        self.label_superior.place(relx=0.5, rely=0.5, anchor="center")

        # Frame intermedio: descripción del contexto
        self.frame_intermedio = tk.Frame(self.frame_principal, bg="green")
        self.frame_intermedio.place(relx=0, rely=0.15, relwidth=1, relheight=0.15)

        # Frame inferior: contenedor de las funcionalidades
        self.frame_inferior = tk.Frame(self.frame_principal, bg="yellow")
        self.frame_inferior.place(relx=0, rely=0.30, relwidth=1, relheight=0.7)

    # Muestra información sobre la aplicación
    def pop_up_aplicacion(self):
        messagebox.showinfo("Sobre La Aplicación", "Información de la aplicación...")  # Agregar detalles necesarios

    # Regresa a la ventana de inicio
    def return_inicio(self):
        self.root.destroy()
        Home.aterrizar()

    # Muestra información de ayuda/acerca de
    def pop_up_ayuda(self):
        messagebox.showinfo("Acerca de", "Información sobre desarrolladores y versión de la aplicación.")

    def despejar_frame_inferior(self):
        for widget in self.frame_inferior.winfo_children():
            widget.destroy()

    def despejar_frame_intermedio(self):
        for widget in self.frame_intermedio.winfo_children():
            widget.destroy()

    def despejar_frame_superior(self):
        for widget in self.frame_superior.winfo_children():
            widget.destroy()

    def despejar_todos_los_frames(self):
        self.despejar_frame_inferior()
        self.despejar_frame_intermedio()
        self.despejar_frame_superior()

    # ========== FUNCIONALIDADES ==========
    def reservar_hotel(self):
        reservar = uiReservaHotel.uiReservaHotel(self)
        reservar.reservar_hotel()

    def reservar_transporte(self):
        reservacion = uiTransporte.uiTransporte(self)
        reservacion.reservar_transporte()
