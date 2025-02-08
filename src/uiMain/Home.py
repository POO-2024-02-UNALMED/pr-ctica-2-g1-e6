#|==================================================================================================================================|
#|                                                                                                                                  |
#|  Copyright (c) 2025 Agencia de Viajes Mundo Aventura S.A.                                                                        |
#|                                                                                                                                  |
#|                                                                                                                                  |
#|  +Nombre del módulo:                                                                                                             |
#|                                                                                                                                  |
#|      Home.py                                                                                                                     |
#|                                                                                                                                  |
#|  +Resumen:                                                                                                                       |
#|                                                                                                                                  |
#|      Este módulo contiene a la clase Home, la cual representa a la ventana de inicio,                                            |
#|              la ventana que se abre de primera al comenzar a ejecutar el programa.                                               |
#|                                                                                                                                  |
#|  +Codificado por:                                                                                                                |
#|                                                                                                                                  |
#|      - Alejandro Pérez Barrera (2025-02-08) (Creador)                                                                            |
#|                                                                                                                                  |
#|  +Última revisión: 2025-02-08-15-57, AlPerBara                                                                                   |
#|                                                                                                                                  |
#|  +Novedades:                                                                                                                     |
#|                                                                                                                                  |
#|      Este espacio está disponible para reportar novedades que se encuentren en este módulo...                                    |
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
        self.root.title("Inicio") #Le coloco su título
        self.root.geometry("800x600") #El tamaño de la ventana es de 800 x 600
        self.root.resizable(0,0) #Así no se puede cambiar el tamaño de la pestaña 😈😈😈🗣️🔥🔥 TODO: Consultar si está permitido que la ventana no sea resizable
        
        
        #El menú de la parte de arriba:
        self.barra_menu= tk.Menu(self.root)#Crear una barra de menú
        self.root.config(menu=self.barra_menu)#Le asigno esa barra a la pestaña root
        self.menu_inicio = tk.Menu(self.barra_menu, tearoff=0)#Ahora creo el botoncito de inicio como tal
        #El tearoff hace que el menu no se pueda desprender de la pestaña principal,
        #se nota que el menu se puede desprender porque encima del menu salen unas rayitas punteadas, pero con tearoff=0 no salen 😀.
        self.menu_inicio.add_command(label="Descripción del Sistema", command=self.descripcion_programa)#Aquí estoy ponendo la opción para ver la descripción TODO: Añadir la funcionalidad para ver la descripción
        self.menu_inicio.add_separator()#Y aquí un separador
        self.menu_inicio.add_command(label="Salir", command=self.root.quit)#Esta es la opción de salir del programa, root.quit me cierra la pestaña
        self.barra_menu.add_cascade(label="Inicio", menu=self.menu_inicio)#Colocar el menú de inicio en la barra de menús
        
        
        #Ahora los frames principales, de izquierda y derecha
        self.frame_dexter = tk.Frame(self.root, bg="green") #TODO: Cambiar o quitar el color de fondo
        self.frame_sinister = tk.Frame(self.root, bg="red") #TODO: Cambiar o quitar el color de fondo
        #Para colocar los frames estoy usando pack, costado de la pantalla correspondiente, y asegurando que ocupen todo su espacio
        self.frame_dexter.pack(side="right", expand=True, fill="both")
        self.frame_sinister.pack(side="left", expand=True, fill="both")
        
        
        #Este es el frame de arriba a la izquierda, para dar la bienvenida y qsy
        self.frame_supra_sinister = tk.Frame(self.frame_sinister, bg="yellow") #TODO: Cambiar o quitar el color de fondo
        self.frame_supra_sinister.pack(pady=10, padx=10,  side="top", anchor="w")
        #Ahora el texto de bienvenida
        self.texto_bienvenida = tk.Label(self.frame_supra_sinister, text="Bienvenido a la agencia de viajes Rumbo Aventura", font=("Arial", 14),wraplength=300, justify="center")
        self.texto_bienvenida.pack(anchor="center")
        #El texto de descripción solo aparece cuando uno le da al boton de descripcion en el menu de inicio
        self.texto_descripcion = tk.Label(self.frame_supra_sinister, wraplength=300, justify="left")
        self.texto_descripcion.pack()
        
        
        #Ahora sigue el frame de las fotos referentes al sistema.
        self.frame_infra_sinister = tk.Frame(self.frame_sinister, bg="blue") #TODO: Cambiar o quitar el color de fondo
        self.frame_infra_sinister.pack(pady=10, padx=10, side="bottom", anchor="w")
        #A continuación el espacio de las fotografías
        
        #Este array guarda todas las fotos del cuadro de abajo a la izquierda
        self.todas_las_fotos = [tk.PhotoImage(file=f"src/uiMain/media/paisajes/imagen{i}.png") for i in range(1, 6)]
        #Aquí se guarda la foto que se vaya a mostrar
        self.ciclo_fotos= cycle(self.todas_las_fotos)
        
        self.marquete_fotos = tk.Label(self.frame_infra_sinister, image=next(self.ciclo_fotos))#En este label se pone la foto para mostrarla
        self.marquete_fotos.pack()
        self.marquete_fotos.bind("<Enter>", self.hover_imagen)#este es el evento cuando se pasa el cursor sobre la foto
        
        #Este es el botón para iniciar el programa
        self.boton_ingreso = tk.Button(self.frame_infra_sinister, text="Comenzar", command=self.comenzar_programa_principal)
        self.boton_ingreso.pack()
        
    
    #El método descripcion_programa muestra el label con la descripción del programa
    def descripcion_programa(self):
        self.texto_descripcion.config(text="Descripción del programa")#TODO: Escribir una descripción para el programa
    
    
    #El método hover_imagen se ejecuta cuando el usuario pasa el cursor sobre la imagen
    def hover_imagen(self, evento):
        #Cuando el cursor se posa sobre la foto, se pasa a la siguiente imagen, con apoyo de un iterable cycle
        self.marquete_fotos.config(image=next(self.ciclo_fotos))
        
    def comenzar_programa_principal(self):
        self.root.destroy()
        Principal.aterrizar()
