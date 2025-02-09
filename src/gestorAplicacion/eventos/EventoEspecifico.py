class eventoEspecifico(Evento):
    def _init_(self, nombre, fecha, precio, tipoEvento):
        super()._init_(nombre, fecha, precio)
        self.tipoEvento = tipoEvento

    def valido(self):
        if self.evento != "":
            return True

