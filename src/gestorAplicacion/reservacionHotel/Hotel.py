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
#|  +Última revisión: 2025-02-16-20-04, AlPerBara                                                                                   |
#|                                                                                                                                  |
#|  + Novedades:                                                                                                                    |
#|                                                                                                                                  |
#|      -Hace falta verificar que este módulo se comporte como es de esperarse.                                                     |
#|                                                                                                                                  |
#|  + Pendientes en este módulo:                                                                                                    |
#|                                                                                                                                  |
#|      - Añadir comentarios.                                                                                                       |
#|                                                                                                                                  |
#|==================================================================================================================================|

class Hotel:
    _SESGO=600 #El sesgo permite ajustar los precios de manera directa, el valor 600 es para utilizar pesos colombianos como moneda, pero puede ser cualquier valor
    
    
    #========== CONSTRUCTOR ==========
    
    
    def __init__(self, nombre, cuartos_simples, cuartos_intermedios, cuartos_lujosos, prestigio, recargo):
        self._nombre = nombre
        self._cuartos_simples = cuartos_simples #a
        self._cuartos_intermedios = cuartos_intermedios #b
        self._cuartos_lujosos = cuartos_lujosos #c
        self._prestigio = prestigio
        self._recargo = recargo
        
        #Se va al comando de calcular demanda
        self._demanda=self.calcular_demanda(self._cuartos_simples, self._cuartos_intermedios, self._cuartos_lujosos, self._prestigio)
        
        
    #========== GETTERS Y SETTERS ==========
    
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
        
        
    @property
    def cuartos_simples(self):
        return self._cuartos_simples
    
    @cuartos_simples.setter
    def cuartos_simples(self, cuartos_simples):
        self._cuartos_simples = cuartos_simples
        
        
    
    @property
    def cuartos_intermedios(self):
        return self._cuartos_intermedios
    
    @cuartos_intermedios.setter
    def cuartos_intermedios(self, cuartos_intermedios):
        self._cuartos_intermedios = cuartos_intermedios
        
        
    
    @property
    def cuartos_lujosos(self):
        return self._cuartos_lujosos
    
    @cuartos_lujosos.setter
    def cuartos_lujosos(self, cuartos_lujosos):
        self._cuartos_lujosos = cuartos_lujosos
        
        
    
    @property
    def prestigio(self):
        return self._prestigio
    
    @prestigio.setter
    def prestigio(self, prestigio):
        self. _prestigio = prestigio
        
        
        
    @property
    def demanda(self):
        return self._demanda
    
    @demanda.setter
    def demanda(self, demanda):
        self._demanda = demanda
        
        
    
    @property
    def recargo(self):
        return self._recargo
    
    @recargo.setter
    def recargo(self, recargo):
        self._recargo=recargo
    
    
    #========== MÉTODOS ==========
    
    
    #Un método estático no se mete con la clase, a diferencia de un método de clase
    @staticmethod
    #Calcular demanda ajusta la demanda con base al numero de cuartos por lujo y el prestigio del hotel. La demanda se usa para calcular el precio por noche
    #la demanda sube cuando hay menos cuartos, y cuando el hotel tiende a ser más bien prestigioso
    #calcular_demanda recibe el numero de cuartos en cada tipo de habitacion y el prestigio del hotel y retorna un float con la demanda del hotel, si la demanda del hotel se menor a 0 o mayor a 10, se limita  0 o a 10
    def calcular_demanda(cuartos_simples, cuartos_intermedios, cuartos_lujosos, prestigio, estadia=0):
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
        
        #Esta es una alternativa al método sobrecargado que había en Java, ahora ambos métodos se ejecutan desde aquí
        if estadia!=0:
            demanda_calculada+=((pow(estadia,2))/((pow(9,3.2))+78))
        
        #La demanda se confina al intervalo [0,10], si es muy grande o muy pequeña se resetea a 10, el máximo
        #El motivo por el cual se resetea a 10 y no a 0 es porque cuando la demanda es demasiado alta la fórmula
        #   puede llegar a dar valores negativos, así que los valores negativos se interpretan
        #   como una demanda tan alta, que "descompuso" la fórmula.
        if (demanda_calculada>10 or demanda_calculada<0):
            demanda_calculada=10
            
        return demanda_calculada
    
    #Este método retorna un cálculo grosso del precio por noche del hotel, ese valor incrementa o se reduce dependiendo del cuarto elegido
    def calcular_precio_esperado_noche(self, fama_destino, temporada_destino, adultos_reserva, menores_reserva):
        
        #Esta variable es la suma entre adultos y niños, donde los niños tienen más peso (Cambian más el valor)
       viajeros = 1+((adultos_reserva+(1.2*menores_reserva))/(adultos_reserva+menores_reserva+5))
       #Los niños hacen que el precio suba más (multiplicar por 1.2), y abajo se suma 5, para hacer que a los grupos más grandes les sea más económico viajar
       
       #Dependiendo de la temporada, se va a multiplicar un recargo distinto (0.85, 1, 1.3)
       if temporada_destino == 0: #Esta fórmula como tal determina el precio con el recargo del hotel, la fama del destino, prestigio y demanda del hotel, viajeros y el sesgo
           self._prec_esp_noc = (self._recargo*(1+(fama_destino/10))*0.85*(1+(self._prestigio/20)*self._demanda*viajeros*self._SESGO))
           return self._prec_esp_noc
       
       elif temporada_destino == 1:
           self._prec_esp_noc = (self._recargo*(1+(fama_destino/10))*1*(1+(self._prestigio/20)*self._demanda*viajeros*self._SESGO))
           return self._prec_esp_noc
       
       elif temporada_destino == 2:
           self._prec_esp_noc = (self._recargo*(1+(fama_destino/10))*1.3*(1+(self._prestigio/20)*self._demanda*viajeros*self._SESGO))
           return self._prec_esp_noc
       
       else: #Si ocurre algún inesperado, este precio se asigna como default, para que no se caiga el programa
           self._prec_esp_noc = 853694.68
           return self._prec_esp_noc
       
    
    #Este método toma el precio esperado del hotel, y lo multiplica por la estadía y el valor asociado al lujo del cuarto
    def calcular_precio_total(self, lujo, estadia):
        
        if lujo == 0:
            return (self._prec_esp_noc*0.85)*estadia
        
        elif lujo == 1:
            return (self._prec_esp_noc*1.3)*estadia
        
        else:
            return (self._prec_esp_noc*1.6)*estadia
        
    
    #Listar precios retorna un array con los precios
    #Posición 0: Cuarto simple
    #Posición 1: cuarto intermedio
    #Posición 2: cuarto lujoso
    #Si algún tipo de cuarto no se encuentra disponible, su posición respectiva va a ser null, y no se va ni a mostrar, ni a permitir reservarlo
    def listar_precios(self):
        
        precios = []
        
        #Si hay cuartos disponibles, se multiplican por su lujo respectivo y el resultado se mete en un array, en una posición en particular
        #Si no hay cuartos, esa misma posición queda como None, y el programa asume que no hay habitaciones de ese tipo.
        
        if self._cuartos_simples>=1:
            precios.insert(0, (self._prec_esp_noc*0.85))
        
        else:
            precios.insert(0, None)
            
        if self._cuartos_intermedios>=1:
            precios.insert(1, (self._prec_esp_noc*1.3))
            
        else:
            precios.insert(1, None)
            
        if self._cuartos_lujosos>=1:
            precios.insert(2, (self._prec_esp_noc*1.6))
            
        else:
            precios.insert(2, None)
            
        return precios
    
    
    #cuarto reservado descuenta el cuarto respectivo, y vuelve a calcular la demanda del hotel con esa información
    #La diferencia entre la demanda antigua y la actual se calcula con el método deltaDemanda, ese valor se le envía al destino
    def cuarto_reservado(self, noches, lujo, destino):
        
        if lujo == 0 and self._cuartos_simples>0:
            self._cuartos_simples-=1
            check = True
            
        elif lujo == 1 and self._cuartos_intermedios>0:
            self._cuartos_intermedios-=1
            check = True
            
        elif lujo == 2 and self._cuartos_lujosos>0:
            self._cuartos_lujosos-=1
            check = True
            
        else:
            check = False
            
        #El booleano check es para verificar que si se haya reservado un cuarto
        if check:
            demanda_previa = self._demanda
        
            self._demanda = self.calcular_demanda(self._cuartos_simples, self._cuartos_intermedios, self._cuartos_lujosos, self._prestigio, noches)
        
            if destino.reserva_hecha(self, lujo, self.delta_demanda(demanda_previa)):
                return True
                
            else:
                return False
            
        else:
            return False
        
        
    #delta demanda resta de la demanda actual la demanda antigua, obtiene la diferencia (delta).
    def delta_demanda(self, demanda_previa):
        return (self._demanda - demanda_previa)
         