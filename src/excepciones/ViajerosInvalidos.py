from .ExceptionC1 import ExceptionC1

class ViajerosInvalidos(ExceptionC1):
    #Esta excepción ocurre cuando se introduce un número de viajeros inválido
    
    def __init__(self, mensaje="Viajeros inválidos"):

        super().__init__("Viajeros Inválidos : "+mensaje)