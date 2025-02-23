#|==================================================================================================================================|
#|                                                                                                                                  |
#|  Copyright (c) 2025 Agencia de Viajes Mundo Aventura S.A.                                                                        |
#|                                                                                                                                  |
#|                                                                                                                                  |
#|  + Nombre del módulo:                                                                                                            |
#|                                                                                                                                  |
#|      Hotel.py                                                                                                                    |
#|                                                                                                                                  |
#|  + Resumen:                                                                                                                      |
#|                                                                                                                                  |
#|      Este módulo contiene las funcionalidades que corresponden a la reserva de hotel:                                            |
#|               Definir y verificar fechas, número de viajeros, estadía y confirmar la reserva.                                    |
#|               Desde aquí se mueven interacciones importantes con la interfaz de usuario.                                         |
#|                                                                                                                                  |
#|  + Codificado por:                                                                                                               |
#|                                                                                                                                  |
#|      - Alejandro Pérez Barrera (2025-02-09) (Creador)                                                                            |
#|                                                                                                                                  |
#|  +Última revisión: 2025-02-17-16-56, AlPerBara                                                                                   |
#|                                                                                                                                  |
#|  + Novedades:                                                                                                                    |
#|                                                                                                                                  |
#|      -Este módulo aún no está terminado, no ha sido probado y puede contener errores.                                            |
#|                                                                                                                                  |
#|  + Pendientes en este módulo:                                                                                                    |
#|                                                                                                                                  |
#|      - Verificar errores.                                                                                                        |
#|      - Añadir comentarios.                                                                                                       |
#|                                                                                                                                  |
#|==================================================================================================================================|


from datetime import datetime
from .Destino import Destino
from .Hotel import Hotel

import os.path, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.excepciones.FechaInvalida import FechaInvalida
from src.excepciones.ViajerosInvalidos import ViajerosInvalidos


class Reserva:
    
    _id_destino = None
    
    _reserva_actual = None
    
    #========== CONSTRUCTOR ==========
    
    def __init__(self, destino):
        self._destino_viaje = destino
        self._hotel_viaje = None
        self._lujo_hotel_viaje = None
        self._precio_total = None
        self._viajeros_adultos = None
        self._viajeros_menores = None
        self._estadia = None
        self._fecha_llegar = None
        self._fecha_salir = None
        
    #========== GETTERS Y SETTERS ==========
    
    @classmethod
    def get_id_destino(cls):
        return cls._id_destino
    
    @classmethod
    def set_id_destino(cls, id):
        cls._id_destino = id
        
        
        
    @classmethod
    def get_reserva_actual(cls):
        return cls._reserva_actual
    
    @classmethod
    def set_reserva_actual(cls, reserva):
        cls._reserva_actual = reserva
        
        
        
    @property
    def destino_viaje(self):
        return self._destino_viaje
    
    @destino_viaje.setter
    def destino_viaje(self, dedstino):
        self._destino_viaje = dedstino
        
        
        
    @property
    def hotel_viaje(self):
        return self._hotel_viaje
    
    @hotel_viaje.setter
    def hotel_viaje(self, hotel):
        self._hotel_viaje = hotel
        
        
        
    @property
    def lujo_hotel_viaje(self):
        return self._lujo_hotel_viaje
    
    @lujo_hotel_viaje.setter
    def lujo_hotel_viaje(self, lujo):
        self._lujo_hotel_viaje = lujo
        
        
        
    @property
    def precio_total(self):
        return self._precio_total
    
    @precio_total.setter
    def precio_total(self, percio):
        self._precio_total = percio
        
    
    
    @property
    def viajeros_adultos(self):
        return self._viajeros_adultos
    
    @viajeros_adultos.setter
    def viajeros_adultos(self, vjaieros):
        self._viajeros_adultos = vjaieros
        
        
        
    @property
    def viajeros_menores(self):
        return self._viajeros_menores
    
    @viajeros_menores.setter
    def viajeros_menores(self, vjaeres):
        self._viajeros_menores = vjaeres
        
        
        
    @property
    def estadia(self):
        return self._estadia
    
    @estadia.setter
    def estadia(self, estraida):
        self._estadia = estraida
        
        
    
    @property
    def fecha_llegar(self):
        return self._fecha_llegar
    
    @fecha_llegar.setter
    def fecha_llegar(self, fecah):
        self._fecha_llegar = fecah
        
    
    
    @property
    def fecha_salir(self):
        return self._fecha_salir
    
    @fecha_salir.setter
    def fecha_salir(self, fecha):
        self._fecha_salir = fecha
        
    #========== MÉTODOS ==========
    
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
        
    def set_ambas_fechas(self, modificar, fecha_llegada, fecha_salida):
        fecha_hoy = datetime.today()
        fecha_llegada = datetime.strptime(fecha_llegada, "%Y-%m-%d")
        fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d")
        
        if (fecha_llegada <= fecha_hoy or fecha_salida <= fecha_hoy or fecha_salida <= fecha_llegada):
            if (fecha_llegada <=fecha_hoy):
                raise FechaInvalida(f"La fecha de llegada ({fecha_llegada.strftime("%d - %m - %Y")}) toma lugar antes de la fecha actual ({fecha_hoy.strftime("%d - %m - %Y")})")
            elif (fecha_salida <= fecha_hoy):
                raise FechaInvalida(f"La fecha de salida ({fecha_salida.strftime("%d - %m - %Y")}) toma lugar antes de la fecha actual ({fecha_hoy.strftime("%d - %m - %Y")})")
            else:
                raise FechaInvalida(f"La fecha de salida ({fecha_salida.strftime("%d - %m - %Y")}) toma lugar antes de la fecha de llegada ({fecha_llegada.strftime("%d - %m - %Y")})")
            
        else:
            self._fecha_llegar = fecha_llegada
            self._fecha_salir = fecha_salida
            
            self._estadia = (fecha_salida - fecha_llegada).days
            
            return True
                
        
    def set_adultos_et_menores(self, modificar, mayores, menores):
        
        if (mayores>0 and menores>=0 and ((mayores*2)>=menores)):
            self._viajeros_adultos = mayores
            self._viajeros_menores = menores
            
            if not modificar:
                return 1
                
        elif mayores>0 and menores>=0:
            return 2
            
        else:
            raise ViajerosInvalidos("El número de viajeros adultos y menores no es válido.")
            
    
    def calculo_estadia_total(self):
        self._precio_total = self._hotel_viaje.calcular_precio_total(self._lujo_hotel_viaje, self._estadia)
        return self._precio_total
    

    def confirmar_hotel(self):
        if self._hotel_viaje.cuarto_reservado(self._estadia, self._lujo_hotel_viaje, self._destino_viaje):
            
            self._reserva_actual = self
            return True
        
        else:
            return False