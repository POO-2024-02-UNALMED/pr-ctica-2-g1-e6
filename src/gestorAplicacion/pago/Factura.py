from datetime import datetime
from enum import Enum
from dataclasses import dataclass

class EstadoPago(Enum):
    COMPLETADO = "COMPLETADO"
    PENDIENTE = "PENDIENTE"
    CANCELADO = "CANCELADO"

class MetodoPago(Enum):
    EFECTIVO = ("EFECTIVO", "Pago en Efectivo")
    TARJETA = ("TARJETA", "Pago con Tarjeta")
    TRANSFERENCIA = ("TRANSFERENCIA", "Transferencia Bancaria")

    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion

    def get_descripcion(self):
        return self.descripcion

@dataclass
class Factura:
    monto: float
    metodo: MetodoPago
    id: str
    fecha_emision: datetime
    estado: EstadoPago = EstadoPago.COMPLETADO
    FORMATO_FECHA = "%d/%m/%Y %H:%M:%S"

    def generar(self) -> str:
        return f"""=============================
FACTURA DE PAGO
=============================
ID Transacción: {self.id}
Fecha: {self.fecha_emision.strftime(self.FORMATO_FECHA)}
Método de Pago: {self.metodo.get_descripcion()}
Estado: {self.estado.value}
-----------------------------
Total: ${self.monto:.2f}
============================="""

    def __str__(self) -> str:
        return f"Factura[id={self.id}, monto={self.monto:.2f}, método={self.metodo.get_descripcion()}]"


if __name__ == "__main__":
    factura = Factura(
        monto=150.50,
        metodo=MetodoPago.TARJETA,
        id="INV-001",
        fecha_emision=datetime.now()
    )
    
    print(factura.generar())
    
    print(factura)
