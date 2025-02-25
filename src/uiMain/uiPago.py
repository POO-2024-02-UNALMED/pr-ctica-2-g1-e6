from gestorAplicacion.pago import Pago, Notificacion

class uiPago:
    procesador = Pago()
    notificador = Notificacion()

    @staticmethod
    def go():
        print("\n=== PROCESO DE PAGO ===")
        
        # Paso 1: Solicitar monto
        monto = uiPago.solicitarMonto()
        if monto < 0:
            return  # Si hubo error, salir
        
        # Paso 2: Seleccionar método de pago
        metodo = uiPago.seleccionarMetodo()
        if metodo is None:
            return
        
        # Paso 3: Procesar pago
        uiPago.procesarPago(monto, metodo)

    @staticmethod
    def solicitarMonto():
        while True:
            try:
                monto = float(input("\nIngrese el monto a pagar: $"))
                if monto < Pago.CARGO_MINIMO:
                    uiPago.notificador.enviarError("Monto mínimo requerido: ${:.2f}".format(Pago.CARGO_MINIMO))
                    return -1
                return monto
            except ValueError:
                uiPago.notificador.enviarError("Debe ingresar un valor numérico válido.")

    @staticmethod
    def seleccionarMetodo():
        print("\nSeleccione el método de pago:")
        metodos = list(Pago.MetodoPago)
        
        for i, metodo in enumerate(metodos):
            print("{}. {}".format(i+1, metodo.getDescripcion()))
        
        try:
            opcion = int(input("\nOpción: "))
            if opcion < 1 or opcion > len(metodos):
                uiPago.notificador.enviarError("Opción inválida")
                return None
            return metodos[opcion-1]
        except ValueError:
            uiPago.notificador.enviarError("Debe ingresar un número")
            return None

    @staticmethod
    def procesarPago(monto, metodo):
        try:
            factura = uiPago.procesador.procesarPago(monto, metodo)
            uiPago.notificador.enviar(factura)
            
            print("\nPago exitoso!\n")
            print(factura.generar())
            
        except ValueError as e:  # Se usa ValueError en lugar de IllegalArgumentException
            uiPago.notificador.enviarError(str(e))
        
        input("\nPresione Enter para continuar...")
