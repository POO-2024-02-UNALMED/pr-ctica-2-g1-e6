from datetime import datetime
import os, sys
import random

from .Transporte import Transporte
from .Avion import Avion
from .Autobus import Autobus
from .Tren import Tren

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.gestorAplicacion.reservacionHotel.Destino import Destino

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.baseDatos.CargarObjetos import CargarObjetos

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.excepciones.FechaInvalida import FechaInvalida

class Empresa:
    _empresas = []
    _datos_ya_cargados = False

    def __init__(self, nombre, prestigio, tasa, destinos_disponibles, medio_destino):
        self._nombre = nombre
        self._prestigio = prestigio  # Escala de [1 10]
        self._tasa = tasa  # Tasa de comisión
        self._destinos_disponibles = destinos_disponibles
        self._medio_destino = medio_destino
        
        self._fechas_reserva_usuario = []
        self._round_trip_reserva_usuario = False
        
        
    #========== GETTERS Y SETTERS ==========
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
        
    @property
    def prestige(self):
        return self._prestige
    
    @prestige.setter
    def prestige(self, value):
        self._prestige = value
        
    @property
    def rate(self):
        return self._rate
    
    @rate.setter
    def rate(self, value):
        self._rate = value
        
    @property
    def destinos_disponibles(self):
        return self._destinos_disponibles
    
    @destinos_disponibles.setter
    def destinos_disponibles(self, value):
        self._destinos_disponibles = value
        
    @property
    def medio_destino(self):
        return self._medio_destino
    
    @medio_destino.setter
    def medio_destino(self, value):
        self._medio_destino = value

    #========== MÉTODOS DE CLASE ==========
    
    @classmethod
    def get_listado_empresas(cls):
        if cls._datos_ya_cargados:
            return cls._empresas
        
        else:
            empresas = CargarObjetos.cargar_empresas()
            
            if empresas == []:
                cls.set_listado_empresas(cls.generador_de_datos())
                cls._datos_ya_cargados = True
                return cls._empresas
            else:
                cls.set_listado_empresas(empresas)
                cls._datos_ya_cargados = True
                return cls._empresas
    
    @classmethod
    def set_listado_empresas(cls, empresas):
        cls._empresas = empresas

    #========== MÉTODOS ==========
    def calcular_tarifa(self, destino, precio_base):
        """
        Calculate final price including company's commission
        Takes into account:
        - Company's base rate
        - Company's prestige
        - Destination's fame
        - Destination's season
        """
        # Base commission calculation
        comision_base = precio_base * (self._rate / 100)
        
        # Adjust based on company prestige (higher prestige = higher commission)
        factor_prestigio = 1 + (self._prestige / 20)  # Max 50% increase for top prestige
        
        # Adjust based on destination fame and season
        factor_destino = 1 + ((destino.fama / 10) + (destino.temporada / 5))
        
        comision_final = comision_base * factor_prestigio * factor_destino
        
        return precio_base + comision_final

    @staticmethod
    def generador_de_datos(): #Generar datos iniciales de empresas
        return [ #TODO: Agregar empresas
                #En el corchete va un array con los destinos, el número indica el medio de transporte que ofrece la empresa
                #1 indica autobús, 2 indica tren, 3 indica avión
            Empresa("Avianza", (random.randint(12,20)/2), (random.randint(100,400)/20), [Destino.get_destinos[0],Destino.get_destinos[2], Destino.get_destinos[3], Destino.get_destinos[4], Destino.get_destinos[5],
                                                                                         Destino.get_destinos[7], Destino.get_destinos[8], Destino.get_destinos[9], Destino.get_destinos[11], Destino.get_destinos[12], 
                                                                                         Destino.get_destinos[13], Destino.get_destinos[14]], 3),
            Empresa("LATA", (random.randint(12,20)/2), (random.randint(100,400)/20), [Destino.get_destinos[2], Destino.get_destinos[3], Destino.get_destinos[4], Destino.get_destinos[5], Destino.get_destinos[6],
                                                                                      Destino.get_destinos[7], Destino.get_destinos[8], Destino.get_destinos[9], Destino.get_destinos[11], Destino.get_destinos[12],
                                                                                      Destino.get_destinos[13], Destino.get_destinos[14]], 3),
            Empresa("Brasil Express", (random.randint(12,20)/2), (random.randint(100,400)/20),  [Destino.get_destinos[3], Destino.get_destinos[5], Destino.get_destinos[8], Destino.get_destinos[13]], 1),
            Empresa("Cotrans", (random.randint(12,20)/2), (random.randint(100,400)/20),  [Destino.get_destinos[3], Destino.get_destinos[5], Destino.get_destinos[7], Destino.get_destinos[15]], 1),
            Empresa("Ferro Nal", (random.randint(12,20)/2), (random.randint(100,400)/20), [Destino.get_destinos[3], Destino.get_destinos[5], Destino.get_destinos[7], Destino.get_destinos[8], Destino.get_destinos[13]], 2),
            Empresa("Salta", (random.randint(12,20)/2), (random.randint(100,400)/20), [Destino.get_destinos[10]], 3),
            Empresa("AeroEuropa", (random.randint(12,20)/2), (random.randint(100,400)/20), [Destino.get_destinos[0], Destino.get_destinos[1], Destino.get_destinos[12], Destino.get_destinos[16]], 3),
            Empresa("Air Go", (random.randint(12,20)/2), (random.randint(100,400)/20), [Destino.get_destinos[0], Destino.get_destinos[2], Destino.get_destinos[9], Destino.get_destinos[11], Destino.get_destinos[16], 
                                                                                        Destino.get_destinos[17]], 3),
            Empresa("Quanto", (random.randint(12,20)/2), (random.randint(100,400)/20), [Destino.get_destinos[12], Destino.get_destinos[16], Destino.get_destinos[18]], 3),
            Empresa("Estirar", (random.randint(12,20)/2), (random.randint(100,400)/20), [Destino.get_destinos[6], Destino.get_destinos[19]], 3)
        ]
    
        
    @staticmethod
    def buscar_destino(clave):
        
        return Destino.buscar_destino(clave)
    
    @staticmethod
    def cantidad_numerica_resultados(resultados_busqueda):
        
        if len(resultados_busqueda)==0:
            return 0
        
        elif len(resultados_busqueda)==1:
            return 1
        
        else:
            return 2
    
    
    #Establecer las fechas de ida y vuelta
    def set_ambas_fechas(self, fecha_ir, fecha_volver=None):
        
        fecha_hoy = datetime.today()
        
        fecha_ir = datetime.strptime(fecha_ir, "%Y-%m-%d")
        
        if fecha_volver is not None:
            
            if (fecha_ir <= fecha_hoy or fecha_volver <= fecha_hoy or fecha_volver <= fecha_ir):
                raise FechaInvalida()
            
            else:
                self._fechas_reserva_usuario.append(fecha_ir)
                self._fechas_reserva_usuario.append(fecha_volver)
                self._round_trip_reserva_usuario = True
                return True
            
        else:
            
            fecha_ir = datetime.strptime(fecha_ir, "%Y-%m-%d")
            
            if (fecha_ir <= fecha_hoy):
                raise FechaInvalida()
            
            else:
                self._fechas_reserva_usuario.append(fecha_ir)
                return True
    
    @classmethod    
    def listar_empresas_con_destino(cls, destino):
        
        #Retornar cada empresa en el listado de empresas SI el destino está en los destinos disponibles de la empresa
        return [empresa for empresa in cls._empresas if destino in empresa._destinos_disponibles]
    
    
    
    #Crear el transporte, dependiendo de que empresa ofrece el servicio
    #1 indica autobús, 2 indica tren, 3 indica avión
    def definir_transporte(self, empresa, destino):
        
        if empresa.medio_destino == 1:
            self._transporte_reserva_usuario = Autobus(self, destino, self._fechas_reserva_usuario[0], self._fechas_reserva_usuario[1])
            
        elif empresa.medio_destino == 2:
            self._transporte_reserva_usuario = Tren(self, destino, self._fechas_reserva_usuario[0], self._fechas_reserva_usuario[1])
            
        else:
            self._transporte_reserva_usuario = Avion(self, destino, self._fechas_reserva_usuario[0], self._fechas_reserva_usuario[1])
            
        
    def set_adultos_et_menores(self, transporte_electo, mayores, menores):
        
        return transporte_electo.set_adultos_et_menores(self, mayores, menores)
        
        
        
                
        
    
            
    