#|==================================================================================================================================|
#|                                                                                                                                  |
#|  Copyright (c) 2025 Agencia de Viajes Mundo Aventura S.A.                                                                        |
#|                                                                                                                                  |
#|                                                                                                                                  |
#|  +Nombre del módulo:                                                                                                             |
#|                                                                                                                                  |
#|      Principal.py                                                                                                                |
#|                                                                                                                                  |
#|  +Resumen:                                                                                                                       |
#|                                                                                                                                  |
#|      En este módulo está programada la pestaña principal del programa,                                                           |
#|               desde la cual se pueden acceder a las 5 (cinco) funcionalidades.                                                   |
#|                                                                                                                                  |
#|  +Codificado por:                                                                                                                |
#|                                                                                                                                  |
#|      - Alejandro Pérez Barrera (2025-02-08) (Creador)                                                                            |
#|                                                                                                                                  |
#|  +Última revisión: 2025-02-08-16-47, AlPerBara                                                                                   |
#|                                                                                                                                  |
#|  +Novedades:                                                                                                                     |
#|                                                                                                                                  |
#|      Este espacio está disponible para reportar novedades que se encuentren en este módulo...                                    |
#|                                                                                                                                  |
#|==================================================================================================================================|

import tkinter as tk

#Este método es solo para poder empezar la ejecución de esta clase desde aquí sin recibir el error TypeError: 'module' object is not callable
def aterrizar():
    root = tk.Tk()
    Principal(root)
    root.mainloop()


class Principal:
    print("prograam")