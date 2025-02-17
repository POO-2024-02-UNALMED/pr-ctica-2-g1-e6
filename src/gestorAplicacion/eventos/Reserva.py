class Reserva:

    def _init_(self, evento, numPersonas, precio, costoTotal):
        self.evento = evento
        self.numPersonas = numPersonas
        self.costoTotal = numPersonas * precio

    @property
    def evento(self):
        return self._evento

    @evento.setter
    def evento(self, value):
        self._evento = value

    @property
    def numPersonas(self):
        return self._numPersonas

    @numPersonas.setter
    def numPersonas(self, value):
        self._numPersonas = value
        self._costoTotal = self._numPersonas * self._precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value
        self._costoTotal = self._numPersonas * self._precio

    @property
    def costoTotal(self):
        return self._costoTotal

    @costoTotal.setter
    def costoTotal(self, value):
        self._costoTotal = value

    