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
#|  +Última revisión: 2025-02-15-15-27, AlPerBara                                                                                   |
#|                                                                                                                                  |
#|  + Novedades:                                                                                                                    |
#|                                                                                                                                  |
#|      - Añadido soporte para mensajes de error personalizados.                                                                    |
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
    
    #mensaje_error_cabeza: El título de un mensaje de error personalizado que se mostrará si no se llenan todos los campos. No pasar este valor implica que se mostrará un mensaje genérico.
    
    #mensaje_error_cuerpo: Un mensaje de error personalizado que se mostrará si no se llenan todos los campos. Este valor va de la mano con mensaje_error_cabeza, si no se pasan los dos, no se mostrará ningún mensaje.
    
    #args y kwargs: Argumentos adicionales que se le pueden pasar al constructor de la clase padre (Frame)
    
    def __init__(self, master,titulo_criterios, criterios, titulo_valores, valores=None, habilitado=None, callback=None, mensaje_error_cabeza=None, mensaje_error_cuerpo=None,*args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.criterios = criterios
        #Inputs lleva seguimiento de todos los inputs que se crean, para poder procurar sus datos
        self.inputs= []
        self.callback = callback
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
        
    #get_value retorna el valor de un criterio específico
    #Recibe como argumento el índice del criterio que se quiere obtener
    def get_value(self, criterio):
        
        return self.inputs[criterio].get()
    
    
    #procurar_todos retorna una lista con todos los valores de los criterios,
    #la lista está en orden de los criterios que se pasaron al constructor
    #Si no se han llenado todos los campos, se muestra un mensaje de error y se retorna un array vacío.
    def procurar_todos(self):
        
        if self.verificar_campos(): #Primero se verifica que todos los campos estén llenos
                
            return [each.get() for each in self.inputs] #si lo están, se retorna una lista con los valores de los campos
        
        else: #si no, se retorna un array vacío
            
            return []
        
    
    #verificar_campos se encarga de verificar que todos los campos estén llenos
    #Si falta así sea uno, se muestra un mensaje de error y se retorna False
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
            
            #Si se pasó un mensaje de error personalizado, se muestra
            if self.mensaje_error_cabeza != None and self.mensaje_error_cuerpo != None:
                
                messagebox.showerror(self.mensaje_error_cabeza, self.mensaje_error_cuerpo)
                return False
            
            #Si no se pasó un mensaje de error personalizado, se muestra un mensaje genérico
            else:
                messagebox.showerror("Error", "Por favor diligencie todos los campos solicitados")
                return False
        
        #Si check es True, se retorna True, porque todos los campos están llenos
        else:   
            
            print("Diagnóstico: Todos los campos están llenos") #TODO: Remover print
            
            #Si se pasó una función de callback, se llama
            if self.callback:
                
                self.callback()
            
            #Si no se pasó una función de callback, se retorna True
            return True
    
    #despejar se encarga de borrar todos los campos, al presionar el botón de cancelar.
    def despejar(self):
        for input in self.inputs:
            input.delete(0, tk.END)