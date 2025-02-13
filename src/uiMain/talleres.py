from tkinter import Frame, Button, Entry, Label
class talleres(Frame):
    def _init_(self, master=None):
        super()._init_(master)
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.hola = Label(self)