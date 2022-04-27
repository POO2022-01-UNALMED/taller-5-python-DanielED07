from asyncio.windows_events import NULL


from gestion.zona import Zona


class Zoologico():

    def __init__(self, nombre=None, ubicacion=None, zonas=None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas

    def cantidadTotalAnimales(self):
        k = 0
        for i in self._zonas:
            if(isinstance(i, Zona)):
                k = k+i.cantidadAnimales()
        return k

    def agregarZonas(self, z):
        if(isinstance(z, Zona)):
            if(self._zonas == None):
                self._zonas = []
                self._zonas.append(z)
            else:
                self._zonas.append(z)

    def getNombre(self):
        return self._nombre

    def getZona(self):
        return self._zonas
