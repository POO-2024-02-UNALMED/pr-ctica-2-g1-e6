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
    suma=0


    def funcion3(self, aprox, poliza):
        pass


    def funcion2(self, carro):
        a = sum(self.Destinos.sitios)
        d = sum(self.Ruta.refrigerios)/((len(self.Ruta.refrigerios))+1)
        c = a+self.Ruta.grupo+d
        return c

    def grupo(self, Registro, Destinos, Manejo, Ruta):
        a = 0
        suma = 0
        suma = sum(self.Destinos.sitios)
        
        a = sum(self.Destinos.sitios)

        preGrupo = (suma + a) / self.Destinos.nro

        if preGrupo > 6 and self.Registro.grupo1 < 15:
            self.Ruta.grupo=1
        else:
            self.Ruta.grupo=2

    def funcion1(self, documento, actividades, refrigerios, fecha, transporte, nro, sitios):
        a=0
        suma=0
        #Registro = Itinerario([], [], 3, 4, [], 2, 3, 4, 5)
        #GuardarObjetos.guardar_registro(Registro)
        self.Registro = CargarObjetos.cargar_talleres()
        self.Destinos = Lugar(nro, 0, sitios)
        self.Manejo = Gestion(documento, 0, 0, 0, 0)
        self.Ruta = Itinerario(actividades, refrigerios, fecha, 0, transporte)
        a = sum(self.Destinos.sitios)

        a = a/nro
        suma = self.Registro.lug1+self.Registro.lug2+self.Registro.lug3+self.Registro.lug4
        suma = suma / (self.Registro.lug1*4+1)
        suma = (suma + a)/2
        Lugar.Puntuacion = suma
        uiTalleres.grupo(self, self.Registro, self.Destinos, self.Manejo, self.Ruta)

        return self.Ruta.grupo

        #for i in range (0, nro):
          #      x = Destinos.Lugar[i] + Ruta.actividad[i]
          #  x+=Ruta.grupo + Destinos.nro
           # z=0
          #  for refri in Ruta.refrigerios:
           #     z+= refri
          #  x+=z/Ruta.refrigerios.lenght
         #   Manejo.descuento = z
          # return z


        
        
