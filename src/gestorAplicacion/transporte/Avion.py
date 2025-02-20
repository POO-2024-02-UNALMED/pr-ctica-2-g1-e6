from .Transporte import Transporte


class Avion(Transporte):
    def calcular_precio(self):
        precio_base = 200  # Example base price
        factor_empresa = self.empresa.get_factor()
        factor_destino = self.destino.get_factor()
        factor_asiento = 1.0 if self.tipo_asiento == 'Turista' else 2.0
        descuento_ida_vuelta = 0.85 if self.ida_vuelta else 1.0
        return precio_base * factor_empresa * factor_destino * factor_asiento * descuento_ida_vuelta