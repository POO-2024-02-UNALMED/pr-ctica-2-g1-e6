#|==================================================================================================================================|
#|                                                                                                                                  |
#|  Copyright (c) 2025 Agencia de Viajes Mundo Aventura S.A.                                                                        |
#|                                                                                                                                  |
#|                                                                                                                                  |
#|  + Nombre del módulo:                                                                                                            |
#|                                                                                                                                  |
#|      Destino.py                                                                                                                  |
#|                                                                                                                                  |
#|  + Resumen:                                                                                                                      |
#|                                                                                                                                  |
#|      Este módulo contiene las funcionalidades que corresponden a los destinos:                                                   |
#|               Buscar un destino, confirmar una reserva y calcular su precio.                                                     |
#|                                                                                                                                  |
#|  + Codificado por:                                                                                                               |
#|                                                                                                                                  |
#|      - Alejandro Pérez Barrera (2025-02-09) (Creador)                                                                            |
#|                                                                                                                                  |
#|  +Última revisión: 2025-02-16-20-06, AlPerBara                                                                                   |
#|                                                                                                                                  |
#|  + Novedades:                                                                                                                    |
#|                                                                                                                                  |
#|      -Ahora solo falta agregar más destinos.                                                                                     |
#|                                                                                                                                  |
#|  + Pendientes en este módulo:                                                                                                    |
#|                                                                                                                                  |
#|      - Añadir Hoteles y Destinos restantes.                                                                                      |
#|      - Añadir comentarios.                                                                                                       |
#|                                                                                                                                  |
#|==================================================================================================================================|


import random
import sys, os.path
from .Hotel import Hotel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.baseDatos.GuardarObjetos import GuardarObjetos
from src.baseDatos.CargarObjetos import CargarObjetos


class Destino:

    _listadoDestinos =[] #En este array se guardan los destinos, el nombre es así desde la versión de Java
    _datos_ya_cargados = False #Cuando se crea destino se asume que no hay destinos en el array listadoDestinos

    #El constructor toma el nombre del destino, su nombre alterno, el pais, la region, la fama, temporada, como llegar y hoteles del destino
    def __init__(self, nombre, nombre_alterno, pais, region, fama, temporada, llegar, hoteles_destino):
        self._nombre = nombre
        self._nombre_alterno = nombre_alterno
        self._region = region
        self._pais = pais
        self._fama = fama
        self._temporada = temporada
        self._llegar = llegar
        self._hoteles_destino = hoteles_destino

    #========== GETTERS Y SETTERS ==========
    @classmethod
    def get_destinos(cls):
        if cls._datos_ya_cargados:
            return cls._listadoDestinos
        
        else:
            destinos = CargarObjetos.cargar_destinos()
            
            if destinos == []:
                cls.set_listado_destinos(cls.generador_de_datos())
                cls._datos_ya_cargados=True
                return cls._listadoDestinos
            else:
                cls.set_listado_destinos(destinos)
                cls._datos_ya_cargados=True
                return cls._listadoDestinos
    
    @classmethod
    def set_listado_destinos(cls, destinos):
        cls._listadoDestinos=destinos

    #========== GETTERS Y SETTERS ABURRIDOS ==========
    
    #Los setters y getters están definidos "The Pythonic Way"
    #Property es un decorador para indicar que el método es un getter
    @property
    def nombre(self):
        return self._nombre
    
    #<nombre_atributo>.setter es un decorador para indicar que el método es un setter
    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre



    @property
    def nombre_alterno(self):
        return self._nombre_alterno
    
    @nombre_alterno.setter
    def nombre_alterno(self, nombre_alterno):
        self._nombre_alterno = nombre_alterno



    @property
    def region(self):
        return self._region
    
    @region.setter
    def region(self, region):
        self._region = region



    @property
    def pais(self):
        return self._pais
    
    @pais.setter
    def pais(self, pais):
        self._pais = pais


    
    @property
    def fama(self):
        return self._fama
    
    @fama.setter
    def fama(self, fama):
        self._fama = fama



    @property
    def llegar(self):
        return self._llegar
    
    @llegar.setter
    def llegar(self, llegar):
        self._llegar = llegar



    @property
    def temporada(self):
        return self._temporada
    
    @temporada.setter
    def temporada(self, temporada):
        self._temporada = temporada



    @property
    def hoteles_destino(self):
        return self._hoteles_destino
    
    @hoteles_destino.setter
    def hoteles_destino(self, hoteles):
        self._hoteles_destino = hoteles

    #========== TERMINAN SETTERS Y GETTERS ==========

    @staticmethod
    def buscar_destino(palabra_clave):
        retorno =[]

        for destino in Destino.get_destinos():
            if palabra_clave.lower() in [destino.nombre.lower(), destino.nombre_alterno.lower(), destino.region.lower(), destino.pais.lower()]:
                retorno.append(destino)

        return retorno
    
    def reserva_hecha(self, hotel_reservado, lujo_reserva, delta_demanda):
        #from .Reserva import Reserva
        hotel_prestigio = hotel_reservado.prestigio

        if delta_demanda>0.35 and hotel_prestigio>8.65:
            self._fama=min(self._fama+((delta_demanda*hotel_prestigio)/20),5.0)

        if (lujo_reserva>=2 or delta_demanda>0.45) and self._temporada<2:
            self._temporada+=1
            
        return True

    
    @classmethod
    def generador_de_datos(cls):
        return [
            Destino("París", "Paris", "Francia", "Île-de-France", random.randint(0, 5), random.randint(0, 2), 4,[
                Hotel("Le Meurice", 21, 0, 15, random.randint(7, 10), random.randint(80, 180)),
                Hotel("Hotel Plaza Athénée", 18, 8, 3, random.randint(7, 10), random.randint(80, 180)),
                Hotel("The Peninsula Paris", 20, 9, 19, random.randint(7, 10), random.randint(80, 180))]),
            #Destino("París", "Paris", "Francia", "Île-de-France", random.randint(0, 5), random.randint(0, 2), 4,[])
        ]
