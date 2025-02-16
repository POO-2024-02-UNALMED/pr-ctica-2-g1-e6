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
    
    @staticmethod
    def cargar_talleres():
        try:
            directorio = open("src/baseDatos/temp/registro.pkl", "rb")
            registro = pickle.load(directorio)
            directorio.close()
            return registro
        except FileNotFoundError:
            print("No pude cargar el objeto :(")
            return 1
