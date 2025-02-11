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
#|  +Última revisión: 2025-02-11-15-48, AlPerBara                                                                                   |
#|                                                                                                                                  |
#|  + Novedades:                                                                                                                    |
#|                                                                                                                                  |
#|      -Este módulo aún no está terminado, no ha sido probado y puede contener errores.                                            |
#|                                                                                                                                  |
#|  + Pendientes en este módulo:                                                                                                    |
#|                                                                                                                                  |
#|      - Todo XD.                                                                                                                  |
#|                                                                                                                                  |
#|==================================================================================================================================|


import random
from Hotel import Hotel


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
            cls.set_listado_destinos(cls.generador_de_datos()) #TODO: agregar metodo cargar_objetos
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

    def buscar_destino(palabra_clave):
        retorno =[]

        for destino in Destino.get_destinos():
            if palabra_clave.lower() in [destino.nombre(), destino.nombre_alterno().lower(), destino.region().lower(), destino.pais().lower()]:
                retorno.append(destino)

        return retorno
    
    def reserva_hecha(self, hotel_reservado, lujo_reserva, delta_demanda):
        hotel_prestigio = hotel_reservado.prestigio

        if delta_demanda>0.35 and hotel_prestigio>8.65:
            self._fama=min(self._fama+((delta_demanda*hotel_prestigio)/20),5.0)

        if (lujo_reserva>=2 or delta_demanda>0.45) and self._temporada<2:
            self._temporada+=1

    
    @classmethod
    def generador_de_datos(cls):
        return [
            Destino("París", "Paris", "Francia", "Île-de-France", random.randint(0, 5), random.randint(0, 2), 4,[
                Hotel("Le Meurice", 21, 0, 15, random.randint(7, 10), random.randint(80, 180))]),
            Destino("París", "Paris", "Francia", "Île-de-France", random.randint(0, 5), random.randint(0, 2), 4,[])
        ]


if __name__ == "__main__": #TODO:remover esto
    data =Destino.get_destinos()
    print(data[0].hoteles_destino[0].calcular_precio_esperado_noche(data[0].fama, data[0].temporada, 2, 1))
    print(data[0].hoteles_destino[0].calcular_precio_total(1, 3))
    print(data[0].hoteles_destino[0].demanda)
    print(data[0].hoteles_destino[0].listar_precios())
    print(data[0].hoteles_destino[0].cuartos_intermedios)
    print(data[0].hoteles_destino[0].cuarto_reservado(4, 1, data[0]))
    print(data[0].hoteles_destino[0].demanda)