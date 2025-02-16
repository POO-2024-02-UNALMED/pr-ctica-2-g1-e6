import pickle

class GuardarObjetos:
    
    @staticmethod
    def guardar_destinos(destinos):
        
        directorio = open("src/baseDatos/temp/destinos.pkl", "wb")
        
        pickle.dump(destinos, directorio)
        
        directorio.close()
        print("Consola: Destinos guardados.")

    @staticmethod
    def guardar_registro(registro):
        
        directorio = open("src/baseDatos/temp/registro.pkl", "wb")
        
        pickle.dump(registro, directorio)
        
        directorio.close()
