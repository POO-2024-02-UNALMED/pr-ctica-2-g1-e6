#|==================================================================================================================================|
#|                                                                                                                                  |
#|  Copyright (c) 2025 Agencia de Viajes Mundo Aventura S.A.                                                                        |
#|                                                                                                                                  |
#|                                                                                                                                  |
#|  + Nombre del módulo:                                                                                                            |
#|                                                                                                                                  |
#|      Home.py                                                                                                                     |
#|                                                                                                                                  |
#|  + Resumen:                                                                                                                      |
#|                                                                                                                                  |
#|      Este módulo contiene a la clase Home, la cual representa a la ventana de inicio,                                            |
#|              la ventana que se abre de primera al comenzar a ejecutar el programa.                                               |
#|                                                                                                                                  |
#|  + Codificado por:                                                                                                               |
#|                                                                                                                                  |
#|      - Alejandro Pérez Barrera (2025-02-08) (Creador)                                                                            |
#|                                                                                                                                  |
#|  + Última revisión: 2025-02-09-15-46, AlPerBara                                                                                  |
#|                                                                                                                                  |
#|  + Novedades:                                                                                                                    |
#|                                                                                                                                  |
#|      Este espacio está disponible para reportar novedades que se encuentren en este módulo...                                    |
#|                                                                                                                                  |
#|  + Pendientes en este módulo:                                                                                                    |
#|                                                                                                                                  |
#|      - Consultar si la ventana puede ser NO resizable.                                                                           |
#|      - Cambiar o eliminar el color del frame principal derecho.                                                                  |
#|      - Cambiar o eliminar el color del frame principal izquierdo.                                                                |
#|      - Cambiar o eliminar el color del frame superior izquierdo.                                                                 |
#|      - Cambiar o eliminar el color del frame inferior izquierdo.                                                                 |
#|      - Cambiar o eliminar el color del frame superior derecho.                                                                   |
#|      - Agregar nombre y descripción de los desarrolladores (Faltan 3 de 3).                                                      |
#|      - Cambiar o eliminar el color del frame inferior derecho.                                                                   |
#|      - Elaborar una descripción para el programa.                                                                                |
#|                                                                                                                                  |
#|==================================================================================================================================|

from itertools import cycle #Cycle se utiliza para pasar por las imágenes de los desarrolladores e imágenes asociadas al programa.
import tkinter as tk #Tkinter se utiliza para crear la interfaz gráfica

import Principal #Principal se utiliza para poder continuar con la ejecución en la pestaña principal del programa.

#Este método es solo para poder empezar la ejecución de esta clase desde aquí sin recibir el error TypeError: 'module' object is not callable
def aterrizar():
    root = tk.Tk()
    Home(root)
    root.mainloop()

