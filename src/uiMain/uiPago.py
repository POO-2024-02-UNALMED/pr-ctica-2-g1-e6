import sys, os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.gestorAplicacion.pago import Pago, Notificacion#, MetodoPago
from src.gestorAplicacion.pago.factura import MetodoPago
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askfloat, askinteger

class uiPago:
    procesador = Pago()
    notificador = Notificacion()

    @staticmethod
    def go():
        # Se crea una ventana oculta para usar los diálogos de Tkinter
        root = tk.Tk()
        root.withdraw()

        messagebox.showinfo("Proceso de Pago", "=== PROCESO DE PAGO ===")

        # Paso 1: Solicitar monto
        monto = uiPago.solicitarMonto()
        if monto < 0:
            root.destroy()
            return  # Operación cancelada o monto inválido

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
            uiPago.notificador.enviarError("Operación cancelada.")
            return -1
        if monto < Pago.CARGO_MINIMO:
            uiPago.notificador.enviarError("Monto mínimo requerido: ${:.2f}".format(Pago.CARGO_MINIMO))
            return -1
        return monto

    @staticmethod
    def seleccionarMetodo():
        # Construir el mensaje con las opciones disponibles
        metodos = list(MetodoPago)
        mensaje = "Seleccione el método de pago:\n"
        for i, metodo in enumerate(metodos):
            # Se utiliza la propiedad get_descripcion definida en el Enum
            mensaje += "{}. {}\n".format(i+1, metodo.get_descripcion)
        
        opcion = askinteger("Seleccionar Método", mensaje)
        if opcion is None:
            uiPago.notificador.enviarError("Operación cancelada.")
            return None
        if opcion < 1 or opcion > len(metodos):
            uiPago.notificador.enviarError("Opción inválida")
            return None
        return metodos[opcion-1]

    @staticmethod
    def procesar_pago(monto, metodo):
        try:
            # Se utiliza el método procesar_pago (con guión bajo) de Pago
            factura = uiPago.procesador.procesar_pago(monto, metodo)
            uiPago.notificador.enviar(factura)
            
            messagebox.showinfo("Pago Exitoso",
                                f"Pago realizado correctamente.\nFactura ID: {factura.id}\nMonto: ${factura.monto:.2f}")
            print(factura.generar())  # También se imprime en consola para registro

        except ValueError as e:
            uiPago.notificador.enviarError(str(e))
            messagebox.showerror("Error", str(e))
