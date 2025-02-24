import math

from .Transporte import Transporte
from .Empresa import Empresa


class Avion(Transporte):
    
    PRECIO_POR_KM=1463.19
    
    def __init__(self, empresa, destino, fecha_ir, fecha_volver):
        super().__init__(empresa, destino, fecha_ir, fecha_volver)
        
    
    def set_adultos_et_menores(self, mayores, menores):
        
        if (mayores>0 and menores>=0 and ((mayores*2)>=menores)):
            self._viajeros_adultos = mayores
            self._viajeros_menores = menores
            
            return 1
                
        elif mayores>0 and menores>=0:
            return 2
            
        else:
            return 3
    
    
    
    def calcular_precio_transporte(self, fama_destino, temporada_destino, adultos, menores, clase):
        
        personas = adultos + menores
        
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
        
        parcial = (self.PRECIO_POR_KM/1000)*(((math.pow(math.log(self._distancia,5),2))*self._distancia)/((math.sqrt(self._distancia))-math.log(self._distancia,5))*(fama_destino/3)*t*c*personas)
        
        return Empresa.calcular_tarifa(self._destino, parcial)
    
    def calcular_precio_ida_vuelta(self, fama_destino, temporada_destino, adultos, menores, clase):
        
        personas = adultos + menores
        
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
        
        parcial = (self.PRECIO_POR_KM/1000)*(((math.pow(math.log(self._distancia,5),2))*self._distancia)/((math.sqrt(self._distancia))-math.log(self._distancia,5))*(fama_destino/3)*t*c*personas*1.8)
        
        return Empresa.calcular_tarifa(self._destino, parcial)
    
    #Tiempo en horas, velocidad en km/h
    def tiempo_de_viaje(self):
        
        distancia = Transporte.distancia_KM(self._destino.pais, self._destino.region)
        
        return (distancia/720)+0.5