class Home:#Home es la ventana de inicio, donde uno puede ver las fotos de los desarrolladores y eso
    def __init__(self, root):
        
        self.root=root #defino la raiz
        self.root.iconphoto(False, tk.PhotoImage(file=f"src/uiMain/media/iconos/icono_principal.png"))
        self.root.title("Inicio") #Le coloco su título
        self.root.geometry("800x600") #El tamaño de la ventana es de 800 x 600
        self.root.resizable(0,0) #Así no se puede cambiar el tamaño de la pestaña 😈😈😈🗣️🔥🔥 TODO: Consultar si está permitido que la ventana no sea resizable
        
        
        #========== MENÚ DE LA PARTE SUPERIOR ==========
        #El menú de la parte de arriba:
        self.barra_menu= tk.Menu(self.root)#Crear una barra de menú
        self.root.config(menu=self.barra_menu)#Le asigno esa barra a la pestaña root
        self.menu_inicio = tk.Menu(self.barra_menu, tearoff=0)#Ahora creo el botoncito de inicio como tal
        #El tearoff hace que el menu no se pueda desprender de la pestaña principal,
        #se nota que el menu se puede desprender porque encima del menu salen unas rayitas punteadas, pero con tearoff=0 no salen 😀.
        self.menu_inicio.add_command(label="Descripción del Sistema", command=self.descripcion_programa)#Aquí estoy ponendo la opción para ver la descripción
        self.menu_inicio.add_separator()#Y aquí un separador
        self.menu_inicio.add_command(label="Salir", command=self.root.quit)#Esta es la opción de salir del programa, root.quit me cierra la pestaña
        self.barra_menu.add_cascade(label="Inicio", menu=self.menu_inicio)#Colocar el menú de inicio en la barra de menús
        
        
        #Ahora los frames principales, de izquierda y derecha
        self.frame_dexter = tk.Frame(self.root, bg="green") #TODO: Cambiar o quitar el color de fondo
        self.frame_sinister = tk.Frame(self.root, bg="red") #TODO: Cambiar o quitar el color de fondo
        #Para colocar los frames estoy usando place, uno va desde el inicio hasta la mitad de la ventana, otro desde la mitad hasta el final
        self.frame_dexter.place(relheight=1,relwidth=0.5,relx=0.5,rely=0)
        self.frame_sinister.place(relheight=1,relwidth=0.5,relx=0,rely=0)
        
        
        #========== RECUADRO SUPERIOR IZQUIERDO ==========
        #Este es el frame de arriba a la izquierda, para dar la bienvenida y qsy
        self.frame_supra_sinister = tk.Frame(self.frame_sinister, bg="yellow") #TODO: Cambiar o quitar el color de fondo
        self.frame_supra_sinister.place(relheight=0.4,relwidth=1,relx=0,rely=0)
        #Ahora el texto de bienvenida
        self.texto_bienvenida = tk.Label(self.frame_supra_sinister, text="Bienvenido a la agencia de viajes Rumbo Aventura", font=("Arial", 16),wraplength=300, justify="center")
        self.texto_bienvenida.pack(anchor="center", fill="x",pady=(10,0))
        #Este label es puro informativo
        self.texto_haz_clic = tk.Label(self.frame_supra_sinister, text="Haz clic en la imagen para comenzar", font=("Arial", 12),wraplength=300, justify="center")
        self.texto_haz_clic.pack(anchor="center",fill="x")
        #Label para poner el emoticón
        self.emoticon = tk.Label(self.frame_supra_sinister, text="⬇️",font=("Segoe UI Emoji",14), justify="center")
        self.emoticon.pack(anchor="center",fill="x")
        #El texto de descripción solo aparece cuando uno le da al boton de descripcion en el menu de inicio
        self.texto_descripcion = tk.Label(self.frame_supra_sinister, wraplength=300, justify="left")
        self.texto_descripcion.pack(anchor="center",fill="x")
        
        
        #========== RECUADRO INFERIOR IZQUIERDO ==========
        #Ahora sigue el frame de las fotos referentes al sistema.
        self.frame_infra_sinister = tk.Frame(self.frame_sinister, bg="blue") #TODO: Cambiar o quitar el color de fondo
        self.frame_infra_sinister.place(relheight=0.6,relwidth=1,relx=0,rely=0.4)
        #A continuación el espacio de las fotografías
        
        #Este array guarda todas las fotos del cuadro de abajo a la izquierda
        self.todas_las_fotos = [tk.PhotoImage(file=f"src/uiMain/media/paisajes/imagen{i}.png") for i in range(1, 6)]
        #Aquí se guarda la foto que se vaya a mostrar
        self.ciclo_fotos= cycle(self.todas_las_fotos)
        
        self.marquete_fotos = tk.Label(self.frame_infra_sinister, image=next(self.ciclo_fotos))#En este label se pone la foto para mostrarla
        self.marquete_fotos.pack(fill="both", expand=True)
        self.marquete_fotos.bind("<Enter>", self.hover_imagen)#este es el evento cuando se pasa el cursor sobre la foto
        self.marquete_fotos.bind("<Button-1>",self.comenzar_programa_principal)
        #Este es el botón para iniciar el programa -----> LO QUITÉ A FAVOR DE USAR LA FOTO COMO BOTÓN
        #self.boton_ingreso = tk.Button(self.frame_infra_sinister, text="Comenzar", command=self.comenzar_programa_principal)
        #self.boton_ingreso.pack()
        
        
        #========== RECUADRO SUPERIOR DERECHO ==========
        #El frame con la información de los desarrolladores:
        self.frame_supra_dexter = tk.Frame(self.frame_dexter, bg="orange") #TODO: Cambiar o quitar el color de fondo
        self.frame_supra_dexter.place(relheight=0.4,relwidth=1,relx=0,rely=0)
        #Esta es la información acerca de los desarrolladores:
        self.los_devs = ["Nombre 1: DESCRIPCIÓN 1","Nombre 2: DESCRIPCIÓN 2","Nombre 3: DESCRIPCIÓN 3"]#TODO: Actualizar los textos para mostrar la verdadera información de los desarrolladores
        self.iterable_devs= cycle(self.los_devs)
        #Este label muestra la info de los desarrolladores
        self.texto_info_devs = tk.Label(self.frame_supra_dexter,  wraplength=300, justify="center", text="Desarrolladores", anchor="center", font=("Arial", 12))
        self.texto_info_devs.pack(expand=True)
        self.texto_info_devs.bind("<Button-1>", self.pasar_siguiente_dev)#Cuando se hace clic sobre la descripción de un desarrollador se pasa al siguiente
        
        
        #========== RECUADRO INFERIOR DERECHO ==========
        #Este frame contiene las fotos:
        self.frame_infra_dexter = tk.Frame(self.frame_dexter, bg="purple") #TODO: Cambiar o quitar el color de fondo
        self.frame_infra_dexter.place(relheight=0.6,relwidth=1,relx=0,rely=0.4)
        self.frame_fotos_devs = tk.Frame(self.frame_infra_dexter)
        self.frame_fotos_devs.pack(expand=True, fill="both")
        self.cambiar_fotos_dev()
        
    
    #========== MÉTODOS DE LA VENTANA ==========
    
    #El método descripcion_programa muestra el label con la descripción del programa
    def descripcion_programa(self):
        self.texto_descripcion.config(text="Descripción del programa:                            d                e", font=("Arial", 12))#TODO: Escribir una descripción para el programa
    
    
    #El método hover_imagen se ejecuta cuando el usuario pasa el cursor sobre la imagen
    def hover_imagen(self, evento):
        #Cuando el cursor se posa sobre la foto, se pasa a la siguiente imagen, con apoyo de un iterable cycle
        self.marquete_fotos.config(image=next(self.ciclo_fotos))
        
    #Para comenzar el programa se redirige al módulo con la ventana principal
    def comenzar_programa_principal(self, evento):
        self.root.destroy()
        Principal.aterrizar()
        
    #Este método pasa al texto correspondiente al siguiente dev, y llama al metodo que actualiza las fotos
    def pasar_siguiente_dev(self, evento):
        self.texto_info_devs.config(text=next(self.iterable_devs))
        self.cambiar_fotos_dev()
      
    #este método cambia las fotos  
    def cambiar_fotos_dev(self):
        for widget in self.frame_infra_dexter.winfo_children():
            widget.destroy() #Primero destruye las fotos antiguas (Si las hay)
        
        #texto= self.texto_info_devs.cget("text")
        if self.texto_info_devs.cget("text").startswith("Nombre"): #Verificando que el label contenga la palabra "Nombre",
                                                                #porque si la contiene, deben aparecer las fotos de algún desarrollador
            #En esta variable se guarda el número del desarrollador que toca mostrar en pantalla
            id_desarrollador = self.los_devs.index(self.texto_info_devs.cget("text"))+1
            
            #Ubicar cada foto
            for i in range(2):
                for j in range(2):
                    foto = tk.PhotoImage(file=f"src/uiMain/media/personas/imagen{id_desarrollador}_{i*2+j+1}.png")
                    foto = foto.subsample(2,2)
                    lbl = tk.Label(self.frame_infra_dexter, image=foto)
                    lbl.image = foto
                    lbl.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")
                    
