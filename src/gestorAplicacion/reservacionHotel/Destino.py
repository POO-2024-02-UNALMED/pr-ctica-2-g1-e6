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
#|  +Última revisión: 2025-02-09-16-53, AlPerBara                                                                                   |
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
import Hotel


class Destino:

    _listadoDestinos =[]
    _datos_ya_cargados = False

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

    #========== GETTERS Y SETTERS ABURRIDOS==========
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre=nombre



    def get_nombre_alterno(self):
        return self._nombre_alterno
    
    def set_nombre_alterno(self, nombre_alterno):
        self._nombre_alterno = nombre_alterno



    def get_region(self):
        return self._region
    
    def set_region(self, region):
        self._region=region



    def get_pais(self):
        return self._pais
    
    def set_pais(self, pais):
        self._pais=pais


    
    def get_fama(self):
        return self._fama
    
    def set_fama(self, fama):
        self._fama=fama



    def get_llegar(self):
        return self._llegar
    
    def set_llegar(self, llegar):
        self._llegar=llegar



    def get_temporada(self):
        return self._temporada
    
    def set_temporada(self, temporada):
        self._temporada=temporada



    def get_hoteles_destino(self):
        return self._hoteles_destino
    
    def set_hoteles_destino(self, hoteles):
        self._hoteles_destino = hoteles

    #========== TERMINAN SETTERS Y GETTERS

    def buscar_destino(palabra_clave):
        retorno =[]

        for destino in Destino.get_destinos():
            if palabra_clave.lower() in [destino.get_nombre(), destino.get_nombre_alterno().lower(), destino.get_region().lower(), destino.get_pais().lower()]:
                retorno.append(destino)

        return retorno
    
    def reserva_hecha(self, hotel_reservado, lujo_reserva, delta_demanda):
        hotel_prestigio = hotel_reservado.get_prestigio()

        if delta_demanda>0.35 and hotel_prestigio>8.65:
            self._fama=min(self._fama+((delta_demanda*hotel_prestigio)/20),5.0)

        if (lujo_reserva>=2 or delta_demanda>0.45) and self._temporada<2:
            self._temporada+=1

    
    @classmethod
    def generador_de_datos(cls):
        return [
            Destino("París", "Paris", "Francia", "Île-de-France", random.randint(0, 5), random.randint(0, 2), 4,[]),
            Destino("París", "Paris", "Francia", "Île-de-France", random.randint(0, 5), random.randint(0, 2), 4,[])
        ]


if __name__ == "__main__": #TODO:remover esto
    data =Destino.get_destinos()
    print(data[0].get_fama())