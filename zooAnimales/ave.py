from zooAnimales.animal import Animal


class Ave(Animal):
    halcones = 0
    aguilas = 0
    _listado = None

    def __init__(self, nom=None, edad=None, hab=None, gen=None, colP=None):
        super().__init__(nom, edad, hab, gen)
        self._colorPlumas = colP
        if Ave._listado == None:
            Ave._listado = []
            Ave._listado.append(self)
        else:
            Ave._listado.append(self)

    def movimiento():
        return "volar"

    @classmethod
    def crearHalcon(self, nom, edad, gen):
        Ave.halcones += 1
        return Ave(nom, edad, "montanas", gen, colP="cafe glorioso")

    @classmethod
    def crearAguila(self, nom, edad, gen):
        Ave.aguilas += 1
        return Ave(nom, edad, "montanas", gen, colP="blanco y amarillo")

    @classmethod
    def cantidadAves(cls):
        return cls.halcones+cls.aguilas+len(cls._listado)

    def getColorPlumas(self):
        return self._colorPlumas
