from tkinter import Frame, Button, Label, Tk, Entry, messagebox

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import baseDatos.CargarObjetos
import baseDatos.GuardarObjetos
import gestorAplicacion.talleres.Lugar
import gestorAplicacion.talleres.Gestion

from gestorAplicacion.talleres.Itinerario import Itinerario
from baseDatos.CargarObjetos import CargarObjetos
from baseDatos.GuardarObjetos import GuardarObjetos

registro = Itinerario()

class talleres(Frame):  
    GuardarObjetos.guardar_registro(registro)

    def __init__(self, master=None): 
        super().__init__(master)  
        self.master = master
        self.pack(expand=True, fill="both")  
        self.create_widgets()
    
    #Empezar a preguntar por las actividades, lugares y refrigerios
    def activityz(self):
        pass

    #definir fecha
    def fecha(self):
        if int(self.entra.get()) > 0 and int(self.entra.get()) < 21:
            fecha = int(self.entra.get())
            self.botonito.destroy()
            self.entra.destroy()
            self.doky.destroy()
            self.frame3.config(bg="red", cursor="spider")
            self.
        else:
            messagebox.showwarning("Advertencia", "Por favor digite un dia del mes entre el 1 y el 20")

    #verificar nro > 0 and < 7 para dias a hacer actividades
    def nro(self):
        if int(self.entra.get()) > 0 and int(self.entra.get()) < 8:
            nro = int(self.entra.get())
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
            documento = self.entra.get()
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
