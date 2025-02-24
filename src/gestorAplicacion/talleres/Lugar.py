from gestorAplicacion.talleres.Ubicacion import Ubicacion
class Lugar(Ubicacion):

    Puntuacion = 0
    sitios=[]

    def _init_(self, nro, distancia, sitios):
        self.nro = nro
        self.distancia = distancia
        self.sitios = sitios
    
    def verify(self, doc):
        if doc > 0 and doc < 9999999999:
            return 0
        else:
            return 1
    
    def get_nro(self):
        return self.nro

    def set_nro(self, nro):
        self.nro = nro

    def get_distancia(self):
        return self.distancia

    def set_distancia(self, distancia):
        self.distancia = distancia

    def get_sitios(self):
        return self.sitios

    def set_sitios(self, sitios):
        self.sitios = sitios