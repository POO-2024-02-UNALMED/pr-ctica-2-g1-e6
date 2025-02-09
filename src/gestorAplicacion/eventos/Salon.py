class Salon:
    capacidadMaxima = 74
    def _init_(self, maxCap, disponible, reservado, serviciosConfirmados):
        self.maxCap = maxCap
        self.disponible = disponible
        self.reservado = reservado
        self.serviciosConfirmados = serviciosConfirmados

    def verificarDisponibilidad(self, fecha, hora, lugar):
        return True
    
    def verificarCapacidad(self):
        if self.numPersonas > self.capacidadMaxima:
            return False
        else:
            return True
    
