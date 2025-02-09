class Reserva:

    def _init_(self, evento, numPersonas, precio, costoTotal):
        self.evento = evento
        self.numPersonas = numPersonas
        self.costoTotal = numPersonas * precio


    