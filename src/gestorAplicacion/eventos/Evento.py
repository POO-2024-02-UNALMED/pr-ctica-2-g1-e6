class Evento:
    def _init(self, nombre, fecha, precio):
        self.nombre = nombre
        self.fecha = fecha
        self.precio = precio

    def detalles(self, nombre, fecha, precio):
        print("Evento: " + nombre + ", Fecha: " + fecha + ", Precio: $" + precio)