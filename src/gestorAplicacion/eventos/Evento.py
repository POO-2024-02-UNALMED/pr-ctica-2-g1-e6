class Evento:
    def _init(self, nombre, fecha, precio):
        self.nombre = nombre
        self.fecha = fecha
        self.precio = precio

    def detalles(self, nombre, fecha, precio):
        print("Evento: " + nombre + ", Fecha: " + fecha + ", Precio: $" + precio)
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value