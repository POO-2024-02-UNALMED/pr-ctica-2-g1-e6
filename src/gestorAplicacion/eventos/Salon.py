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
    @property
    def maxCap(self):
        return self._maxCap

    @maxCap.setter
    def maxCap(self, value):
        self._maxCap = value

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, value):
        self._disponible = value

    @property
    def reservado(self):
        return self._reservado

    @reservado.setter
    def reservado(self, value):
        self._reservado = value

    @property
    def serviciosConfirmados(self):
        return self._serviciosConfirmados

    @serviciosConfirmados.setter
    def serviciosConfirmados(self, value):
        self._serviciosConfirmados = value
    
