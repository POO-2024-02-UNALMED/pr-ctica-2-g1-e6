


import tkinter as tk
from tkinter import messagebox    
import Fieldframe

import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.gestorAplicacion.reservacionHotel.Destino import Destino
from src.gestorAplicacion.reservacionHotel.Reserva import Reserva

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
            self.lista_destinos = tk.Listbox(self.master.frame_inferior, selectmode=tk.SINGLE, font=("Arial", 12), height=10, width=50)
            
            self.destinos = Destino.buscar_destino(nombre_destino)
            
            for destino in self.destinos:
                
                self.lista_destinos.insert(tk.END, destino.nombre)
            
            self.lista_destinos.grid(row=0, column=1, padx=5, pady=5)
            
            self.boton_seleccionar = tk.Button(self.master.frame_inferior, text="Seleccionar", command=self.seleccionar_destino, height=3, width=15, font=("Arial", 12))
            self.boton_seleccionar.grid(row=1, column=1, padx=5, pady=5)
            
        else:
            
            self.lista_destinos = tk.Listbox(self.master.frame_inferior, selectmode=tk.SINGLE, font=("Arial", 12), height=10, width=50)
            
            self.destinos = Destino.get_destinos()
            
            for destino in self.destinos:
                
                self.lista_destinos.insert(tk.END, destino.nombre)
            
            self.lista_destinos.grid(row=0, column=1, padx=5, pady=5)
            
            self.boton_seleccionar = tk.Button(self.master.frame_inferior, text="Seleccionar", command=self.seleccionar_destino, height=3, width=15, font=("Arial", 12))
            self.boton_seleccionar.grid(row=1, column=1, padx=5, pady=5)
            
            
    def seleccionar_destino(self):
        
        try:
            seleccion = self.destinos[self.lista_destinos.curselection()[0]]
            self.reserva_usuario = Reserva(seleccion)
            print("Nombre: "+self.reserva_usuario.destino_viaje.nombre)
            print("Elección: ",seleccion)
            self.pedir_fechas()
            
        except IndexError:
            
            messagebox.showwarning("Selección inválida", "Por favor, seleccione un destino de la lista.")
        
        
    def pedir_fechas():
        pass