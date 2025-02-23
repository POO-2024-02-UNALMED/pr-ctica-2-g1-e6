#|==================================================================================================================================|
#|                                                                                                                                  |
#|  Copyright (c) 2025 Agencia de Viajes Mundo Aventura S.A.                                                                        |
#|                                                                                                                                  |
#|  + Nombre del módulo:                                                                                                            |
#|                                                                                                                                  |
#|      uiReservaHotel.py                                                                                                           |
#|                                                                                                                                  |
#|  + Resumen:                                                                                                                      |
#|                                                                                                                                  |
#|      Este módulo contiene la interfaz de usuario para la reserva de habitaciones de hotel.                                       |
#|              Se encarga de solicitar al usuario el destino de su viaje, las fechas de llegada y salida,                          |
#|              y el número de personas con las que viaja.                                                                          |
#|                                                                                                                                  |
#|  + Codificado por:                                                                                                               |
#|                                                                                                                                  |
#|      - Alejandro Pérez Barrera (2025-02-13) (Creador)                                                                            |
#|                                                                                                                                  |
#|  +Última revisión: 2025-02-23-12-00, AlPerBara                                                                                   |
#|                                                                                                                                  |
#|  + Novedades:                                                                                                                    |
#|                                                                                                                                  |
#|      -Se han implementado casos de excepción.                                                                                    |
#|                                                                                                                                  |
#|  + Pendientes en este módulo:                                                                                                    |
#|                                                                                                                                  |                                    
#|      - Verificar errores.                                                                                                        |                                    
#|      - Añadir comentarios.                                                                                                       |                        
#|                                                                                                                                  |                                                                          
#|==================================================================================================================================|


import tkinter as tk
from tkinter import messagebox    
import Fieldframe

import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.gestorAplicacion.reservacionHotel.Destino import Destino
from src.gestorAplicacion.reservacionHotel.Reserva import Reserva
import locale #Locale es para mostrar el nombre de los meses en español

from src.excepciones.FechaInvalida import FechaInvalida

from src.excepciones.ViajerosInvalidos import ViajerosInvalidos

from src.excepciones.DestinoInexistente import DestinoInexistente


