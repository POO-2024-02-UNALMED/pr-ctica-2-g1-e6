from tkinter import Frame, Button, Label, Tk, Entry, messagebox

import baseDatos.CargarObjetos

class talleres(Frame):  
    baseDatos.CargarObjetos.cargar_talleres()
    def __init__(self, master=None): 
        super().__init__(master)  
        self.master = master
        self.pack(expand=True, fill="both")  
        self.create_widgets()
    
    def verify(self):
        a = float(self.entra.get())
        if a > 9999 and a < 999999999:

            self.entra.delete(0, "end")
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
