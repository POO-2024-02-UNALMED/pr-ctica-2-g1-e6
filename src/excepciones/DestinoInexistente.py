from .ExceptionC1 import ExceptionC1

class DestinoInexistente(ExceptionC1):
    #Esta excepción ocurre cuando se introduce un destino que no existe
    
    def __init__(self, mensaje="Destino Inexistente"):

        super().__init__("Error Destino inexistente : "+mensaje)