class uiReservaHotel:
    def __init__(self, master):
        self.master = master
        self.field_frame = None
        self.reserva_usuario = None

    def reservar_hotel(self):
        #Primero es despejar los frames
        self.master.despejar_todos_los_frames()
        #Definiendo título y descripción, junto con un botón para comenzar
        tk.Label(self.master.frame_superior, text="Reservación de habitaciones de hotel", font=("Arial", 20, "bold")).place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(self.master.frame_intermedio, font=("Arial",12), wraplength=700, text="Puede reservar una habitación de hotel en uno de los múltiples destinos que ofrecemos, asegúrese de incluir información acerca del número de personas con las que viaja, y la fecha de llegada y de salida de su viaje.").place(relx=0.5, rely=0.5, anchor="center")
        tk.Button(self.master.frame_inferior, text="Comenzar", command=self.solicitar_destino, height=3,width=15, font=("Arial", 12)).place(relx=0.5, rely=0.5, anchor="center")
        
        
    def solicitar_destino(self):
        #Despejar frames inferior e intermedio
        self.master.despejar_frame_inferior()
        self.master.despejar_frame_intermedio()
        
        #Instrucciones para el usuario
        tk.Label(self.master.frame_intermedio, wraplength=700, text="Por favor ingrese el destino de su viaje, o deje el recuadro en blanco para ver todos nuestros destinos.", font=("Arial", 12)).place(relx=0.5, rely=0.5, anchor="center")
        
        #Estoy creando 3 columnas en el frame inferior, todas con el mismo peso (Mismo tamaño)
        self.master.frame_inferior.columnconfigure(0, weight=1)
        self.master.frame_inferior.columnconfigure(1, weight=1)
        self.master.frame_inferior.columnconfigure(2, weight=1)
        
        #En la fila 0, columna 1 se coloca el fieldframe
        self.field_frame = Fieldframe.Fieldframe(self.master.frame_inferior, "Destino", ["Introduzca un destino: "], "Nombre del destino", None, None, self.listar_destinos,False)
        self.field_frame.grid(row=0, column=1,padx=5, pady=5)
        
    def listar_destinos(self):
        
        nombre_destino = self.field_frame.procurar_todos()[0]
        
        self.master.despejar_frame_inferior()
        self.master.despejar_frame_intermedio()
        tk.Label(self.master.frame_intermedio, font=("Arial",12), wraplength=700, text="Por favor seleccione un destino y haga clic en el botón seleccionar.").place(relx=0.5, rely=0.5, anchor="center")
        
        if nombre_destino is not None:
            
            try:
                
                self.lista_destinos = tk.Listbox(self.master.frame_inferior, selectmode=tk.SINGLE, font=("Arial", 12), height=10, width=50)

                self.destinos = Destino.buscar_destino(nombre_destino)

                if len(self.destinos)>0:
                
                    for destino in self.destinos:

                        self.lista_destinos.insert(tk.END, f"- {destino.nombre}, {destino.pais}")

                    self.lista_destinos.grid(row=0, column=1, padx=5, pady=5)

                    self.boton_seleccionar = tk.Button(self.master.frame_inferior, text="Seleccionar", command=self.seleccionar_destino, height=3, width=15, font=("Arial", 12))
                    self.boton_seleccionar.grid(row=1, column=1, padx=5, pady=5)

                else:
                    messagebox.showwarning("Destino no encontrado", "No se encontraron destinos que coincidan con su búsqueda.")
                    self.solicitar_destino()
                    
            except DestinoInexistente:
                messagebox.showwarning("Destino no encontrado", "No se encontraron destinos que coincidan con su búsqueda.")
                self.solicitar_destino()
            
        else:
            
            self.lista_destinos = tk.Listbox(self.master.frame_inferior, selectmode=tk.SINGLE, font=("Arial", 12), height=10, width=50)
            
            self.destinos = Destino.get_destinos()
            
            for destino in self.destinos:
                
                self.lista_destinos.insert(tk.END, f"- {destino.nombre}, {destino.pais}")
            
            self.lista_destinos.grid(row=0, column=1, padx=5, pady=5)
            
            self.boton_seleccionar = tk.Button(self.master.frame_inferior, text="Seleccionar", command=self.seleccionar_destino, height=3, width=15, font=("Arial", 12))
            self.boton_seleccionar.grid(row=1, column=1, padx=5, pady=5)
            
            
    def seleccionar_destino(self):
        
        try:
            seleccion = self.destinos[self.lista_destinos.curselection()[0]]
            self.reserva_usuario = Reserva(seleccion)
            
            self.pedir_fechas()
            
        except IndexError:
            
            messagebox.showwarning("Selección inválida", "Por favor, seleccione un destino de la lista.")
        
        
    def pedir_fechas(self):
        
        self.master.despejar_frame_inferior()
        self.master.despejar_frame_intermedio()
        
        tk.Label(self.master.frame_intermedio, font=("Arial",12), wraplength=700, text=f"Por favor introduzca las fechas de su estadía en {self.reserva_usuario.destino_viaje.nombre}, (En formato AAAA-MM-DD).").place(relx=0.5, rely=0.5, anchor="center")
        
        criterios = ["Fecha de llegada: ", "Fecha de salida: "]
        valores = ["Ej: 2025-06-13", "Ej: 2025-06-20"]
        self.field_frame = Fieldframe.Fieldframe(self.master.frame_inferior, "Fechas", criterios, "AAAA-MM-DD", valores, None, self.validar_fechas, True)
        self.field_frame.grid(row=0, column=1,padx=5, pady=5, sticky="nsew")
        
    def validar_fechas(self):
            
            fechas = self.field_frame.procurar_todos()
            
            fecha_llegada = fechas[0]
            fecha_salida = fechas[1]
            
            try:
                if self.reserva_usuario.set_ambas_fechas(False, fecha_llegada, fecha_salida):
                    self.pedir_personas()

                else:
                    messagebox.showwarning("Error en fechas", "Por favor, introduzca fechas válidas.")
                    
            except ValueError:
                messagebox.showerror("Error de datos", "Por favor, introduzca datos válidos.")
                
            except FechaInvalida:
                messagebox.showwarning("Error en fechas", "Por favor, introduzca fechas válidas.")
                
    def pedir_personas(self):
        self.master.despejar_frame_inferior()
        self.master.despejar_frame_intermedio()
        
        tk.Label(self.master.frame_intermedio, font=("Arial",12), wraplength=700, text="Por favor introduzca el número de personas con las que viaja (Si no viaja con menores de edad, digite 0 (cero) en el campo respectivo).").place(relx=0.5, rely=0.5, anchor="center")
            
        criterios = ["Adultos: ", "Menores: "]
        valores = ["Ej: 2", "Ej: 1"]
        self.field_frame = Fieldframe.Fieldframe(self.master.frame_inferior, "Viajeros", criterios, "Número de personas", valores, None, self.validar_personas, True)
        self.field_frame.grid(row=0, column=1,padx=5, pady=5, sticky="nsew")
        
    def validar_personas(self):
            
            personas = self.field_frame.procurar_todos()
            
            try:
                
                mayores = int(personas[0])
                menores = int(personas[1])
                
                #1 representa que la reserva es válida y legañ
                if self.reserva_usuario.set_adultos_et_menores(False, mayores, menores)==1:
                    self.mostrar_hoteles()
                    
                #2 representa que la reserva es válida pero ilegal
                elif self.reserva_usuario.set_adultos_et_menores(False, mayores, menores)==2:
                    messagebox.showwarning("Error en viajeros", "Lo lamentamos, pero por motivos legales no podemos permitir que más de dos menores de edad viajen viajen bajo la supervición de un solo adulto.")
                   
                #3 representa que la reserva es inválida 
                else:
                    messagebox.showwarning("Error en viajeros", "Por favor, introduzca un número válido de viajeros.")
            
            except ValueError:  
                messagebox.showerror("Error de datos", "Por favor, introduzca datos válidos.")
                
            except ViajerosInvalidos:
                messagebox.showwarning("Error en viajeros", "Por favor, introduzca un número válido de viajeros.")
                
    def mostrar_hoteles(self):
        self.master.despejar_frame_inferior()
        self.master.despejar_frame_intermedio()
        
        hoteles = self.reserva_usuario.destino_viaje.hoteles_destino
        
        tk.Label(self.master.frame_intermedio, font=("Arial",12), wraplength=700, text="Por favor seleccione un hotel de la lista y haga clic en el botón seleccionar.").place(relx=0.5, rely=0.5, anchor="center")
        
        self.lista_hoteles = tk.Listbox(self.master.frame_inferior, selectmode=tk.SINGLE, font=("Arial", 12), height=10, width=50)
        
        for hotel in hoteles:
            precio = hotel.calcular_precio_esperado_noche(self.reserva_usuario.destino_viaje.fama, self.reserva_usuario.destino_viaje.temporada, self.reserva_usuario.viajeros_adultos, self.reserva_usuario.viajeros_menores)
            precio_str = f"{precio:,.2f}"
            self.lista_hoteles.insert(tk.END, f"- {hotel.nombre} ({hotel.prestigio / 2} Estrellas) {'-' * (40 - len(hotel.nombre) - len(precio_str))} ${precio_str}*")

        self.lista_hoteles.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.master.frame_inferior, text="*Precio estimado por noche, está sujeto a variaciones acorde al tipo de estadía seleccionada.", font=("Arial", 8)).grid(row=1, column=1, padx=5, pady=5)
        
        self.boton_seleccionar = tk.Button(self.master.frame_inferior, text="Seleccionar", command=self.seleccionar_hotel, height=3, width=15, font=("Arial", 12))
        self.boton_seleccionar.grid(row=2, column=1, padx=5, pady=5)
        
    def seleccionar_hotel(self):
        try:
            seleccion = self.lista_hoteles.curselection()[0]
            hotel_seleccionado = self.reserva_usuario.destino_viaje.hoteles_destino[seleccion]
            self.reserva_usuario.hotel_viaje = hotel_seleccionado
            self.seleccionar_habitacion()
            
        except IndexError:
            messagebox.showerror("Selección inválida", "Por favor, seleccione un hotel de la lista.")
            
    def seleccionar_habitacion(self):
        
        self.master.despejar_frame_inferior()
        self.master.despejar_frame_intermedio()
        
        tk.Label(self.master.frame_intermedio, font=("Arial",12), wraplength=700, text="Por favor seleccione el tipo de habitación que desea y haga clic en el botón seleccionar.").place(relx=0.5, rely=0.5, anchor="center")
        
        precios = self.reserva_usuario.hotel_viaje.listar_precios()
        self.lista_habitaciones = tk.Listbox(self.master.frame_inferior, selectmode=tk.SINGLE, font=("Arial", 12), height=10, width=50)
        
        if precios[0] is not None:
            precio_str= f"{precios[0]:,.2f}"
            self.lista_habitaciones.insert(tk.END, f"- Habitación Sencilla {'-' * (45 - len(precio_str))} ${precio_str}*")
        if precios[1] is not None:
            precio_str= f"{precios[1]:,.2f}"
            self.lista_habitaciones.insert(tk.END, f"- Habitación Prémium {'-' * (46 - len(precio_str))} ${precio_str}*")
        if precios[2] is not None:
            precio_str= f"{precios[2]:,.2f}"
            self.lista_habitaciones.insert(tk.END, f"- Habitación Presidencial {'-' * (41 - len(precio_str))} ${precio_str}*")
        
        self.lista_habitaciones.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.master.frame_inferior, text="*Precio por noche.", font=("Arial", 10)).grid(row=1, column=1, padx=5, pady=5)
        
        self.boton_seleccionar = tk.Button(self.master.frame_inferior, text="Seleccionar", command=self.definir_lujo, height=3, width=15, font=("Arial", 12))
        self.boton_seleccionar.grid(row=2, column=1, padx=5, pady=5)
        
    def definir_lujo(self):
        try:
            seleccion = self.lista_habitaciones.get(self.lista_habitaciones.curselection()[0])
            if "Sencilla" in seleccion:
                self.reserva_usuario.lujo_hotel_viaje = 0
            elif "Prémium" in seleccion:
                self.reserva_usuario.lujo_hotel_viaje = 1
            elif "Presidencial" in seleccion:
                self.reserva_usuario.lujo_hotel_viaje = 2
            else:
                messagebox.showerror("Selección inválida", "Por favor, seleccione un tipo de habitación de la lista.")
        except IndexError:
            messagebox.showerror("Selección inválida", "Por favor, seleccione un tipo de habitación de la lista.")
        
        if self.reserva_usuario.lujo_hotel_viaje is not None:
            self.resumir_reserva()
            
    def resumir_reserva(self):
        self.master.despejar_frame_inferior()
        self.master.despejar_frame_intermedio()
        
        tk.Label(self.master.frame_intermedio, font=("Arial",12), wraplength=700, text="Por favor revise su reserva y haga clic en el botón confirmar.").place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(self.master.frame_inferior, text=f"Destino: {self.reserva_usuario.destino_viaje.nombre}", font=("Arial", 14)).grid(row=0, column=1, padx=5, pady=5)
        
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        
        fecha_llegada = self.reserva_usuario.fecha_llegar.strftime("%d de %B de %Y")
        fecha_salida = self.reserva_usuario.fecha_salir.strftime("%d de %B de %Y")
        
        tk.Label(self.master.frame_inferior, text=f"Fecha de llegada: {fecha_llegada}", font=("Arial", 14)).grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.master.frame_inferior, text=f"Fecha de salida: {fecha_salida}", font=("Arial", 14)).grid(row=2, column=1, padx=5, pady=5)
        tk.Label(self.master.frame_inferior, text=f"Viajeros: {self.reserva_usuario.viajeros_adultos} adultos, {self.reserva_usuario.viajeros_menores} menores", font=("Arial", 14)).grid(row=3, column=1, padx=5, pady=5)
        tk.Label(self.master.frame_inferior, text=f"Hotel: {self.reserva_usuario.hotel_viaje.nombre}", font=("Arial", 14)).grid(row=4, column=1, padx=5, pady=5)
        tipo_habitacion = ["Sencilla", "Prémium", "Presidencial"]
        tk.Label(self.master.frame_inferior, text=f"Habitación: {tipo_habitacion[self.reserva_usuario.lujo_hotel_viaje]}", font=("Arial", 14)).grid(row=5, column=1, padx=5, pady=5)
        
        self.boton_confirmar = tk.Button(self.master.frame_inferior, text="Confirmar", command=self.confirmar_reserva, height=3, width=15, font=("Arial", 16))
        self.boton_confirmar.grid(row=6, column=1, padx=5, pady=5)
        
    def confirmar_reserva(self):
        if self.reserva_usuario.confirmar_hotel():
            messagebox.showinfo("Reserva exitosa", "Su reserva ha sido confirmada exitosamente.")
            self.reservar_hotel()
            
        else:
            messagebox.showerror("Error en reserva", "Lo lamentamos, pero no se pudo confirmar su reserva.")
            self.reservar_hotel()