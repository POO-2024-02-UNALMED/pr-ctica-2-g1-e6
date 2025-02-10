import gestorAplicacion 

class uiEventos:
    def Evento1():
        name = input("Cuál es el nombre del evento que desea programar?")
        fecha = input("Digite la fecha del evento a reservar")
        tipo = input("Qué tipo de evento desea reservar?")
    def Evento2():
        while True:
            num = int(input("Cuántas personas van a asistir al evento?"))
            if num > 0:
                break
            else:
                print("Digite un número valido")

