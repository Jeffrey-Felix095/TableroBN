
class barco():
    casillas=[]
    def __init__(self, nombre : str, tamano : int, casillas):
        self._name = nombre
        self._size = tamano
        self.casillas=casillas
    def getNombre(self):
        return self._name
    def getSize(self):
        return self._size
    def ubicar(self,tablero):
        pass
        #Metodo utilizado para ubicar el en el tablero.