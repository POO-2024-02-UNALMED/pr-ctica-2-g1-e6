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
#|  +Última revisión: 2025-02-17-16-57, AlPerBara                                                                                   |
#|                                                                                                                                  |
#|  + Novedades:                                                                                                                    |
#|                                                                                                                                  |
#|      -Ahora solo falta agregar más destinos.                                                                                     |
#|                                                                                                                                  |
#|  + Pendientes en este módulo:                                                                                                    |
#|                                                                                                                                  |                                                                                      |
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
            #nro 0
            Destino("París", "Paris", "Francia", "Île-de-France", random.randint(0, 5), random.randint(0, 2), 4,[
                Hotel("Le Meurice", 21, 0, 15, random.randint(7, 10), random.randint(80, 180)),
                Hotel("Hotel Plaza Athénée", 18, 8, 3, random.randint(7, 10), random.randint(80, 180)),
                Hotel("The Peninsula Paris", 20, 9, 19, random.randint(7, 10), random.randint(80, 180))]),
            
            Destino("Roma", "Rome", "Italia", "Lazio", random.randint(0, 5), random.randint(0, 2), 4,[
                Hotel("Hotel Hassler", 18, 6, 15, random.randint(7, 10), random.randint(80, 180)),
                Hotel("Hotel de Russie", 18, 8, 26, random.randint(7, 10), random.randint(80, 180)),
                Hotel("The St. Regis Rome", 20, 18, 19, random.randint(7, 10), random.randint(80, 180))]),
            
            Destino("Nueva York", "new york", "Estados Unidos", "Nueva York", random.randint(0, 5), random.randint(0, 2), 4,[
                Hotel("The Plaza Hotel", 5, 13, 9, random.randint(7, 10), random.randint(100, 200)),
                Hotel("Mandarin Oriental New York", 21, 18, 22, random.randint(7, 10), random.randint(100, 200)),
                Hotel("The St. Regis New York", 9, 30, 20, random.randint(7, 10), random.randint(100, 200))]),
            
            Destino("Cartagena", "cartagena", "Colombia", "Bolivar", random.randint(0, 5), random.randint(0, 2), 3,[
                Hotel("Hotel Bocagrande", 6, 5, 24, random.randint(7, 10), random.randint(30, 100)),
                Hotel("Gyatt Residency Cartagena", 16, 22, 10, random.randint(7, 10), random.randint(30, 100)),
                Hotel("Hotel Cartagena Plaza", 24, 25, 6, random.randint(7, 10), random.randint(30, 100))]),
            
            Destino("Lima", "lima", "Peru", "Lima", random.randint(0, 5), random.randint(0, 2), 4,[
                Hotel("Hotel Lima San Isidro", 25, 20, 15, random.randint(7, 10), random.randint(30, 100)),
                Hotel("Inkari Suites Hotel", 22, 16, 12, random.randint(7, 10), random.randint(30, 100)),
                Hotel("Decapolis Miraflores", 20, 15, 10, random.randint(7, 10), random.randint(30, 100))]),
            
            # nro 5
            Destino("Bogotá", "bogota", "Colombia", "Cundinamarca", random.randint(0, 5), random.randint(0, 2), 3,[
                Hotel("Great Tower Bogotá", 25, 15, 10, random.randint(7, 10), random.randint(30, 100)),
                Hotel("Hotel Mayasa Bogotá", 20, 12, 8, random.randint(7, 10), random.randint(30, 100)),
                Hotel("Urbana Inn", 28, 20, 10, random.randint(7, 10), random.randint(30, 100))]),
            
            Destino("Buenos Aires", "buenos aires", "Argentina", "CABA", random.randint(0, 5), random.randint(0, 2), 4,[
                Hotel("All Seasons Buenos Aires", 20, 15, 10, random.randint(7, 10), random.randint(30, 100)),
                Hotel("Buenos Aires Parrott", 22, 16, 12, random.randint(7, 10), random.randint(30, 100)),
                Hotel("Milton Buenos Aires", 18, 14, 10, random.randint(7, 10), random.randint(30, 100))]),
            
            Destino("Cali", "cali", "Colombia", "Valle del Cauca", random.randint(0, 5), random.randint(0, 2), 3, [
                Hotel("Hotel Bisou Cali", 20, 15, 8, random.randint(7, 10), random.randint(30, 100)),
                Hotel("Hotel Belén", 25, 18, 12, random.randint(7, 10), random.randint(30, 100)),
                Hotel("Hotel Chipichape", 28, 20, 10, random.randint(7, 10), random.randint(30, 100))]),
            
            Destino("Santa Marta", "santa marta", "Colombia", "Magdalena", random.randint(0, 5), random.randint(0, 2), 3, [
                Hotel("Hotel El Rodadero", 20, 14, 10, random.randint(7, 10), random.randint(30, 100)),
                Hotel("Hotel Tayrona", 24, 16, 12, random.randint(7, 10), random.randint(30, 100)),
                Hotel("Garden Inn Santa Marta", 26, 18, 10, random.randint(7, 10), random.randint(30, 100))]),
            
            Destino("Río de Janeiro", "rio de janeiro", "Brasil", "Rio de Janeiro", random.randint(0, 5), random.randint(0, 2), 4, [
                Hotel("Hotel Copacabana", 25, 20, 15, random.randint(7, 10), random.randint(55, 135)),
                Hotel("Hotel Ipanema", 23, 18, 14, random.randint(7, 10), random.randint(60, 135)),
                Hotel("Hotel Leblon", 20, 15, 12, random.randint(7, 10), random.randint(55, 135))]),
            
            # nro 10
            Destino("Leticia", "leticia", "Colombia", "Amazonas", random.randint(0, 5), random.randint(0, 2), 4, [
                Hotel("Hotel Divino Niño", 15, 10, 5, random.randint(7, 10), random.randint(30, 100)),
                Hotel("Waldo's Hotel Boutique", 18, 12, 6, random.randint(7, 10), random.randint(30, 100))]),
            
            Destino("Santiago de Chile", "santiago", "Chile", "Metropolitana", random.randint(0, 5), random.randint(0, 2), 4, [
                Hotel("Hotel Leonardo Da Vinci", 22, 17, 12, random.randint(7, 10), random.randint(50, 120)),
                Hotel("DoubleTree Hotel Santiago", 24, 20, 14, random.randint(7, 10), random.randint(50, 120)),
                Hotel("The Singular Santiago", 18, 14, 10, random.randint(7, 10), random.randint(50, 120))]),
            
            Destino("Madrid", "madrid", "España", "Comunidad de Madrid", random.randint(0, 5), random.randint(0, 2), 4, [
                Hotel("Hotel Rizz Madrid", 30, 20, 15, random.randint(7, 10), random.randint(60, 160)),
                Hotel("\"Érase un hotel\"", 25, 18, 12, random.randint(7, 10), random.randint(55, 160)),
                Hotel("Hotel Claridge", 28, 22, 14, random.randint(7, 10), random.randint(55, 160))]),

            Destino("Barranquilla", "barranquilla", "Colombia", "Atlantico", random.randint(0, 5), random.randint(0, 2), 3, [
               Hotel("Hotel Sides Barranquilla", 20, 15, 10, random.randint(7, 10), random.randint(30, 100)),
               Hotel("GLS Grand Barranquilla", 22, 14, 12, random.randint(7, 10), random.randint(30, 100)),
               Hotel("Hotel Costa Mar", 25, 18, 10, random.randint(7, 10), random.randint(30, 100))]),
             
            Destino("San Andrés", "san andres", "Colombia", "San Andres", random.randint(0, 5), random.randint(0, 2), 4, [
                Hotel("Decaroline Isleño", 18, 14, 10, random.randint(7, 10), random.randint(60, 120)),
                Hotel("Hotel Calypse Beach", 20, 15, 10, random.randint(7, 10), random.randint(60, 120)),
                Hotel("Hotel Casablanca", 22, 18, 12, random.randint(7, 10), random.randint(50, 120))]),

            # nro 15
             Destino("Pereira", "pereira", "Colombia", "Risaralda", random.randint(0, 5), random.randint(0, 2), 2, [
                Hotel("Hotel Otún", 15, 10, 6, random.randint(7, 10), random.randint(30, 100)),
                Hotel("Hotel Movich Pereira", 18, 12, 8, random.randint(7, 10), random.randint(30, 100))]),
             
            Destino("Londres", "londres", "Reino Unido", "Inglaterra", random.randint(0, 5), random.randint(0, 2), 4, [
                Hotel("Sea Containers London", 30, 20, 15, random.randint(7, 10), random.randint(86, 187)),
                Hotel("Marlin Waterloo", 25, 18, 12, random.randint(7, 10), random.randint(96, 190)),
                Hotel("The Grange Pub", 28, 22, 14, random.randint(7, 10), random.randint(100, 185))]),

             Destino("Tokio", "tokyo", "Japón", "Kanto", random.randint(0, 5), random.randint(0, 2), 4, [
                Hotel("Lucky Hotel", 30, 25, 20, random.randint(7, 10), random.randint(96, 178)),
                Hotel("GIVE Araiyakushi", 28, 22, 18, random.randint(7, 10), random.randint(103, 201)),
                Hotel("The Shinjuku Resort", 26, 20, 15, random.randint(7, 10), random.randint(90, 185))]),
             
            Destino("Sídney", "sidney", "Australia", "Nueva Gales del Sur", random.randint(0, 5), random.randint(0, 2), 4, [
                Hotel("Park Gyatt Sydney", 28, 22, 16, random.randint(4, 10), random.randint(30, 100)),
                Hotel("Rockdale Grand Hotel", 30, 25, 18, random.randint(4, 10), random.randint(30, 100)),
                Hotel("Merlin Suites Sydney", 25, 20, 15, random.randint(4, 10), random.randint(30, 100))]),
            
            Destino("Dubái", "dubai", "Emiratos Arabes Unidos", "Dubai", random.randint(0, 5), random.randint(0, 2), 4, [
                Hotel("Al Habtoor Palace", 25, 20, 18, random.randint(9, 10), random.randint(348, 462)),
                Hotel("Palace Downtown", 30, 25, 20, 10, random.randint(360, 450)),
                Hotel("Mazaya Centre LEVA Hotel", 28, 22, 16, random.randint(8, 10), random.randint(300, 486))])
        ]
