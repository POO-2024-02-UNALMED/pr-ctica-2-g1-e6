from .ErrorAplicacion import ErrorAplicacion

class ExceptionC1(ErrorAplicacion):
    
    def __init__(self, mensaje="Error reservación"):

        super().__init__("Error de reservación: "+mensaje)