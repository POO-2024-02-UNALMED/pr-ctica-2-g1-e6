import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append("src/gestorAplicacion/talleres")

import gestorAplicacion.talleres
from gestorAplicacion.talleres.Gestion import Gestion
from gestorAplicacion.talleres.Lugar import Lugar
from gestorAplicacion.talleres.Ubicacion import Ubicacion
from gestorAplicacion.talleres.Itinerario import Itinerario
from baseDatos.CargarObjetos import CargarObjetos
from baseDatos.GuardarObjetos import GuardarObjetos


class uiTalleres:
    actividades = []
    refrigerios = []
    sitios = []
    a=0
    sum=0

    def grupo(self, Registro, Destinos, Manejo, Ruta):
        a = 0
        sum = 0
        for i in (0, self.nro):
            sum += Destinos.sitios[i]
            pass
        
        for sitio in Destinos.sitios:
            a += sitio

        preGrupo = (sum + a) / Destinos.nro

        print(preGrupo)

    def funcion1(self, documento, actividades, refrigerios, fecha, transporte, nro, sitios):
        a=0
        sum=0
        Registro = CargarObjetos.cargar_talleres()
        Destinos = Lugar(nro, 0, sitios)
        Manejo = Gestion(documento, 0, 0, 0, 0)
        Ruta = Itinerario(actividades, refrigerios, fecha, transporte)
        for i in (0, nro):
            a+=sitios[i]
            pass
        a = a/nro
        sum = Registro.lug1+Registro.lug2+Registro.lug3+Registro.lug4
        sum = sum / (Registro.lug1*4+1)
        sum = (sum + a)/2
        Lugar.Puntuacion = sum
        uiTalleres.grupo(self,Registro, Destinos, Manejo, Ruta)


    def talleres1():
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
        while True:
            transporte=input("Desea incluir transporte: 1.Sí  2.No")
            if transporte == 1 or transporte ==2:
                break
            else:
                print("Digite una opción valida 1 para agregar o 2 para no agregar")
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
        
        def talleres2():
            Destinos.puntuacion()
            if Destinos.puntaje > 3:
                Destinos.grupo = 1
                print("Fuiste agregado al grupo 1")
            else:
                Destinos.grupo = 2
                print("Fuiste agregado al grupo 2")
            x=0
            for i in range (0, nro):
                x = Destinos.Lugar[i] + Ruta.actividad[i]
            x+=Ruta.grupo + Destinos.nro
            z=0
            for refri in Ruta.refrigerios:
                z+= refri
            x+=z/Ruta.refrigerios.lenght
            Manejo.descuento = z
            return z


        
        
