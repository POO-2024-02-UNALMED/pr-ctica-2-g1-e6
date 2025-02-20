from datetime import datetime
import os, sys
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from gestorAplicacion.transporte import Transporte
from src.gestorAplicacion.reservacionHotel.Destino import Destino

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.baseDatos.CargarObjetos import CargarObjetos

class Empresa:
    _empresas = []
    _datos_ya_cargados = False

    def __init__(self, nombre, prestige, rate, destinos_disponibles):
        self._nombre = nombre
        self._prestige = prestige  # Scale from 1-10
        self._rate = rate  # Base commission rate
        self._destinos_disponibles = destinos_disponibles
        
        
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
    def generador_de_datos():
        """Generate initial company data"""
        return [ #TODO: Agregar empresas
            Empresa("Avianza", (random.randint(12,20)/2), (random.randint(100,400)/20), Destino.get_destinos()),
            Empresa("LATA", (random.randint(12,20)/2), (random.randint(100,400)/20), Destino.get_destinos()),
            Empresa("Brasil Express", (random.randint(12,20)/2), (random.randint(100,400)/20), Destino.get_destinos()),
            Empresa("Cotrans", (random.randint(12,20)/2), (random.randint(100,400)/20), Destino.get_destinos())
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
    
    @classmethod    
    def listar_empresas_con_destino(cls, destino):
        
        #Retornar cada empresa en el listado de empresas SI el destino está en los destinos disponibles de la empresa
        return [empresa for empresa in cls._empresas if destino in empresa._destinos_disponibles]
    
    
    
              
                
        
    def set_ambas_fechas(self, transporte_electo, fecha_ir, fecha_volver=None):
        
        fecha_ir = datetime.strptime(fecha_ir, "%Y-%m-%d")
        
        if fecha_volver is not None:
            
            fecha_volver = datetime.strptime(fecha_volver, "%Y-%m-%d")
            
            transporte_electo.fechas(self, fecha_ir, fecha_volver)
          
            
        else:
            
            transporte_electo.fechas(self, fecha_ir)
        
        
        
                
        
    def set_adultos_et_menores(self, transporte_electo, mayores, menores):
        
        if mayores>0 and menores>=0: #Solo se verifica que las cantidades sean positivas
            return transporte_electo.set_adultos_et_menores(self, mayores, menores)
            
        else:
            return 2
            
    