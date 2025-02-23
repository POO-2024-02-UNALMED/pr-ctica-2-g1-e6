class ErrorAplicacion(Exception):
    
    def __init__(self, mensaje="Error Aplicación"):

        super().__init__("Manejo de errores de la aplicación: "+mensaje)