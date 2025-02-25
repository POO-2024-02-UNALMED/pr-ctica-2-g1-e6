from datetime import datetime
from typing import List
import uuid
from factura import Factura, MetodoPago, EstadoPago

class Pago:
    CARGO_MINIMO = 1000.0

    def __init__(self):
        self.historial_facturas: List[Factura] = []

    def procesar_pago(self, monto: float, metodo: MetodoPago = MetodoPago.TARJETA) -> Factura:
        """
        Process a payment with the given amount and payment method.
        If no method is specified, TARJETA (card) is used by default.
        """
        self.validar_monto(monto)
        factura = Factura(
            monto=monto,
            metodo=metodo,
            id=str(uuid.uuid4()),
            fecha_emision=datetime.now()
        )
        self.historial_facturas.append(factura)
        return factura

    def validar_monto(self, monto: float) -> None:
        """Validate that the payment amount meets the minimum requirement."""
        if monto < self.CARGO_MINIMO:
            raise ValueError(f"El monto mínimo de pago es ${self.CARGO_MINIMO:.2f}")

    def get_historial_facturas(self) -> List[Factura]:
        """Return a copy of the invoice history."""
        return self.historial_facturas.copy()

    def get_total_facturado(self) -> float:
        """Calculate the total amount invoiced."""
        return sum(factura.monto for factura in self.historial_facturas)


if __name__ == "__main__":
    pago = Pago()
    
    try:
      
        factura1 = pago.procesar_pago(1500.0)
        print("Factura 1:", factura1)
      
        factura2 = pago.procesar_pago(2000.0, MetodoPago.TRANSFERENCIA)
        print("Factura 2:", factura2)
        
        factura3 = pago.procesar_pago(500.0)  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")
    
    print(f"\nTotal facturado: ${pago.get_total_facturado():.2f}")
    
    print("\nHistorial de facturas:")
    for factura in pago.get_historial_facturas():
        print(factura)
