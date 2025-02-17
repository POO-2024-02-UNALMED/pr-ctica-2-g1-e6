class Lugar(Ubicacion):
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
    