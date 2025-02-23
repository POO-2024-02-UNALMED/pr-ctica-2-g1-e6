"""from abc import ABC, abstractmethod

class Transporte(ABC):
    
    def __init__(self, empresa, destino, tipo_asiento, ida_vuelta):
        self.empresa = empresa
        self.destino = destino
        self.tipo_asiento = tipo_asiento
        self.ida_vuelta = ida_vuelta

    @abstractmethod
    def calcular_precio(self):
        pass

    @staticmethod
    def generar_transportes():
        # This method should generate transport objects if none are serialized
        pass

class Bus(Transporte):
    def calcular_precio(self):
        precio_base = 50  # Example base price
        factor_empresa = self.empresa.get_factor()
        factor_destino = self.destination.get_factor()
        factor_asiento = 1.0 if self.tipo_asiento == 'standard' else 1.5
        descuento_ida_vuelta = 0.9 if self.round_trip else 1.0
        return precio_base * factor_empresa * factor_destino * factor_asiento * descuento_ida_vuelta

class Train(Transporte):
    def calcular_precio(self):
        precio_base = 100  # Example base price
        factor_empresa = self.empresa.get_factor()
        factor_destino = self.destination.get_factor()
        factor_asiento = 1.0 if self.tipo_asiento == 'standard' else 1.5
        descuento_ida_vuelta = 0.9 if self.round_trip else 1.0
        return precio_base * factor_empresa * factor_destino * factor_asiento * descuento_ida_vuelta

class Avion(Transporte):
    def calcular_precio(self):
        precio_base = 200  # Example base price
        factor_empresa = self.empresa.get_factor()
        factor_destino = self.destino.get_factor()
        factor_asiento = 1.0 if self.tipo_asiento == 'Turista' else 2.0
        descuento_ida_vuelta = 0.85 if self.ida_vuelta else 1.0
        return precio_base * factor_empresa * factor_destino * factor_asiento * descuento_ida_vuelta

class Empresa:
    def __init__(self, nombre, destinos):
        self.nombre = nombre
        self.destinos = destinos
        self.demand = 1.0  # Initial demand factor

    def get_factor(self):
        return 1.0 + (self.demand * 0.1)  # Example factor calculation based on demand

    def incrementar_demanda(self):
        self.demand += 0.1  # Increase demand when a reservation is made

class Destino:
    def __init__(self, nombre, fama, temporada, distancia):
        self.nombre = nombre
        self.fama = fama
        self.temporada = temporada
        self.distancia = distancia

    def get_factor(self):
        return 1.0 + (self.fama * 0.2) + (self.temporada * 0.3)  # Example factor calculation

class GUI:
    def __init__(self):
        self.empresas = []
        self.destinos = []

    def agregar_empresa(self, empresa):
        self.empresas.append(empresa)

    def agregar_destino(self, destino):
        self.destinos.append(destino)
    
    def hacer_reserva(self, empresa, destino, tipo_asiento, ida_vuelta, transporte_tipo):
        if transporte_tipo == 'Bus':
            transporte = Bus(empresa, destino, tipo_asiento, ida_vuelta)
        elif transporte_tipo == 'Train':
            transporte = Train(empresa, destino, tipo_asiento, ida_vuelta)
        elif transporte_tipo == 'Avion':
            transporte = Avion(empresa, destino, tipo_asiento, ida_vuelta)
        else:
            raise ValueError("Tipo de transporte no válido")

        precio = transporte.calcular_precio()
        empresa.incrementar_demanda()
        return precio

    def calcular_tiempo_estimado(self, destino, velocidad_promedio):
        return destino.distancia / velocidad_promedio  # Time = Distance / Speed"""
    
from abc import ABC, abstractmethod
from datetime import datetime
import os.path, sys

from .Empresa import Empresa

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.excepciones.FechaInvalida import FechaInvalida
   
