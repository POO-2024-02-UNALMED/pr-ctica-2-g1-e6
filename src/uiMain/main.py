#|==================================================================================================================================|
#|                                                                                                                                  |
#|  Copyright (c) 2025 Agencia de Viajes Mundo Aventura S.A.                                                                        |
#|                                                                                                                                  |
#|                                                                                                                                  |
#|  + Nombre del módulo:                                                                                                            |
#|                                                                                                                                  |
#|      main.py                                                                                                                     |
#|                                                                                                                                  |
#|  + Resumen:                                                                                                                      |
#|                                                                                                                                  |
#|      Desde este módulo se va a empezar a ejecutar el programa, lo único que hace es redirigir a                                  |
#|               Home.aterrizar(), donde se crea la ventana de inicio para la interfaz gráfica.                                     |
#|                                                                                                                                  |
#|  + Codificado por:                                                                                                               |
#|                                                                                                                                  |
#|      - Alejandro Pérez Barrera (2025-02-08) (Creador).                                                                           |
#|                                                                                                                                  |
#|  +Última revisión: 2025-02-09-15-55, AlPerBara                                                                                   |
#|                                                                                                                                  |
#|  + Novedades:                                                                                                                    |
#|                                                                                                                                  |
#|      Este espacio está disponible para reportar novedades que se encuentren en este módulo...                                    |
#|                                                                                                                                  |
#|  + Pendientes en este módulo:                                                                                                    |
#|                                                                                                                                  |
#|      -Quitar print que dice "Cerar". (Solo está ahí para indicar el final de la ejecución del programa).                         |
#|                                                                                                                                  |
#|==================================================================================================================================|

import Home #Home se utiliza para poder comenzar la ejecución del programa desde la pestaña de inicio.

if __name__ == "__main__":
    Home.aterrizar() #Home. aterrizar es el método para entrar a la clase de la pestaña de inicio
    print("Cerar") #TODO: Quitar esto