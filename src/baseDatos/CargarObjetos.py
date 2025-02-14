import pickle

class CargarObjetos:
    
    @staticmethod
    def cargar_destinos():
        try:
            directorio = open("src/baseDatos/temp/destinos.pkl", "rb")
            destinos = pickle.load(directorio)
            directorio.close()
            print("cargado")
            return destinos
        except FileNotFoundError:
            print("Consola: Procurando Destinos.")
            return []