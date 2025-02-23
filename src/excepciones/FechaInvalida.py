from .ExceptionC1 import ExceptionC1

class FechaInvalida(ExceptionC1):
    #Esta excepción ocurre cuando se introducen fechas inválidas
    #Esto puede ser cuando la fecha de llegada es antes de la fecha actual
    #O cuando la fecha de salida es después de la fecha de llegada
    
    def __init__(self, mensaje="Fecha inválida"):

        super().__init__("Fecha inválida: "+mensaje)