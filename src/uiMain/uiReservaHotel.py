import tkinter as tk    
import Fieldframe

class uiReservaHotel:
    def __init__(self, master):
        self.master = master

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
        self.field_frame = Fieldframe.Fieldframe(self.master.frame_inferior, "Destino", ["Introduzca un destino: "], "Nombre del destino", None, None, self.buscar_destino,False)
        self.field_frame.grid(row=0, column=1, padx=5, pady=5)
        
    def buscar_destino(self):
        print("Buscar")
        nombre_destino = self.field_frame.procurar_todos()[0]
        print(nombre_destino)
        
        