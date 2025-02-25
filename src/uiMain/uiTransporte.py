#|==================================================================================================================================|
#|                                                                                                                                  |
#|  Copyright (c) 2025 Agencia de Viajes Mundo Aventura S.A.                                                                        |
#|                                                                                                                                  |
#|  + Nombre del módulo:                                                                                                            |
#|                                                                                                                                  |
#|      uiTransporte.py                                                                                                             |
#|                                                                                                                                  |
#|  + Resumen:                                                                                                                      |
#|                                                                                                                                  |
#|      Este módulo contiene la interfaz de usuario para la reserva de medios de transporte.                                        |
#|              Se encarga de solicitar al usuario el destino de su viaje, las fechas de llegada y salida (Si aplica),              |
#|              y el número de personas con las que viaja.                                                                          |
#|                                                                                                                                  |
#|  + Codificado por:                                                                                                               |
#|                                                                                                                                  |
#|      - Alejandro Pérez Barrera (2025-02-23) (Creador)                                                                            |
#|                                                                                                                                  |
#|  +Última revisión: 2025-02-25-08-28, AlPerBara                                                                                   |
#|                                                                                                                                  |
#|  + Novedades:                                                                                                                    |
#|                                                                                                                                  |
#|      - Añadida barra de scroll.                                                                                                  |
#|                                                                                                                                  |
#|  + Pendientes en este módulo:                                                                                                    |
#|                                                                                                                                  |
#|      - Verificar errores.                                                                                                        |
#|      - Añadir comentarios.                                                                                                       |
#|                                                                                                                                  |
#|==================================================================================================================================|


import tkinter as tk
from tkinter import messagebox
import os.path, sys, datetime, locale


import Fieldframe

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.gestorAplicacion.transporte.Transporte import Transporte
from src.gestorAplicacion.transporte.Avion import Avion
from src.gestorAplicacion.transporte.Tren import Tren
from src.gestorAplicacion.transporte.Autobus import Autobus
from src.gestorAplicacion.transporte.Empresa import Empresa

from src.gestorAplicacion.reservacionHotel.Destino import Destino

from src.excepciones.DestinoInexistente import DestinoInexistente
from src.excepciones.FechaInvalida import FechaInvalida

from src.excepciones.ViajerosInvalidos import ViajerosInvalidos

from src.baseDatos.GuardarObjetos import GuardarObjetos


# filepath: /c:/Users/USUARIO/Documents/Universidad/POO/AgenciaViajes/pr-ctica-2-g1-e6/src/uiMain/uiTransporte.py


