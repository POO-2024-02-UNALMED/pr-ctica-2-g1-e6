class Ubicacion:
    lug1 = 2000
    lug2 = 2350
    lug3 = 2700
    lug4 = 3000
    def puntuacion(self, numero, numero1, numero2, numero3, numero4):
        x=0
        y=numero.length()
        for t in numero:
            x+=t
        suma = numero1+numero2+numero3+numero4
        suma = suma/4
        suma+=x
        suma=suma/5
        return suma



