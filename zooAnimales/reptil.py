from zooAnimales.animal import Animal


class Reptil(Animal):

    iguanas = 0
    serpientes = 0
    _listado = None

    def __init__(self, nom=None, edad=None, hab=None, gen=None, colE=None, larC=None):
        super().__init__(nom, edad, hab, gen)
        self._colorEscamas = colE
        self._largoCola = larC
        if Reptil._listado == None:
            Reptil._listado = []
            Reptil._listado.append(self)
        else:
            Reptil._listado.append(self)

    def movimiento():
        return "reptar"

    @classmethod
    def crearIguana(self, nom, edad, gen):
        Reptil.iguanas += 1
        return Reptil(nom, edad, "humedal", gen, colE="verde", larC=3)

    @classmethod
    def crearSerpiente(self, nom, edad, gen):
        Reptil.serpientes += 1
        return Reptil(nom, edad, "jungla", gen, colE="blanco", larC=1)

    @classmethod
    def cantidadReptiles(cls):
        return cls.iguanas+cls.serpientes  # +len(cls._listado)

    def getColorEscamas(self):
        return self._colorEscamas

    def getLargoCola(self):
        return self._largoCola
