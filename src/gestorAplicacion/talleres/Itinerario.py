from multimethod import multimethod

class Itinerario:
    actividades=[]
    @multimethod
    def __init__(self, actividades, refrigerios, fecha, grupo, transporte):
        self.Itinerario(actividades, refrigerios, fecha, grupo)
        self.transporte = transporte
    
    @multimethod
    def __init__(self, actividades, refrigerios, fecha, grupo):
        self.actividades = actividades
        self.refrigerios = refrigerios
        self.fecha = fecha
        self.grupo = grupo

    @multimethod
    def __init__(self, documentos=[], precios=[], grupo1=[], grupo2=[], fechas=[], lug1=0, lug2=0, lug3=0, lug4=0):
        self.documentos = documentos
        self.precios = precios
        self.grupo1 = grupo1
        self.grupo2 = grupo2
        self.fechas = fechas
        self.lug1 = lug1
        self.lug2 = lug2
        self.lug3 = lug3
        self.lug4 = lug4
    
    #Getters y setters emulados para Python como hizo my buddy

    @property
    def actividades(self):
        return self.actividades

    @actividades.setter
    def actividades(self, value):
        self._actividades = value

    @property
    def refrigerios(self):
        return self._refrigerios

    @refrigerios.setter
    def refrigerios(self, value):
        self._refrigerios = value

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

    @property
    def grupo(self):
        return self._grupo

    @grupo.setter
    def grupo(self, value):
        self._grupo = value

    @property
    def transporte(self):
        return self._transporte

    @transporte.setter
    def transporte(self, value):
        self._transporte = value

    @property
    def documentos(self):
        return self._documentos

    @documentos.setter
    def documentos(self, value):
        self._documentos = value

    @property
    def precios(self):
        return self._precios

    @precios.setter
    def precios(self, value):
        self._precios = value

    @property
    def grupo1(self):
        return self._grupo1

    @grupo1.setter
    def grupo1(self, value):
        self._grupo1 = value

    @property
    def grupo2(self):
        return self._grupo2

    @grupo2.setter
    def grupo2(self, value):
        self._grupo2 = value

    @property
    def fechas(self):
        return self._fechas

    @fechas.setter
    def fechas(self, value):
        self._fechas = value

    @property
    def lug1(self):
        return self._lug1

    @lug1.setter
    def lug1(self, value):
        self._lug1 = value

    @property
    def lug2(self):
        return self._lug2

    @lug2.setter
    def lug2(self, value):
        self._lug2 = value

    @property
    def lug3(self):
        return self._lug3

    @lug3.setter
    def lug3(self, value):
        self._lug3 = value

    @property
    def lug4(self):
        return self._lug4

    @lug4.setter
    def lug4(self, value):
        self._lug4 = value

