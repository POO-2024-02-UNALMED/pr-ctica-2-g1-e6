from tkinter import Frame, Button, Entry, Label
class talleres(Frame):
    def _init_(self, master=None):
        super()._init_(master)
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.frame1 = Frame(self, bg="cyan")
        self.frame1.pack(expand=True, fill="both")
        self.frame1.config(cursor="pirate", relief="sunken")

        self.frame2 = Frame(self, bg="green")
        self.frame2.pack(expand=True, fill="both")
        self.frame2.config(cursor="hearth", relief="sunken")

        self.hola = Label(self.frame1)
        self.hola["text"] = "Reservaciones de talleres y actividades"
        self.hola.pack(side="top")

        self.holak = Label(self.frame2)
        self.holak["text"] = " Aquí puede reservar rutas con talleres y actividades emocionantes"
        self.holak.pack(side="top")
        
        self.field = Button(self.frame2)
        self.field["text"] = "Reservar actividades"
        self.field.pack()
