#|==================================================================================================================================|
#|                                                                                                                                  |
#|  Copyright (c) 2025 Agencia de Viajes Mundo Aventura S.A.                                                                        |
#|                                                                                                                                  |
#|                                                                                                                                  |
#|  + Nombre del módulo:                                                                                                            |
#|                                                                                                                                  |
#|      Principal.py                                                                                                                |
#|                                                                                                                                  |
#|  + Resumen:                                                                                                                      |
#|                                                                                                                                  |
#|      En este módulo está programada la pestaña principal del programa,                                                           |
#|               desde la cual se pueden acceder a las 5 (cinco) funcionalidades.                                                   |
#|                                                                                                                                  |
#|  + Codificado por:                                                                                                               |
#|                                                                                                                                  |
#|      - Alejandro Pérez Barrera (2025-02-08) (Creador)                                                                            |
#|                                                                                                                                  |
#|  +Última revisión: 2025-02-15-17-46, AlPerBara                                                                                   |
#|                                                                                                                                  |
#|  + Novedades:                                                                                                                    |
#|                                                                                                                                  |
#|      Este espacio está disponible para reportar novedades que se encuentren en este módulo...                                    |
#|                                                                                                                                  |
#|  + Pendientes en este módulo:                                                                                                    |
#|      - Consultar si la ventana puede ser NO resizable.                                                                           |
#|      - Asignar comando para reservar hotel.                                                                                      |
#|      - Asignar comando para reservar talleres.                                                                                   |
#|      - Asignar comando para reservar transporte.                                                                                 |
#|      - Asignar comando para realizar pago.                                                                                       |
#|      - Asignar comando para reservar eventos.                                                                                    |
#|      - Cambiar o eliminar el color del frame principal.                                                                          |
#|      - Añadir información sobre la aplicación.                                                                                   |
#|      - Añadir información sobre los desarrolladores.                                                                             |
#|                                                                                                                                  |
#|==================================================================================================================================|

import tkinter as tk #tkinter para crear la interfaz de usuario
from tkinter import messagebox  #Esto es para mostrar los cuadritos de información

import Home #Esto es para regresar a la ventana de inicio
import uiReservaHotel #Esto es para poder crear los campos de texto
import uiTransporte

#Este método es solo para poder empezar la ejecución de esta clase desde aquí sin recibir el error TypeError: 'module' object is not callable
def aterrizar():
    root = tk.Tk()
    Principal(root)
    root.mainloop()


