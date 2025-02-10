#|==================================================================================================================================|
#|                                                                                                                                  |
#|  Copyright (c) 2025 Agencia de Viajes Mundo Aventura S.A.                                                                        |
#|                                                                                                                                  |
#|                                                                                                                                  |
#|  + Nombre del módulo:                                                                                                            |
#|                                                                                                                                  |
#|      Hotel.py                                                                                                                    |
#|                                                                                                                                  |
#|  + Resumen:                                                                                                                      |
#|                                                                                                                                  |
#|      Este módulo contiene las funcionalidades que corresponden a los Hoteles:                                                    |
#|               Calcular su demanda, calcular sus precios esperados y por noche,                                                   |
#|               listar sus precios y confirmar una reserva.                                                                        |
#|                                                                                                                                  |
#|  + Codificado por:                                                                                                               |
#|                                                                                                                                  |
#|      - Alejandro Pérez Barrera (2025-02-09) (Creador)                                                                            |
#|                                                                                                                                  |
#|  +Última revisión: 2025-02-09-17-10, AlPerBara                                                                                   |
#|                                                                                                                                  |
#|  + Novedades:                                                                                                                    |
#|                                                                                                                                  |
#|      -Este módulo aún no está terminado, no ha sido probado y puede contener errores.                                            |
#|                                                                                                                                  |
#|  + Pendientes en este módulo:                                                                                                    |
#|                                                                                                                                  |
#|      - Getters, setters.                                                                                                         |
#|      - Métodos.                                                                                                                  |
#|      - Depurar                                                                                                                   |
#|                                                                                                                                  |
#|==================================================================================================================================|

class Hotel:
    _SESGO=600 #El sesgo permite ajustar los precios de manera directa, el valor 600 es para utilizar pesos colombianos como moneda, pero puede ser cualquier valor
    
    #========== CONSTRUCTOR ==========
    def __init__(self, nombre, cuartos_simples, cuartos_intermedios, cuartos_lujosos, prestigio, recargo):
        self._nombre = nombre
        self._cuartos_simples = cuartos_simples
        self._cuartos_intermedios = cuartos_intermedios
        self._cuartos_lujosos = cuartos_lujosos
        self._prestigio = prestigio
        self._recargo = recargo
        
        self._demanda=self.calcular_demanda(self._cuartos_simples, self._cuartos_intermedios, self._cuartos_lujosos, self._prestigio)
        
    #========== GETTERS Y SETTERS ==========
    
    #
    
    #========== MÉTODOS ==========
    #Un método estático no se mete con la clase, a diferencia de un método de clase
    @staticmethod
    def calcular_demanda(cuartos_simples, cuartos_intermedios, cuartos_lujosos, prestigio):
        #Aquí lo primero es limitar el número de cuartos de hotel al intérvalo [1,30]
        #Si no se limitan existe el riesgo de que ocurra el error "ZeroDivisionError",
        #   ese error ocurre al intentar dividir entre cero
        if cuartos_simples<1:
            cuartos_simples=1

        elif cuartos_simples>30:
            cuartos_simples=30
            
        
        if cuartos_intermedios<1:
            cuartos_intermedios=1

        elif cuartos_intermedios>30:
            cuartos_intermedios=30
            
        
        if cuartos_lujosos<1:
            cuartos_lujosos=1

        elif cuartos_lujosos>30:
            cuartos_lujosos=30
            
        #Aquí se calcula la demanda como tal,
        #l   a fórmula tiene en cuenta la cantidad de cuartos disponibles y el prestigio,
        #   pero es muy complicada como para explicarla
        demanda_calculada = (((1.2*cuartos_lujosos*prestigio)+(0.79*cuartos_intermedios*0.79*prestigio)+(0.05*cuartos_simples*prestigio))/(((0.93*cuartos_lujosos)*cuartos_simples*cuartos_intermedios)-1))+1.2
        
        #La demanda se confina al intervalo [0,10], si es muy grande o muy pequeña se resetea a 10, el máximo
        #El motivo por el cual se resetea a 10 y no a 0 es porque cuando la demanda es demasiado alta la fórmula
        #   puede llegar a dar valores negativos, así que los valores negativos se interpretan
        #   como una demanda tan alta, que "descompuso" la fórmula.
        if (demanda_calculada>10 or demanda_calculada<0):
            demanda_calculada=10
            
        return demanda_calculada
            
             