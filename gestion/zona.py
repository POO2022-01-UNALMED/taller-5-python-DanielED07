from gestion.zoologico import Zoologico


class Zona():

    def __init__(self, nombre=None, z=None, animales=None):
        self._nombre = nombre
        self._zoo = []
        self._zoo.append(z)
        self._animales = animales

    def agregarAnimales(self, anim):

        if(self._animales == None):
            self._animales = []
            self._animales.append(anim)
        else:
            self._animales.append(anim)

    def cantidadAnimales(self):
        return len(self._animales)

    def getAnimales(self):
        return self._animales

    def getNombre(self):
        return self._nombre

    def getZoo(self):
        return self._zoo[0]
