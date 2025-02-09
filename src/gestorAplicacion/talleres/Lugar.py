class Lugar(Ubicacion):
    sitios=[]
    def _init_(self, nro, distancia, sitios):
        self.nro = nro
        self.distancia = distancia
        self.sitios = sitios
    