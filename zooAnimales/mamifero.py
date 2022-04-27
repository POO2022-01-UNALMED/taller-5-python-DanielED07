from zooAnimales.animal import Animal


class Mamifero(Animal):
    caballos = 0
    leones = 0
    _listado = None

    def __init__(self, nom=None, edad=None, hab=None, gen=None, pelo=None, pats=None):
        super().__init__(nom, edad, hab, gen)
        self._pelaje = pelo
        self._patas = pats
        if Mamifero._listado == None:
            Mamifero._listado = []
            Mamifero._listado.append(self)
        else:
            Mamifero._listado.append(self)

    @classmethod
    def crearCaballo(self, nom, edad, gen):
        Mamifero.caballos += 1
        return Mamifero(nom, edad, "pradera", gen, pelo=True, pats=4)

    @classmethod
    def crearLeon(self, nom, edad, gen):
        Mamifero.leones += 1
        return Mamifero(nom, edad, "selva", gen, pelo=True, pats=4)

    @classmethod
    def cantidadMamiferos(cls):
        return cls.caballos+cls.leones  # +len(cls._listado)

    def isPelaje(self):
        return self._pelaje

    def getPatas(self):
        return self._patas
