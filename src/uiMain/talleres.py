from tkinter import Frame, Button, Label, Tk, Entry, messagebox, PhotoImage

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import baseDatos.CargarObjetos
import baseDatos.GuardarObjetos
import gestorAplicacion.talleres.Lugar
import gestorAplicacion.talleres.Gestion

from uiTalleres import uiTalleres
from gestorAplicacion.talleres.Itinerario import Itinerario
from baseDatos.CargarObjetos import CargarObjetos
from baseDatos.GuardarObjetos import GuardarObjetos

registro = Itinerario()

class talleres(Frame):  

    def __init__(self, master=None): 
        super().__init__(master)  
        self.master = master
        self.pack(expand=True, fill="both")  
        self.create_widgets()


    def descuento(self):
        messagebox.showinfo("Información", f"Usted ha sido agregado al grupo: {self.group}")
        self.frame3.config(bg="black", cursor="star")
        self.ti1.config(bg="white", text="Asignación de grupos")
        uiTalleres.funcion2(self, self.transporte)

    def a(self):
        self.transporte = 1
        self.descuento()

    def b(self):
        self.transporte = 2
        self.descuento()

    def c(self):
        self.transporte = 3
        self.descuento()

    def d(self):
        self.transporte = 4
        self.descuento()

    def grupo1(self):
        self.transporte=1
        self.doky.config(text="En que vehiculo desea hacer su recorrido ??")
        self.ti1.config(text="1). Moto 2). Carro express 3). Carro premium 4). Bus turistico ")
        self.group=uiTalleres.funcion1(self, self.documento, self.taller, self.food, self.date, self.transporte, self.nro, self.lugar)
        self.op1.config(bg="purple", image=self.moto, command=self.a)
        self.op1.pack(side="left", ipady=10, ipadx=10, padx=5)
        self.op2.config(bg="purple", image=self.express, command=self.b)
        self.op2.pack(side="left", ipady=10, ipadx=10, padx=5)
        self.op3 = Button(self.frame3, bg="purple", image=self.carro, command=self.c)
        self.op3.pack(side="left", ipady=10, ipadx=10, padx=5)
        self.op4 = Button(self.frame3, bg="purple", image=self.bus, command=self.d)
        self.op4.pack(side="left", ipady=10, ipadx=10, padx=5)

        
    def grupo2(self):
        self.transporte=2
        self.group=uiTalleres.funcion1(self, self.documento, self.taller, self.food, self.date, self.transporte, self.nro, self.lugar)
        self.op1.destroy()
        self.op2.destroy()
        self.transporte=0
        self.descuento()

    def funcion4(self):
        if len(self.food) >= self.nro:
            self.doky.config(text="¿Desea incluir transporte al recorrido?: 1. Si o 2. No")
            self.op3.destroy()
            self.op1.config(text="Si", bg="green", fg="white", image=self.imagetrue, command=self.grupo1)
            self.op2.config(text="Nop", bg="red", fg="white",  image=self.imagefalse, command=self.grupo2) 
            self.op1.pack(ipadx=30, ipady = 30)
            self.op2.pack(ipadx=30, ipady = 30)
        else: 
            self.op1.destroy()
            self.op2.destroy()
            self.op3.destroy()
            self.k += 1
            self.funcion1()
    
    def funcion3(self):
        self.doky.config(text="¿Qué refrigerio desea para este dia?")
        self.ti1.config(text="1. Sandwich, 2. Hamburgesa, 3. Pizza")
        self.op4.destroy()
        self.op1.config(image=self.image21, command=lambda: (self.food.append(1), self.funcion4()))
        self.op2.config(image = self.image22, command=lambda: (self.food.append(2), self.funcion4()))
        self.op3.config(image = self.image23, command=lambda: (self.food.append(3), self.funcion4()))
        self.op1.pack(ipadx=20, ipady = 20)
        self.op2.pack(ipadx=20, ipady = 20)
        self.op3.pack(ipadx=20, ipady = 20)
        


    def funcion2(self):
        self.doky.config(text="¿En que sitio deseas realizar la actividad?")
        self.ti1.config(text="1. Parque Berrio 2. San Antonio 3. San Ignacio o 4. Prado")
        self.op1.config(image=self.image11, padx=30, command=lambda: (self.lugar.append(1), self.funcion3()))
        self.op2.config(image = self.image12, padx=30, command=lambda: (self.lugar.append(2), self.funcion3()))
        self.op3.config(image = self.image13, padx=30, command=lambda: (self.lugar.append(3), self.funcion3()))
        self.op4.config(image = self.image14, padx=30, command=lambda: (self.lugar.append(4), self.funcion3()))
        self.op5.destroy()
        self.op6.destroy()
        self.op7.destroy()
        self.master.geometry("750x600")

    def funcion1(self):
        self.master.geometry("1500x600")
        self.doky.config(text=f"Elija que actividad desea agendar para el dia {self.k} ")
        self.op1=Button(self.frame3, image = self.image1, command=lambda: (self.taller.append(1), self.funcion2()))
        self.op1.pack(side="left", padx=15, pady=0, ipadx=5, ipady=5)
        self.op2=Button(self.frame3, image = self.image2, command=lambda: (self.taller.append(2), self.funcion2()))
        self.op2.pack(side="left", padx=5, pady=0, ipadx=5, ipady=5)
        self.op3=Button(self.frame3, image = self.image3, command=lambda: (self.taller.append(3), self.funcion2()))
        self.op3.pack(side="left", padx=5, pady=0, ipady=5, ipadx=5)
        self.op4=Button(self.frame3, image = self.image4, command=lambda: (self.taller.append(4), self.funcion2()))
        self.op4.pack(side="left", padx=5, pady=0, ipadx=5, ipady=5)
        self.op5=Button(self.frame3, image = self.image5, command=lambda: (self.taller.append(5), self.funcion2()))
        self.op5.pack(side="left", padx=5, pady=0, ipadx=5, ipady=5)
        self.op6=Button(self.frame3, image = self.image6, command=lambda: (self.taller.append(6), self.funcion2()))
        self.op6.pack(side="left", padx=5, pady=0, ipadx=5, ipady=5)
        self.op7=Button(self.frame3, image = self.image7, command=lambda: (self.taller.append(7), self.funcion2()))
        self.op7.pack(side="left", padx=5, pady=0, ipadx=5, ipady=5)
    
    #definir fecha
    def fecha(self):
        if int(self.entra.get()) > 0 and int(self.entra.get()) < 21:
            self.date = int(self.entra.get())
            self.doky.config(bg="purple", fg="yellow")
            self.botonito.destroy()
            self.entra.destroy()
            self.master.geometry("1500x600")
            self.frame3.config(bg="red", cursor="spider")
            self.image1 = PhotoImage(file="src/uiMain/media/talleres/planta.png")
            self.image2 = PhotoImage(file="src/uiMain/media/talleres/ave.png")
            self.image3 = PhotoImage(file="src/uiMain/media/talleres/cultura.png")
            self.image4 = PhotoImage(file="src/uiMain/media/talleres/musica.png")
            self.image5 = PhotoImage(file="src/uiMain/media/talleres/parque.png")
            self.image6 = PhotoImage(file="src/uiMain/media/talleres/tejer.png")
            self.image7 = PhotoImage(file="src/uiMain/media/talleres/tobogan.png")
            self.image11 = PhotoImage(file="src/uiMain/media/talleres/lug1.png")
            self.image12 = PhotoImage(file="src/uiMain/media/talleres/lug2.png")
            self.image13 = PhotoImage(file="src/uiMain/media/talleres/lug3.png")
            self.image14 = PhotoImage(file="src/uiMain/media/talleres/lug4.png")
            self.image21 = PhotoImage(file="src/uiMain/media/talleres/f1.png")
            self.image22 = PhotoImage(file="src/uiMain/media/talleres/f2.png")
            self.image23 = PhotoImage(file="src/uiMain/media/talleres/f3.png")
            self.imagetrue = PhotoImage(file="src/uiMain/media/talleres/true.png")
            self.imagefalse = PhotoImage(file="src/uiMain/media/talleres/false.png")
            self.moto = PhotoImage(file="src/uiMain/media/talleres/moto.png")
            self.express = PhotoImage(file="src/uiMain/media/talleres/express.png")
            self.carro = PhotoImage(file="src/uiMain/media/talleres/carro.png")
            self.bus = PhotoImage(file="src/uiMain/media/talleres/bus.png") 

            self.ti1 = Label(self.frame3, bg="violet", fg="white", text="Haz click en: 1. Plantaton  2. Avevisor  3. casaCultura  4. casaMusica  5. TurcoParque  6. Tejedores o 7. Toboganes")
            self.ti1.pack(padx=100)
            self.taller = []
            self.lugar = []
            self.food = []
            self.transporte = 0
            self.k = 1
            self.funcion1()


            
        else:
            messagebox.showwarning("Advertencia", "Por favor digite un dia del mes entre el 1 y el 20")

    #verificar nro > 0 and < 7 para dias a hacer actividades
    def nro(self):
        if int(self.entra.get()) > 0 and int(self.entra.get()) < 8:
            self.nro = int(self.entra.get())
            self.entra.delete(0, "end")
            self.doky.config(text="¿Qué dia del mes vas a empezar con las actividades? Debe ser antes del dia 21, pues después deben estar listas todas la agenda")
            self.botonito.config(command=self.fecha)
        else:
            messagebox.showwarning("Advertencia", "Solo puede reservar actividades entre 1 y 7 dias en total")



    #Pedimos nro de dias que va a hacer actividades
    def geto(self):
        self.doky.config(text="¿Cuántos dias vas a realizar actividades?")
        self.botonito.config(command=self.nro)
    
    #Pedimos documento al Usuario y lo verificamos k sea mas de 5 numeros y menos de 10
    def verify(self):
        a = float(self.entra.get())
        if a > 9999 and a < 999999999:
            self.documento = self.entra.get()
            self.entra.delete(0, "end")
            self.geto()
        else:
            messagebox.showwarning("Advertencia", "Su documento debe ser un número con mas de 5 digitos y menos de 10")

    def law(self):
        self.frame2.destroy()
        self.frame3 = Frame(self.master, bg="orange", cursor = "clock")
        self.frame3.pack(expand = True, fill="both")
        self.doky=Label(self.frame3, bg="red", fg="white", text="Digite número de documento")
        self.doky.pack(pady=20, ipady=6)
        self.entra = Entry(self.frame3)
        self.entra.pack(pady= 45, ipadx=50, ipady=10)
        self.botonito = Button(self.frame3, text= "Aceptar", font=("Arial", 10), command=self.verify)
        self.botonito.pack(pady = 70, ipady=10, ipadx = 40)

    def create_widgets(self):
        self.frame1 = Frame(self, bg="cyan")
        self.frame1.pack(expand=True, fill="both")
        self.frame1.config(cursor="pirate", relief="sunken")

        self.frame2 = Frame(self, bg="green")
        self.frame2.pack(expand=True, fill="both")
        self.frame2.config(cursor="heart", relief="sunken")  

        self.hola = Label(self.frame1, text="Reservaciones de talleres y actividades", bg="cyan", font=("Arial", 16, "bold"))
        self.hola.pack(side="top", pady = 30)

        self.holak = Label(self.frame2, text="Aquí puede reservar rutas con talleres y actividades emocionantes", bg="green", fg="white", font=("Arial", 16, "bold"))
        self.holak.pack(side="top", pady = 50)
        
        self.field = Button(self.frame2, text="Reservar actividades", bg="orange", command=self.law)
        self.field.pack(ipadx = 50, ipady= 35, pady= 40)

root = Tk()
root.title("New tab")

app = talleres(master=root)
app.mainloop()
