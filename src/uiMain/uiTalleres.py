import sys

sys.path.append("src/gestorAplicacion")

import gestorAplicacion 

class uiTalleres:
    actividades = []
    refrigerios = []
    sitios = []
    def talleres():
        while True:
            documento=int(input("Digite número de documento: "))
            if documento > 9999999999:
                print("Digite un número de documento con 10 cifras  o menos")
            else: 
                break
        while True:
            nro = int(input("Digite cuántos dias va a hacer actividades y talleres: "))
            if nro > 7 or nro < 1:
                print("El máximo de días es de 7, y el minimo de 1")
            else: break
        
        for i in range (0, nro):
            while True:
                act = int(input("Qué actividad deseas realizar el dia" + str(i) + "?: 1.Plantaton  2.Avevisor  3.casaCultura  4. casaMusica  5.TurcoParque  6.Tejedores o 7.Toboganes: "))
                sitio = int(input("En qué sitio deseas realizar la actividad: 1.Parque Berrio 2.San Antonio 3. San Ignacio o 4.Prado: "))
                refrigerio = int(input("Qué refrigerio deseas para el dia" + str(i) + "1.Sandwich  2. Hamburguesa  3. Pizza: "))
                if act > 0 and act < 8 and sitio > 0 and sitio < 5 and refrigerio > 0 and refrigerio < 4:
                    break
                else:
                    print("Debe seleccionar los números correspondientes a la opción deseada, no pude elegir opciones diferentes")
            uiTalleres.actividades.append(act)
            uiTalleres.sitios.append(sitio)
            uiTalleres.refrigerios.append(refrigerio)
        transporte=input("Desea incluir transporte: 1.Sí  2.No")
        if transporte == 1:
            transporte=int(input("Qué transporte desea: 1.Moto 2.Carro express 3.Carro 4.Bus turistico"))
        else:
            transporete = 0
        Destinos = gestorAplicacion.Lugar(nro, 0, uiTalleres.sitios)
        Manejo = gestorAplicacion.Gestion(documento, 0, 0, 0, 0)
        if transporte == 0:
            Ruta = gestorAplicacion.Itineario(uiTalleres.actividades, uiTalleres.refrigerios, 0, 0)
        else:
            Ruta = gestorAplicacion.Itineario(uiTalleres.actividades, uiTalleres.refrigerios, 0, 0, transporte)
        print(Ruta)

        
        