class uiTransporte():
    def __init__(self, master):
        self.master = master
        self.destino_viaje = None
        self.empresa = None
        self.transporte_reserva = None
        self.fecha_ida = None
        self.fecha_vuelta = None
        self.total_viajeros = 0
        self.clase = 0
        self.precio = 0
        self.tiempo = 0

    def reservar_transporte(self):
        """for child in self.winfo_children():
            child.destroy()
        tk.Label(self, text="Bienvenido a la reserva de Transporte.").pack()
        tk.Label(self, text="Aquí podrá reservar Avión, Tren o Autobus.").pack()
        tk.Button(self, text="Iniciar reserva", command=self.next_step).pack()"""
                
        
        #Primero es despejar los frames
        self.master.despejar_todos_los_frames()
        #Definiendo título y descripción, junto con un botón para comenzar
        tk.Label(self.master.frame_superior, text="Reservación de medios de transporte", font=("Arial", 20, "bold")).place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(self.master.frame_intermedio, font=("Arial",12), wraplength=700, text="Puede reservar un medio de transporte para viajar a alguno de los múltiples destinos que ofrecemos, asegúrese de incluir información acerca del número de personas con las que viaja, y la fecha de salida de su viaje.").place(relx=0.5, rely=0.5, anchor="center")
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

                self.destinos = Empresa.buscar_destino(nombre_destino)

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
            
            self.master.despejar_frame_intermedio()
            tk.Label(self.master.frame_intermedio, font=("Arial",12), wraplength=700, text="Mostrando todos nuestros destinos, para ver más destinos, por favor utilice la barra de scroll.").place(relx=0.5, rely=0.5, anchor="center")

            
            self.lista_destinos = tk.Listbox(self.master.frame_inferior, selectmode=tk.SINGLE, font=("Arial", 12), height=10, width=50)
            
            self.scroll = tk.Scrollbar(self.master.frame_inferior, orient="vertical", command=self.lista_destinos.yview)
            
            self.lista_destinos.config(yscrollcommand=self.scroll.set)
            
            self.scroll.grid(row=0, column=2, sticky="ns")
            
            

            
            self.destinos = Destino.get_destinos()
            
            for destino in self.destinos:
                
                self.lista_destinos.insert(tk.END, f"- {destino.nombre}, {destino.pais}")
            
            self.lista_destinos.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
            
            self.boton_seleccionar = tk.Button(self.master.frame_inferior, text="Seleccionar", command=self.seleccionar_destino, height=3, width=15, font=("Arial", 12))
            self.boton_seleccionar.grid(row=1, column=1, padx=5, pady=5)
            
            
    def seleccionar_destino(self):
        
        try:
            self.destino_viaje = self.destinos[self.lista_destinos.curselection()[0]]
            #print(self.destino_viaje.nombre)
            
            self.pedir_fechas()
            
        except IndexError:
            
            messagebox.showwarning("Selección inválida", "Por favor, seleccione un destino de la lista.")
            
            
    
    def pedir_fechas(self):
        
        self.master.despejar_frame_inferior()
        self.master.despejar_frame_intermedio()
        
        tk.Label(self.master.frame_intermedio, font=("Arial",12), wraplength=700, text=f"Por favor introduzca las fechas de su viaje a {self.destino_viaje.nombre}, (En formato AAAA-MM-DD). Si se trata de un viaje de solo ida, deje el espacio de la fecha de retorno en blanco.").place(relx=0.5, rely=0.5, anchor="center")
        
        criterios = ["Fecha de salida: ", "Fecha de retorno: "]
        valores = ["Ej: 2025-06-13", "Ej: 2025-06-20"]
        self.field_frame = Fieldframe.Fieldframe(self.master.frame_inferior, "Fechas", criterios, "AAAA-MM-DD", valores, None, self.validar_fechas, False)
        self.field_frame.grid(row=0, column=1,padx=5, pady=5, sticky="nsew")
        
    def validar_fechas(self):
            
            fechas = self.field_frame.procurar_todos()
            
            fecha_llegada = fechas[0]
            fecha_salida = fechas[1]
            #print(fechas[1])
            
            try:
                if Empresa.set_ambas_fechas(fecha_llegada, fecha_salida):

                    
                    self.mostrar_empresas(self.destino_viaje)

                else:
                    messagebox.showwarning("Error en fechas", "Por favor, introduzca fechas válidas.")
                    
            except ValueError:
                messagebox.showerror("Error de datos", "Por favor, introduzca datos válidos.")
                
            except FechaInvalida:
                messagebox.showwarning("Error en fechas", "Por favor, introduzca fechas válidas.")
                
    
    def mostrar_empresas(self,destino):
        
        self.master.despejar_frame_inferior()
        self.master.despejar_frame_intermedio()
        
        tk.Label(self.master.frame_intermedio, font=("Arial",12), wraplength=700, text="Estas son las opciones de transporte que encontramos. Por favor seleccione una opción de la lista y haga clic en el botón seleccionar.").place(relx=0.5, rely=0.5, anchor="center")
        
        self.lista_empresas = tk.Listbox(self.master.frame_inferior, selectmode=tk.SINGLE, font=("Arial", 12), height=10, width=50)
        
        #self.empresas = 
        
        for empresa in Empresa.listar_empresas_con_destino(destino):
            
            #print(empresa.medio_destino+", "+empresa.nombre)
            self.lista_empresas.insert(tk.END, f"- {empresa.medio_destino}, {empresa.nombre}")
        
        self.lista_empresas.grid(row=0, column=1, padx=5, pady=5)
        
        self.boton_seleccionar = tk.Button(self.master.frame_inferior, text="Seleccionar", command=self.seleccionar_empresa, height=3, width=15, font=("Arial", 12))
        self.boton_seleccionar.grid(row=1, column=1, padx=5, pady=5)
        
    def seleccionar_empresa(self):
        try:
            
            empresa_electa = Empresa.listar_empresas_con_destino(self.destino_viaje)[self.lista_empresas.curselection()[0]]
            #print(empresa_electa.nombre)
            self.empresa = empresa_electa
            

            #print("Antes switch")
            
            if empresa_electa.medio_destino == "Avión":
                #print("Avión ", empresa_electa.nombre)
                self.transporte_reserva = Avion(self.empresa, self.destino_viaje, Empresa.fechas_reserva_usuario()[0],Empresa.fechas_reserva_usuario()[1])
            elif empresa_electa.medio_destino == "Tren":
                
                self.transporte_reserva = Tren(self.empresa, self.destino_viaje, Empresa.fechas_reserva_usuario()[0], Empresa.fechas_reserva_usuario()[1])
                #print("Tren ", empresa_electa.nombre)
            elif empresa_electa.medio_destino == "Autobús":
                #print("Autobús ", empresa_electa.nombre)
                self.transporte_reserva = Autobus(self.empresa, self.destino_viaje, Empresa.fechas_reserva_usuario()[0],Empresa.fechas_reserva_usuario()[1])
                
            # Continue to next step of reservation process
            #print("Empresa seleccionada")
            self.numero_de_viajeros()
            

        except IndexError:
            messagebox.showwarning("Selección inválida", 
                                  "Por favor, seleccione una empresa de la lista.")
            
    def numero_de_viajeros(self):
        
        self.master.despejar_frame_inferior()
        self.master.despejar_frame_intermedio()
        
        tk.Label(self.master.frame_intermedio, font=("Arial",12), wraplength=700, text="Por favor introduzca el número de adultos y menores que viajarán con usted. En caso de no viajar con menores, deje el espacio respectivo en blanco").place(relx=0.5, rely=0.5, anchor="center")
        
        criterios = ["Adultos: ", "Menores: "]
        valores = ["Ej: 2", "Ej: 1"]
        self.field_frame = Fieldframe.Fieldframe(self.master.frame_inferior, "Personas", criterios, "Número de personas", valores, None, self.validar_numero_personas, False)
        self.field_frame.grid(row=0, column=1,padx=5, pady=5, sticky="nsew")
        
        
    def validar_numero_personas(self):
        
        personas = self.field_frame.procurar_todos()
        
        try:
            
            adultos = int(personas[0]) if personas[0] else 0
            menores = int(personas[1]) if personas[1] else 0
            
            total = adultos + menores
            
            resultado_esperado = self.transporte_reserva.set_adultos_et_menores(adultos, menores)

            if resultado_esperado == True:
                
                self.total_viajeros = total
                # Siquiente paso
                self.elegir_clase()
                #print("Siguiente paso")
            
            elif resultado_esperado == 2:
                
                if  isinstance(self.transporte_reserva, Avion):
                    messagebox.showwarning("Error en viajeros", "Lo lamentamos, pero por motivos legales no podemos permitir que más de dos menores de edad viajen viajen bajo la supervición de un solo adulto.")
                    
                elif isinstance(self.transporte_reserva, Tren):
                    messagebox.showwarning("Error en viajeros", "Lo lamentamos, pero por motivos legales no podemos permitir que más de tres menores de edad viajen viajen bajo la supervición de un solo adulto.")
            
            else:
                messagebox.showwarning("Error en viajeros", "Por favor, introduzca un número válido de viajeros.")

        except ValueError:
            messagebox.showerror("Error de datos", "Por favor, introduzca datos válidos.")
            
        except ViajerosInvalidos:
            messagebox.showerror("Error en viajeros", "Por favor, introduzca un número válido de viajeros.")
            
            
    def elegir_clase(self):
        
        self.master.despejar_frame_inferior()
        self.master.despejar_frame_intermedio()
        
        tk.Label(self.master.frame_intermedio, font=("Arial",12), wraplength=700, text="Por favor seleccione la clase en la que desea viajar.").place(relx=0.5, rely=0.5, anchor="center")
        
        self.master.frame_inferior.columnconfigure(0, weight=1)
        self.master.frame_inferior.columnconfigure(1, weight=1)
        self.master.frame_inferior.columnconfigure(2, weight=1)
        
        self.lista_clases = tk.Listbox(self.master.frame_inferior, selectmode=tk.SINGLE, font=("Arial", 12), height=5, width=40)
        
        """if isinstance(self.transporte_reserva, Avion):
            clases = ["Turista", "Business", "Primera Clase"]
        elif isinstance(self.transporte_reserva, Tren):
            clases = ["Básico", "Estándar", "Preferente"]
        elif isinstance(self.transporte_reserva, Autobus):
            clases = ["Normal", "Plus", "Comfort"]
            
        
        
        for clase in len(clases):
            
            precio = 0
            
            if Empresa.round_trip_reserva_usuario():
                precio = self.transporte_reserva.calcular_precio_ida_vuelta(clase)
            
            else:
                precio = self.transporte_reserva.calcular_precio_transporte(clase)
                
                
            precio_str = f"{precio:,.2f}"
            self.lista_clases.insert(tk.END, f"{clase} {'-' * (50 - len(clase) - len(precio_str))} ${precio_str}")"""
            
        if Empresa.round_trip_reserva_usuario():
            precio = self.transporte_reserva.calcular_precio_ida_vuelta(0)
            precio_str = f"{precio:,.2f}"
            self.lista_clases.insert(tk.END, f"* Económico {'-' * (50 - 11 - len(precio_str))} ${precio_str}")
            
            precio = self.transporte_reserva.calcular_precio_ida_vuelta(1)
            precio_str = f"{precio:,.2f}"
            self.lista_clases.insert(tk.END, f"* Normal {'-' * (50 - 6 - len(precio_str))} ${precio_str}")
            
            precio = self.transporte_reserva.calcular_precio_ida_vuelta(2)
            precio_str = f"{precio:,.2f}"
            self.lista_clases.insert(tk.END, f"* Prémium {'-' * (50 - 7 - len(precio_str))} ${precio_str}")
            
        else:
            precio = self.transporte_reserva.calcular_precio_transporte(0)
            precio_str = f"{precio:,.2f}"
            self.lista_clases.insert(tk.END, f"* Económico {'-' * (50 - 11 - len(precio_str))} ${precio_str}")
            
            precio = self.transporte_reserva.calcular_precio_transporte(1)
            precio_str = f"{precio:,.2f}"
            self.lista_clases.insert(tk.END, f"* Normal {'-' * (50 - 6 - len(precio_str))} ${precio_str}")
            
            precio = self.transporte_reserva.calcular_precio_transporte(2)
            precio_str = f"{precio:,.2f}"
            self.lista_clases.insert(tk.END, f"* Prémium {'-' * (50 - 7 - len(precio_str))} ${precio_str}")
        
        self.lista_clases.grid(row=0, column=1, padx=5, pady=5)
        
        self.boton_seleccionar = tk.Button(self.master.frame_inferior, text="Seleccionar", command=self.validar_clase, height=3, width=15, font=("Arial", 12))
        self.boton_seleccionar.grid(row=1, column=1, padx=5, pady=5)
        
    def validar_clase(self):
        
        try:
            
            clase_elegida = self.lista_clases.curselection()[0]
            self.clase = clase_elegida
            
            self.mostrar_resumen()
            #self.calcular_reserva()
            
        except IndexError:
            messagebox.showwarning("Selección inválida", "Por favor, seleccione una clase de la lista.")
            
    def mostrar_resumen(self):
        
        self.master.despejar_frame_inferior()
        self.master.despejar_frame_intermedio()
        
        tk.Label(self.master.frame_intermedio, font=("Arial",12), wraplength=700, text="Este es el resumen de su reserva. Presione confirmar para confirmar su reserva.").place(relx=0.5, rely=0.5, anchor="center")

        
        #self.precio = 0
        
        self.precio = self.empresa.dar_precio(self.transporte_reserva, self.clase, True if self.fecha_vuelta else False)
            
            
        self.tiempo = self.transporte_reserva.tiempo_de_viaje()
    
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    
        resumen_items = [
            f"Destino: {self.destino_viaje.nombre}, {self.destino_viaje.pais}",
            f"Medio de Transporte: {self.empresa.medio_destino}",
            f"Empresa: {self.empresa.nombre}",
            f"Adultos: {self.transporte_reserva._viajeros_adultos}",
            f"Menores: {self.transporte_reserva._viajeros_menores}",
            f"Fecha de Salida: {self.transporte_reserva.fecha_ir.strftime("%d de %B de %Y")}"
        ]
    
        if Empresa.round_trip_reserva_usuario():
            resumen_items.append(f"Fecha de Retorno: {self.transporte_reserva.fecha_volver.strftime("%d de %B de %Y")}")

        resumen_items.extend([
            f"Precio Total: ${self.precio:,.2f}",
            f"Tiempo Estimado de Viaje: {self.tiempo:.2f} horas"
        ])

        for idx, item in enumerate(resumen_items):
            tk.Label(self.master.frame_inferior, font=("Arial", 12), wraplength=700, text=item).grid(row=idx, column=1, padx=5, pady=5)

        tk.Button(self.master.frame_inferior, text="Confirmar", command=self.confirmar_reserva, height=3, width=15, font=("Arial", 12)).grid(row=len(resumen_items), column=1, padx=5, pady=5, sticky="ew")
        
    def confirmar_reserva(self):
        
        
        self.empresa.incrementar_demanda()
        GuardarObjetos.guardar_emtrans(Empresa.get_listado_empresas())
        messagebox.showinfo("Reserva Confirmada", "Su reserva de transporte ha sido confirmada.")
        self.reservar_transporte()

