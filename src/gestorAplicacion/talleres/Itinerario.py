from multimethod import multimethod

class Itinerario:
    def inicializar_atributos(self, actividades, refrigerios, fecha, grupo):
        """Método auxiliar para evitar repetir código"""
        self.actividades = actividades
        self.refrigerios = refrigerios
        self.fecha = fecha
        self.grupo = grupo

    @multimethod
    def __init__(self, actividades: list, refrigerios: list, fecha: int, grupo: int, transporte: int):
        self.inicializar_atributos(actividades, refrigerios, fecha, grupo)
        self.transporte = transporte 

    @multimethod
    def __init__(self, actividades: list, refrigerios: list, fecha: int, grupo: int):
        self.inicializar_atributos(actividades, refrigerios, fecha, grupo)

    @multimethod
    def __init__(self, documentos: list, precios: list, grupo1: int, grupo2: int, fechas: list, lug1: int, lug2: int, lug3: int, lug4: int):
        self.documentos = documentos
        self.precios = precios
        self.grupo1 = grupo1
        self.grupo2 = grupo2
        self.fechas = fechas
        self.lug1 = lug1
        self.lug2 = lug2
        self.lug3 = lug3
        self.lug4 = lug4
    
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

