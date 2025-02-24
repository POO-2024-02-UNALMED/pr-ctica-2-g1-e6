import pickle

class CargarObjetos:
    
    @staticmethod
    def cargar_destinos():
        try:
            directorio = open("src/baseDatos/temp/destinos.pkl", "rb")
            destinos = pickle.load(directorio)
            directorio.close()
            return destinos
        except FileNotFoundError:
            return []
    
    @staticmethod
    def cargar_talleres():
        try:
            directorio = open("src/baseDatos/temp/registro.pkl", "rb")
            registro = pickle.load(directorio)
            directorio.close()
            print("Nice")
            return registro
        except FileNotFoundError:
            print("No pude cargar el objeto :(")
            return False
        
    @staticmethod
    def cargar_empresas():
        try:
            directorio = open("src/baseDatos/temp/empresas.pkl", "rb")
            empresas = pickle.load(directorio)
            directorio.close()
            return empresas
        except FileNotFoundError:
            return []