###############################
    """def create_widgets_step1(self):
        for child in self.winfo_children():
            child.destroy()
        tk.Label(self, text="Seleccione Destino:").pack()
        self.ff_destino = Fieldframe(self, ["Destino"])
        self.ff_destino.pack()
        tk.Button(self, text="Siguiente", command=self.set_destino).pack()

    def set_destino(self):
        self.destino = self.ff_destino.get_values()[0]
        self.next_step()

    def create_widgets_step2(self):
        for child in self.winfo_children():
            child.destroy()
        tk.Label(self, text="Ingrese Fechas de Viaje:").pack()
        self.ff_fechas = Fieldframe(self, ["Fecha Ida", "Fecha Vuelta (opcional)"])
        self.ff_fechas.pack()
        tk.Button(self, text="Siguiente", command=self.set_fechas).pack()

    def set_fechas(self):
        vals = self.ff_fechas.get_values()
        self.fecha_ida = vals[0]
        self.fecha_vuelta = vals[1] if vals[1] else None
        self.next_step()

    def create_widgets_step3(self):
        for child in self.winfo_children():
            child.destroy()
        tk.Label(self, text="Seleccione Medio de Transporte:").pack()
        self.ff_medio = Fieldframe(self, ["Avion / Tren / Autobus"])
        self.ff_medio.pack()
        tk.Button(self, text="Siguiente", command=self.set_medio).pack()

    def set_medio(self):
        entrada = self.ff_medio.get_values()[0].lower()
        if entrada == "avion":
            self.medio = Avion(Empresa("Empresa A", 5, 1.2, None, None),
                               self.destino, self.fecha_ida, self.fecha_vuelta)
        elif entrada == "tren":
            self.medio = Tren(Empresa("Empresa B", 4, 1.1, None, None),
                              self.destino, self.fecha_ida, self.fecha_vuelta)
        else:
            self.medio = Autobus(Empresa("Empresa C", 3, 1.0, None, None),
                                 self.destino, self.fecha_ida, self.fecha_vuelta)
        self.next_step()

    def create_widgets_step4(self):
        for child in self.winfo_children():
            child.destroy()
        tk.Label(self, text="Ingrese Número de Adultos y Menores:").pack()
        self.ff_personas = Fieldframe(self, ["Adultos", "Menores"])
        self.ff_personas.pack()
        tk.Button(self, text="Siguiente", command=self.set_adultos_menores).pack()

    def set_adultos_menores(self):
        valores = self.ff_personas.get_values()
        try:
            a = int(valores[0])
            m = int(valores[1])
            if a > 0 and m >= 0:
                self.adultos = a
                self.menores = m
                self.total_viajeros = a + m
                self.next_step()
            else:
                messagebox.showerror("Error", "Valores no válidos.")
        except:
            messagebox.showerror("Error", "Ingrese valores numéricos.")

    def create_widgets_step5(self):
        for child in self.winfo_children():
            child.destroy()
        tk.Label(self, text="Seleccione Clase (0=Economy, 1=Business, 2=First):").pack()
        self.ff_clase = Fieldframe(self, ["Clase"])
        self.ff_clase.pack()
        tk.Button(self, text="Siguiente", command=self.set_clase).pack()

    def set_clase(self):
        try:
            self.clase = int(self.ff_clase.get_values()[0])
        except:
            self.clase = 0
        self.next_step()

    def create_widgets_step6(self):
        for child in self.winfo_children():
            child.destroy()
        self.precio = self.medio.calcular_precio_transporte(None, 0, self.adultos, self.menores, self.clase)
        self.tiempo = self.medio.tiempo_de_viaje()
        tk.Label(self, text=f"Resumen de Transporte:\nDestino: {self.destino}\nViajeros: {self.total_viajeros}\nPrecio: {round(self.precio,2)}\nTiempo Estimado: {round(self.tiempo,2)} hrs").pack()
        tk.Button(self, text="Confirmar", command=self.next_step).pack()

    def create_widgets_step7(self):
        for child in self.winfo_children():
            child.destroy()
        messagebox.showinfo("Reserva Confirmada", "Su reserva de transporte ha sido confirmada.")
        tk.Label(self, text="Reserva finalizada.").pack()

    def next_step(self):
        self.step += 1
        if self.step == 1:
            self.create_widgets_step1()
        elif self.step == 2:
            self.create_widgets_step2()
        elif self.step == 3:
            self.create_widgets_step3()
        elif self.step == 4:
            self.create_widgets_step4()
        elif self.step == 5:
            self.create_widgets_step5()
        elif self.step == 6:
            self.create_widgets_step6()
        elif self.step == 7:
            self.create_widgets_step7()"""