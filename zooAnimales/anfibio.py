from zooAnimales.animal import Animal


class Anfibio(Animal):
    salamandras = 0
    ranas = 0
    _listado = None

    def __init__(self, nom=None, edad=None, hab=None, gen=None, colP=None, ven=None):
        super().__init__(nom, edad, hab, gen)
        self._colorPiel = colP
        self._venenoso = ven
        if Anfibio._listado == None:
            Anfibio._listado = []
            Anfibio._listado.append(self)
        else:
            Anfibio._listado.append(self)

    def movimiento():
        return "saltar"

    @classmethod
    def crearRana(self, nom, edad, gen):
        Anfibio.ranas += 1
        return Anfibio(nom, edad, "selva", gen, colP="rojo", ven=True)

    @classmethod
    def crearSalamandra(self, nom, edad, gen):
        Anfibio.salamandras += 1
        return Anfibio(nom, edad, "selva", gen, colP="negro y amarillo", ven=False)

    @classmethod
    def cantidadAnfibios(cls):
        return cls.ranas+cls.salamandras  # +len(cls._listado)

    def getColorPiel(self):
        return self._colorPiel

    def isVenenoso(self):
        return self._venenoso
