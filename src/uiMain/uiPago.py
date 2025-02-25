import sys
import os.path
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askfloat, askinteger

# Configuración de la ruta para imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.gestorAplicacion.pago import Pago, Notificacion
from src.gestorAplicacion.pago.factura import MetodoPago

class uiPago:
    procesador = Pago.Pago()  # Requiere que Pago tenga CARGO_MINIMO = 1000.0
    notificador = Notificacion.Notificacion()

    @staticmethod
    def go():
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Proceso de Pago", "=== PROCESO DE PAGO ===")

        # Paso 1: Solicitar monto
        monto = uiPago.solicitarMonto()
        if monto < 0:
            root.destroy()
            return

        # Paso 2: Seleccionar método de pago
        metodo = uiPago.seleccionarMetodo()
        if metodo is None:
            root.destroy()
            return

        # Paso 3: Procesar pago
        uiPago.procesar_pago(monto, metodo)
        root.destroy()

    @staticmethod
    def solicitarMonto():
        monto = askfloat("Realizar Pago", "Ingrese el monto a pagar:")
        if monto is None:
            uiPago.notificador.enviar_error("Operación cancelada.")  # ✅ snake_case
            return -1
        if monto < Pago.CARGO_MINIMO:  # CARGO_MINIMO = 1000.0 definido en Pago.py
            uiPago.notificador.enviar_error(f"Monto mínimo requerido: ${Pago.CARGO_MINIMO:.2f}")  # ✅
            return -1
        return monto

    @staticmethod
    def seleccionarMetodo():
        metodos = list(MetodoPago)
        mensaje = "Seleccione el método de pago:\n"
        for i, metodo in enumerate(metodos):
            mensaje += f"{i+1}. {metodo.get_descripcion}\n"  # Requiere get_descripcion en MetodoPago
        
        opcion = askinteger("Seleccionar Método", mensaje)
        if opcion is None:
            uiPago.notificador.enviar_error("Operación cancelada.")  # ✅
            return None
        if opcion < 1 or opcion > len(metodos):
            uiPago.notificador.enviar_error("Opción inválida")  # ✅
            return None
        return metodos[opcion-1]

    @staticmethod
    def procesar_pago(monto, metodo):
        try:
            factura = uiPago.procesador.procesar_pago(monto, metodo)  # Requiere método en Pago
            uiPago.notificador.enviar(factura)
            messagebox.showinfo(
                "Pago Exitoso", 
                f"Pago realizado correctamente.\nFactura ID: {factura.id}\nMonto: ${factura.monto:.2f}"
            )
            print(factura.generar())  # Requiere método generar() en Factura

        except ValueError as e:
            uiPago.notificador.enviar_error(str(e))  # ✅
            messagebox.showerror("Error", str(e))
