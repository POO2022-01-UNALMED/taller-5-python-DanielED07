from zooAnimales.animal import Animal


class Pez(Animal):
    salmones = 0
    bacalaos = 0
    _listado = None

    def __init__(self, nom=None, edad=None, hab=None, gen=None, colE=None, CantA=None):
        super().__init__(nom, edad, hab, gen)
        self._colorEscamas = colE
        self._cantidadAletas = CantA
        if Pez._listado == None:
            Pez._listado = []
            Pez._listado.append(self)
        else:
            Pez._listado.append(self)

    def movimiento():
        return "nadar"

    @classmethod
    def crearSalmon(self, nom, edad, gen):
        Pez.salmones += 1
        return Pez(nom, edad, "oceano", gen, colE="rojo", CantA=6)

    @classmethod
    def crearBacalao(self, nom, edad, gen):
        Pez.bacalaos += 1
        return Pez(nom, edad, "oceano", gen, colE="gris", CantA=6)

    @classmethod
    def cantidadPeces(cls):
        return cls.salmones+cls.bacalaos+len(cls._listado)

    def getColorEscamas(self):
        return self._colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas
