import tkinter as tk

class Fieldframe(tk.Frame):
    def __init__(self, master,titulo_criterios, criterios, titulo_valores, valores=None, habilitado=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.criterios = criterios
        self.inputs= []
        
        tk.Label(self, text=titulo_criterios, font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self, text=titulo_valores, font=("Arial", 12, "bold")).grid(row=0, column=1, padx=5, pady=5)
        
        for i, criterio in enumerate(criterios):
            tk.Label(self, text=criterio).grid(row=i+1, column=0, padx=5, pady=5, sticky="w")
            
            if valores is None or valores[i] is None:
                valor_inicial = ""
            else:
                valor_inicial = valores[i]
                
            if habilitado is None or not habilitado[i]:
                estado = tk.DISABLED
            else:
                estado = tk.NORMAL
                
            ingreso_datos = tk.Entry(self)
            ingreso_datos.insert(0, valor_inicial)
            ingreso_datos.configure(state=estado)
            
            ingreso_datos.grid(row=i+1, column=1, padx=5, pady=5)
            
            self.inputs.append(ingreso_datos)
            
        self.boton_ok = tk.Button(self, text="Aceptar", command=self.verificar_campos)
        self.boton_ok.grid(row=len(self.criterios)+1, column=0, padx=5, pady=10)
        
        self.boton_cancelar = tk.Button(self, text="Cancelar", command=self.despejar)
        self.boton_cancelar.grid(row=len(self.criterios)+1, column=1, padx=5, pady=10)
        
    def get_value(self, criterio):
        
        return self.inputs[criterio].get()
    
        
    def procurar_todos(self):
        
        if self.verificar_campos():
                
            return [each.get() for each in self.inputs]
        
        else:
            
            return []
        
    
    def verificar_campos(self):
        for each in self.inputs:
            if not each.get():
                print("Faltan campos por llenar")
                return False
        print("Todos los campos están llenos")
        return True
    
    def despejar(self):
        for input in self.inputs:
            input.delete(0, tk.END)