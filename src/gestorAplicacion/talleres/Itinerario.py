from multimethod import multimethod

class Itinerario:
    actividades=[]
    @multimethod
    def _init_(self, actividades, refrigerios, fecha, grupo, transporte):
        self.Itinerario(actividades, refrigerios, fecha, grupo)
        self.transporte = transporte
    
    @multimethod
    def _init_(self, actividades, refrigerios, fecha, grupo):
        self.actividades = actividades
        self.refrigerios = refrigerios
        self.fecha = fecha
        self.grupo = grupo

    @multimethod
    def __init__(self, documentos=0, precios=0, grupo1=0, grupo2=0, fechas=0, lug1=0, lug2=0, lug3=0, lug4=0):
        self.documentos = documentos
        self.precios = precios
        self.grupo1 = grupo1
        self.grupo2 = grupo2
        self.fechas = fechas
        self.lug1 = lug1
        self.lug2 = lug2
        self.lug3 = lug3
        self.lug4 = lug4

