class Gestion:
    def _init_(self, Documento, Seguro, Precio, Descuento, Presupuesto):
        self.Documento = Documento
        self.Precio = Precio
        self.Seguro = Seguro
        self.Descuento = Descuento
        self.Presupuesto = Presupuesto

    @property
    def Documento(self):
        return self._Documento

    @Documento.setter
    def Documento(self, value):
        self._Documento = value

    @property
    def Seguro(self):
        return self._Seguro

    @Seguro.setter
    def Seguro(self, value):
        self._Seguro = value

    @property
    def Precio(self):
        return self._Precio

    @Precio.setter
    def Precio(self, value):
        self._Precio = value

    @property
    def Descuento(self):
        return self._Descuento

    @Descuento.setter
    def Descuento(self, value):
        self._Descuento = value

    @property
    def Presupuesto(self):
        return self._Presupuesto

    @Presupuesto.setter
    def Presupuesto(self, value):
        self._Presupuesto = value
        
        