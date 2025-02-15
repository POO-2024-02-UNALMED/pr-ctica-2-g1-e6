#|==================================================================================================================================|
#|                                                                                                                                  |
#|  Copyright (c) 2025 Agencia de Viajes Mundo Aventura S.A.                                                                        |
#|                                                                                                                                  |
#|                                                                                                                                  |
#|  + Nombre del módulo:                                                                                                            |
#|                                                                                                                                  |
#|      Fieldframe.py                                                                                                               |
#|                                                                                                                                  |
#|  + Resumen:                                                                                                                      |
#|                                                                                                                                  |
#|      - Este módulo contiene el componente genérico utilizado para representar formularios de tipo clave-valor,                   |
#|              a este componente se le pueden asignar tantos pares clave-valor como sean necesarios,                               |
#|              y se puede habilitar o deshabilitar la edición de cada campo de forma independiente.                                |
#|      - Cada componente de tipo Fieldframe es capaz de verificar que todos los campos estén llenos antes de                       |
#|              de permitir que el usuario continúe.                                                                                |
#|      - Es posible pasarle a los objetos Fieldframe una función para que llamen a a hora                                          |
#|              de presionar el botón de aceptar.                                                                                   |
#|                                                                                                                                  |
#|  + Codificado por:                                                                                                               |
#|                                                                                                                                  |
#|      - Alejandro Pérez Barrera (2025-02-15) (Creador)                                                                            |
#|                                                                                                                                  |
#|  +Última revisión: 2025-02-15-16-25, AlPerBara                                                                                   |
#|                                                                                                                                  |
#|  + Novedades:                                                                                                                    |
#|                                                                                                                                  |
#|      - Ahora get_value retorna None si se ejecuta referente a un campo vacío.                                                    |
#|      - Actualmente este módulo solo está optimizado para la funcionalidad de reservar hoteles.                                   |
#|                                                                                                                                  |
#|  + Pendientes en este módulo:                                                                                                    |
#|                                                                                                                                  |
#|      - Ajustar a las necesidades de cada funcionalidad.                                                                          |
#|      - Verificar errores.                                                                                                        |
#|                                                                                                                                  |
#|==================================================================================================================================|


import tkinter as tk #Se importa la librería tkinter para hacer uso de labels, entries, botones, et al.
from tkinter import messagebox #Messagebox se utiliza para mostrar mensajes de error al usuario.

