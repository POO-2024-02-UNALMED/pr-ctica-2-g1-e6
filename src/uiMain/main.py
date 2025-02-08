#Esta clase es el inicio de la ejecucion de programa
import tkinter as tk

class Home:#Home es la ventana de inicio, donde uno puede ver las fotos de los desarrolladores y eso
    def __init__(self, root):
        self.root=root #defino la raiz
        self.root.title("Inicio") #Le coloco su título
        self.root.geometry("800x600") #El tamaño de la ventana es de 800 x 600
        
        #El menú de la parte de arriba:
        self.barra_menu= tk.Menu(self.root)#Crear una barra de menú
        self.root.config(menu=self.barra_menu)#Le asigno esa barra a la pestaña root
        self.menu_inicio = tk.Menu(self.barra_menu, tearoff=0)#Ahora creo el botoncito de inicio como tal
        #Sinceramente no estoy seguro de que hace tearoff, solo lo pongo porque así sale en todos los tutoriales
        self.menu_inicio.add_command(label="Descripción del Sistema")#Aquí estoy ponendo la opción para ver la descripción
        self.menu_inicio.add_separator()#Y aquí un separador
        self.menu_inicio.add_command(label="Salir", command=self.root.quit)#Esta es la opción de salir del programa, root.quit me cierra la pestaña
        self.barra_menu.add_cascade(label="Inicio", menu=self.menu_inicio)#Colocar el menú de inicio en la barra de menús


if __name__ == "__main__":
    root = tk.Tk()
    Home(root)
    root.mainloop()
    print("Cerar") #TODO: Quitar esto