class Transporte:
    def __init__(self, empresa, destino, fecha_ir, fecha_volver=None):
        self._empresa = empresa
        self._destino = destino
        self._adultos = None
        self._menores = None
        self._is_round_trip = False
        self._fecha_ir = fecha_ir
        self._fecha_volver = fecha_volver
        self._distancia = self.distancia_KM(self.destino.pais, self.destino.region)
      
    #========== SETTERS Y GETTERS ==========
      
    @property
    def empresa(self):
        return self._empresa

    @empresa.setter
    def empresa(self, value):
        self._empresa = value

    @property
    def destino(self):
        return self._destino

    @destino.setter
    def destino(self, value):
        self._destino = value

    @property
    def personas(self):
        return self._personas

    @personas.setter
    def personas(self, value):
        self._personas = value

    @property
    def round_trip(self):
        return self._round_trip

    @round_trip.setter
    def round_trip(self, value):
        self._round_trip = value

    @property
    def fecha_ir(self):
        return self._fecha_ir

    @fecha_ir.setter
    def fecha_ir(self, value):
        self._fecha_ir = value

    @property
    def fecha_volver(self):
        return self._fecha_volver

    @fecha_volver.setter
    def fecha_volver(self, value):
        self._fecha_volver = value

    @property
    def distancia(self):
        return self._distancia

    @distancia.setter
    def distancia(self, value):
        self._distancia = value
        
    #========== MÉTODOS ==========
        
    def validar_fechas(self, fecha_ir, fecha_volver=None):
        fecha_hoy = datetime.today()
        if fecha_volver:
            fecha_ir = datetime.strptime(fecha_ir, "%Y-%m-%d")
            fecha_volver = datetime.strptime(fecha_volver, "%Y-%m-%d")
            
            if (fecha_ir <= fecha_hoy or fecha_volver <= fecha_hoy or fecha_volver <= fecha_ir):
                raise FechaInvalida()
            
            else:
                self._fecha_ir = fecha_ir
                self._fecha_volver = fecha_volver
                self._round_trip = True
                return True
            
        else:
            
            fecha_ir = datetime.strptime(fecha_ir, "%Y-%m-%d")
            
            if (fecha_ir <= fecha_hoy):
                return False
            
            else:
                self._fecha_ir = fecha_ir
                return True
            
        
    @abstractmethod
    def set_adultos_et_menores(self, mayores, menores):
        pass
     
    @abstractmethod
    def calcular_precio_transporte(self, fama_destino, temporada_destino, personas, clase):
        pass
    
    @abstractmethod
    def calcular_precio_ida_vuelta(self, fama_destino, temporada_destino, personas, clase):
        pass
        
    @abstractmethod
    def tiempo_de_viaje(self, distancia):
        pass
    
    def distancia_KM(pais, region):
        if pais=="Colombia":
            if region=="Bolivar":
                return 460.88
            elif region=="Cundinamarca":
                return 278.71
            elif region=="Valle del Cauca":
                return 329.49
            elif region=="Magdalena":
                return 573.62
            elif region=="Amazonas":
                return 1322.06
            elif region=="Atlantico":
                return 532.71
            elif region=="San Andres":
                return 972.14
            elif region=="Risaralda":
                return 158.02
            else:
                return 350.45
        else:
            if pais=="Francia":
                return 8602.81
            elif pais=="Estados Unidos":
                return 3836.29
            elif pais=="Italia":
                return 9359.23
            elif pais=="Peru":
                return 2037.48
            elif pais=="Argentina":
                return 4898.86
            elif pais=="Brasil":
                return 4781.50
            elif pais=="Chile":
                return 4441.34
            elif pais=="España":
                return 8026.88
            elif pais=="Reino Unido":
                return 8461.90
            elif pais=="Japon":
                return 14048.71
            elif pais=="Australia":
                return 14324.28
            elif pais=="Emiratos Arabes Unidos":
                return 13658.18
            else:
                return 5654.45