class Fieldframe(tk.Frame):
    #Los argumentos que tomará el constructor son:
    
    #master: El frame al que pertenece este Fieldframe
    
    #titulo_criterios: El título que se le dará a la columna de criterios
    
    #criterios: Una lista con los nombres de los criterios
    
    #titulo_valores: El título que se le dará a la columna de valores
    
    #valores: Una lista con los valores iniciales de los criterios. No pasar este valor implica que los campos estarán vacíos.
    
    #habilitado: Una lista de booleanos que indican si el campo es editable o no. No pasar este valor implica que todos los campos son editables.
    
    #callback: Una función que se llamará cuando se presione el botón de aceptar. No pasar este valor implica que no se llamará ninguna función.
    
    #mostrar_error: Un booleano que indica si se mostrará un mensaje de error si no se llenan todos los campos. No pasar este valor implica que SI se mostrará un mensaje de error.
    
    #mensaje_error_cabeza: El título de un mensaje de error personalizado que se mostrará si no se llenan todos los campos. No pasar este valor implica que se mostrará un mensaje genérico.
    
    #mensaje_error_cuerpo: Un mensaje de error personalizado que se mostrará si no se llenan todos los campos. Este valor va de la mano con mensaje_error_cabeza, si no se pasan los dos, no se mostrará ningún mensaje.
    
    #args y kwargs: Argumentos adicionales que se le pueden pasar al constructor de la clase padre (Frame)
    
    def __init__(self, master, titulo_criterios, criterios, titulo_valores, valores=None, habilitado=None, callback=None,mostrar_error=True, mensaje_error_cabeza=None, mensaje_error_cuerpo=None,*args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.criterios = criterios
        #Inputs lleva seguimiento de todos los inputs que se crean, para poder procurar sus datos
        self.inputs= []
        self.callback = callback
        self.mostrar_error = mostrar_error
        self.mensaje_error_cabeza = mensaje_error_cabeza
        self.mensaje_error_cuerpo = mensaje_error_cuerpo
        
        #Estos labels son los títulos de las columnas, criterios y valores
        tk.Label(self, text=titulo_criterios, font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self, text=titulo_valores, font=("Arial", 12, "bold")).grid(row=0, column=1, padx=5, pady=5)
        
        #Por cada criterio se crea un label y un entry
        for i, criterio in enumerate(criterios):
            tk.Label(self, text=criterio).grid(row=i+1, column=0, padx=5, pady=5, sticky="w")
            
            #Si no se pasan valores iniciales, se deja el campo vacío
            if valores is None or valores[i] is None:
                valor_inicial = ""
            else:
                valor_inicial = valores[i]
                
            #Si no se pasa la lista de habilitados, se asume que todos los campos son editables
            if habilitado is None or habilitado[i]:
                estado = tk.NORMAL
            else:
                #Un campo solo es de solo lectura si se pasa la lista de habilitados y el valor es False
                estado = tk.DISABLED
                
            ingreso_datos = tk.Entry(self)
            ingreso_datos.insert(0, valor_inicial)
            ingreso_datos.configure(state=estado)
            
            ingreso_datos.grid(row=i+1, column=1, padx=5, pady=5)
            #Se añade el entry a la lista de inputs
            self.inputs.append(ingreso_datos)
            
        #Botón de aceptar y cancelar
        self.boton_ok = tk.Button(self, text="Aceptar", command=self.verificar_campos)
        self.boton_ok.grid(row=len(self.criterios)+1, column=0, padx=5, pady=10)
        
        self.boton_cancelar = tk.Button(self, text="Cancelar", command=self.despejar)
        self.boton_cancelar.grid(row=len(self.criterios)+1, column=1, padx=5, pady=10)
        
    
    
    #|==============================================================================================================|
    #|                                                                                                              |
    #|  get_value(criterio):                                                                                        |
    #|      Descripción:                                                                                            |
    #|              - Retorna el valor de un criterio en particular,                                                |
    #|                      de la lista de criterios que se le pasan al constructor en el atributo "criterios".     |
    #|              - ESTA FUNCIÓN NO VERIFICA SI EL DATO ES VÁLIDO, SOLO RETORNA EL VALOR DEL CAMPO.               |
    #|                                                                                                              |
    #|      Parámetros:                                                                                             |
    #|              - criterio: El índice del criterio que se quiere obtener.                                       |
    #|                                                                                                              |
    #|      Retorno:                                                                                                |
    #|              - Retorna el valor del campo en la posición especificada.                                       |
    #|              - Si el campo está vacío, se retorna None.                                                      |
    #|                                                                                                              |
    #|==============================================================================================================|
    def get_value(self, criterio):
        
        if self.inputs[criterio].get() == "":
            return None
        
        else:
            return self.inputs[criterio].get()
        
    
    
    #|==================================================================================================================|
    #|   procurar_datos:                                                                                                |
    #|      Descripción:                                                                                                |
    #|             - Retorna una lista con todos los valores de los criterios,                                          |
    #|                      la lista está en orden de los criterios que se pasaron al constructor.                      |
    #|             - ESTA FUNCIÓN NO VERIFICA SI TODOS LOS DATOS SON VÁLIDOS, SOLO RETORNA LOS VALORES DE LOS CAMPOS.   |
    #|                                                                                                                  |
    #|      Parámetros:                                                                                                 |
    #|             - No recibe parámetros.                                                                              |
    #|                                                                                                                  |
    #|      Retorno:                                                                                                    |        
    #|             - Retorna una lista con los valores de los campos en el orden especificado en el constructor.        |
    #|             - Si no se han llenado todos los campos, se añade un None en el espacio vacío.                       |
    #|==================================================================================================================|
    def procurar_todos(self):
        
        retorno = []#en este array se guardarán los valores de los campos
            
        #Se recorre la lista de inputs   
        for each in self.inputs:
            
            #Si el campo está vacío, se añade un None a la lista
            if each.get() == "":
                retorno.append(None)
            
            else:
                retorno.append(each.get())
                
        return retorno #se retorna la lista con los valores de los campos
        
        
    
    #|==========================================================================================================================|
    #|                                                                                                                          |
    #|      verificar_campos:                                                                                                   |
    #|          Descripción:                                                                                                    |
    #|              - Verifica que todos los campos estén llenos.                                                               |
    #|              - Puede mostrar un mensaje de error al faltar así sea uno de los campos.                                    |
    #|              - Puede ejecutar una función si esta se especifica en el constructor si todos los campos están llenos.      |
    #|              - Si se desactiva el mensaje de error, se ejecuta la función que se haya especificado.                      |
    #|                                                                                                                          |
    #|      Parámetros:                                                                                                         |
    #|             - No recibe parámetros.                                                                                      |
    #|                                                                                                                          |
    #|       Retorno:                                                                                                           |
    #|              - Retorna True si todos los campos están llenos (Si no se especifica una función de retorno).               |
    #|              - Retorna False si falta al menos un campo (Si no se especifica una función de retorno).                    |
    #|              - No retorna nada si se especifica una función de retorno y todos los campos están llenos.                  |
    #|              - Muestra un mensaje de error si faltan campos por diligenciar (A no ser que se desactive el mensaje).      |
    #|                                                                                                                          |
    #|==========================================================================================================================|
    def verificar_campos(self):
        
        #Primero se asume que todos los campos están llenos
        check = True
        
        #Se recorre la lista de inputs
        for each in self.inputs:
            
            if not each.get():
                #si alguno de los campos está vacío, se cambia el valor de check a False
                check = False
        
        #Si check es False, se muestra un mensaje de error y se retorna False, porque no todos los campos están llenos
        if not check:
            
            #Verificar si se debe mostrar un mensaje de error
            if self.mostrar_error:
            
                #Si se pasó un mensaje de error personalizado, se muestra
                if self.mensaje_error_cabeza != None and self.mensaje_error_cuerpo != None:

                    messagebox.showerror(self.mensaje_error_cabeza, self.mensaje_error_cuerpo)
                    return False

                #Si no se pasó un mensaje de error personalizado, se muestra un mensaje genérico
                else:
                    messagebox.showerror("Error", "Por favor diligencie todos los campos solicitados")
                    return False
            
            #Si no se debe mostrar un mensaje de error, se ejecuta el callback    
            else:
                
                #Si se pasó una función de callback, se llama
                if self.callback:
                
                    self.callback()
            
                #Si no se pasó una función de callback, se retorna True
                return True
        
        #Si check es True, se retorna True, porque todos los campos están llenos
        else:   
            
            print("Diagnóstico: Todos los campos  del Fieldframe están llenos") #TODO: Remover print
            
            #Si se pasó una función de callback, se llama
            if self.callback:
                
                self.callback()
            
            #Si no se pasó una función de callback, se retorna True
            return True
    


    #|======================================================|
    #|                                                      |
    #|      despejar:                                       |
    #|          Descripción:                                |
    #|              - Borra todos los campos de texto.      |
    #|                                                      |
    #|      Parámetros:                                     |
    #|              - No recibe parámetros.                 |
    #|                                                      |
    #|      Retorno:                                        |
    #|              - No retorna nada.                      |
    #|                                                      |
    #|======================================================|
    def despejar(self):
        for input in self.inputs:
            input.delete(0, tk.END)