class Principal: #Principal es la ventana de inicio, desde la cual se accede a las funcionalidades 
    def __init__(self, root):
        self.root=root #definir  raiz
        self.root.iconphoto(False, tk.PhotoImage(file=f"src/uiMain/media/iconos/icono_principal.png"))
        self.root.title("Rumbo Aventura") #Le coloco su título
        self.root.geometry("800x600") #El tamaño de la ventana es de 800 x 600
        #self.root.resizable(0,0) #Así no se puede cambiar el tamaño de la pestaña 😈😈😈🗣️🔥🔥 TODO: Consultar si está permitido que la ventana no sea resizable


        #========== MENÚ DE LA PARTE SUPERIOR ==========
        #El menú de la parte de arriba:
        self.barra_menu= tk.Menu(self.root)#Crear una barra de menú
        self.root.config(menu=self.barra_menu)#Le asigno esa barra a la pestaña root

        #----- Pestaña de archivo -----
        self.menu_archivo = tk.Menu(self.barra_menu, tearoff=0)#Ahora creo el botoncito de inicio como tal
        #El tearoff hace que el menu no se pueda desprender de la pestaña principal,
        #se nota que el menu se puede desprender porque encima del menu salen unas rayitas punteadas, pero con tearoff=0 no salen 😀.
        self.menu_archivo.add_command(label="Aplicación", command=self.pop_up_aplicacion)#Opción para tener info. de la app
        self.menu_archivo.add_separator()#Y aquí un separador
        self.menu_archivo.add_command(label="Salir", command=self.return_inicio)#Opcion para regresar al menu de inicio.
        self.barra_menu.add_cascade(label="Archivo", menu=self.menu_archivo)#Colocar el menú de archivo en la barra de menús

        #----- Pestaña Procesos y Consultas -----
        self.menu_procesos = tk.Menu(self.barra_menu, tearoff=0)#Ahora creo el botoncito de inicio como tal
        #El tearoff hace que el menu no se pueda desprender de la pestaña principal,
        #se nota que el menu se puede desprender porque encima del menu salen unas rayitas punteadas, pero con tearoff=0 no salen 😀.
        self.menu_procesos.add_command(label="Reservar habitación de hotel", command=self.reservar_hotel)#Opción reservar hotel TODO:Asignar comando correspondiente
        self.menu_procesos.add_separator()#Y aquí un separador

        self.menu_procesos.add_command(label="Reservar Ruta de actividades y talleres")#Opcion para reservar talleres TODO: Asignar comando correspondiente
        self.menu_procesos.add_separator()#Y aquí un separador

        self.menu_procesos.add_command(label="Reservar medio de transporte", command=self.reservar_transporte)#Opción reservar trasporte TODO:Asignar comando correspondiente
        self.menu_procesos.add_separator()#Y aquí un separador

        self.menu_procesos.add_command(label="Realizar pagos")#Opción pagar TODO:Asignar comando correspondiente
        self.menu_procesos.add_separator()#Y aquí un separador

        self.menu_procesos.add_command(label="Reservar Eventos")#Opción reservar trasporte TODO:Asignar comando correspondiente

        self.barra_menu.add_cascade(label="Procesos y Consultas", menu=self.menu_procesos)#Colocar el menú de procesos en la barra de menús

        #----- Pestaña de ayuda -----
        self.menu_ayuda = tk.Menu(self.barra_menu, tearoff=0)#Ahora creo el botoncito de inicio como tal
        #El tearoff hace que el menu no se pueda desprender de la pestaña principal,
        #se nota que el menu se puede desprender porque encima del menu salen unas rayitas punteadas, pero con tearoff=0 no salen 😀.
        self.menu_ayuda.add_command(label="Acerca de", command=self.pop_up_ayuda)#Opción de información.
        self.barra_menu.add_cascade(label="Ayuda", menu=self.menu_ayuda)#Colocar el menú de ayudas en la barra de menús


        #========== FRAMES PARA COLOCAR LAS FUNCIONALIDADES ==========
        #Frame principal contiene la pestaña principal
        self.frame_principal = tk.Frame(self.root, bg="cyan") #TODO: Quitar o cambiar el color de fondo
        self.frame_principal.pack(expand=True,fill="both", padx=10, pady=10)
        
        #En el frame superior se aloja el nombre de la funcionalidad actual
        self.frame_superior = tk.Frame(self.frame_principal, bg="blue") #TODO: Quitar o cambiar el color de fondo
        self.frame_superior.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        self.label_superior = tk.Label(self.frame_superior, text="Sistema de reservaciones y pagos", font=("Arial", 20, "bold"))
        self.label_superior.place(relx=0.5, rely=0.5, anchor="center")
        
        #En el frame intermedio se aloja una descripción del contexto actual
        self.frame_intermedio = tk.Frame(self.frame_principal, bg="green") #TODO: Quitar o cambiar el color de fondo
        self.frame_intermedio.place(relx=0, rely=0.15, relwidth=1, relheight=0.15,)
        
        #EL FRAME INFERIOR ES EL CONTENEDOR DE LAS FUNCIONALIDADES
        self.frame_inferior = tk.Frame(self.frame_principal, bg="yellow") #TODO: Quitar o cambiar el color de fondo
        self.frame_inferior.place(relx=0, rely=0.30, relwidth=1, relheight=0.7)
    
    #pop_up_aplicacion muestra una ventana con la informacion de la aplicacion
    def pop_up_aplicacion(self):
        messagebox.showinfo("Sobre La Aplicación", "Informacionn            e    \n           g") #TODO: Añadir información sobre la aplicación

    #return_inicio regresa a la pestaña de inicio
    def return_inicio(self):
        self.root.destroy() #se cierra esta ventana
        Home.aterrizar() #El metodo aterrizar de home crea la ventana de inicio y todo lo demás, referente a aquella funcionalidad

    def pop_up_ayuda(self):
        messagebox.showinfo("Acerca de", "Desarrolladores... n                       j   \n         8                    7") #TODO: Añadir información sobre los desarrolladores
        
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
        
    #========== FUNCINALIDADES ==========
    
    #========== RESERVAR HOTEL ==========
    
    def reservar_hotel(self):
        reservar = uiReservaHotel.uiReservaHotel(self)
        reservar.reservar_hotel()
        
    def reservar_transporte(self):
        reservacion = uiTransporte.uiTransporte(self)
        reservacion.reservar_transporte()
        