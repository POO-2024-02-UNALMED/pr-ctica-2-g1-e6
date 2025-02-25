from datetime import datetime
from typing import List
from .factura import Factura

class Notificacion:
    def __init__(self):
        self.historial_notificaciones: List[str] = []
    
    def enviar(self, mensaje_o_factura):
        if isinstance(mensaje_o_factura, str):
            notificacion = f"[{datetime.now()}] {mensaje_o_factura}"
            self.historial_notificaciones.append(notificacion)
            print(f"NOTIFICACIÓN: {notificacion}")
        elif isinstance(mensaje_o_factura, Factura):
            factura = mensaje_o_factura
            mensaje = f"""Pago procesado exitosamente
ID: {factura.id}
Método: {factura.metodo.get_descripcion()}
Monto: ${factura.monto:.2f}"""
            self.enviar(mensaje)
    
    def enviar_error(self, error: str):
        self.enviar(f"ERROR: {error}")
    
    def get_historial_notificaciones(self) -> List[str]:
        return self.historial_notificaciones.copy()


if __name__ == "__main__":
    notificacion = Notificacion()
    notificacion.enviar("Test message")
    notificacion.enviar_error("Something went wrong")
    print("\nHistorial de notificaciones:")
    for notif in notificacion.get_historial_notificaciones():
        print(notif)
