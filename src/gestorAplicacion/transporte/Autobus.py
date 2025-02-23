import math

from .Transporte import Transporte

class Autobus(Transporte):
    
    PRECIO_POR_KM=289.85
    
    def __init__(self, empresa, destino, fecha_ir, fecha_volver):
        super().__init__(empresa, destino, fecha_ir, fecha_volver)

    
    def set_adultos_et_menores(self, mayores, menores):
        if (mayores>0 and menores>=0):
            self._viajeros_adultos = mayores
            self._viajeros_menores = menores
            return 1
        
        else:
            
            return 3
    
    
    
    
    def calcular_precio_transporte(self, fama_destino, temporada_destino, personas, clase):
        
        t = 1.2
        if temporada_destino == 0:
            t = 1
        elif temporada_destino == 1:
            t = 1.2
        elif temporada_destino == 2:
            t = 1.5
        else:
            pass
        
        c = 1.5
        if clase == 0:
            c = 1
        elif clase == 1:
            c = 1.5
        elif clase == 2:
            c = 2
        else:
            pass
        
        total = (self.PRECIO_POR_KM/1000)*(((math.pow(math.log(self._distancia,5),2))*self._distancia)/((math.sqrt(self._distancia))-math.log(self._distancia,5))*(fama_destino/3)*t*c*personas)
        
        return total
    
    def calcular_precio_ida_vuelta(self, fama_destino, temporada_destino, personas, clase):
        
        t = 1.2
        if temporada_destino == 0:
            t = 1
        elif temporada_destino == 1:
            t = 1.2
        elif temporada_destino == 2:
            t = 1.5
        else:
            pass
        
        c = 1.5
        if clase == 0:
            c = 1
        elif clase == 1:
            c = 1.5
        elif clase == 2:
            c = 2
        else:
            pass
        
        total = (self.PRECIO_POR_KM/1000)*(((math.pow(math.log(self._distancia,5),2))*self._distancia)/((math.sqrt(self._distancia))-math.log(self._distancia,5))*(fama_destino/3)*t*c*personas*1.8)
        
        return total
    
    
    #Tiempo en horas, velocidad en km/h
    def tiempo_de_viaje(self, distancia):
        return distancia/40