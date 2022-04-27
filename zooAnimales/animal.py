from gestion.zona import Zona


class Animal():
    _totalAnimales = 0

    def __init__(self, nom=None, edad=None, hab=None, gen=None, zon=None):
        self._nombre = nom
        self._edad = edad
        self._habitat = hab
        self._genero = gen
        if(zon == None):
            self._zona = []
            self._zona.append(zon)
        if(isinstance(zon, Zona)):
            self._zona = []
            self._zona.append(zon)
        Animal._totalAnimales += 1

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil

        return "Mamiferos : "+str(Mamifero.cantidadMamiferos())+"\nAves : "+str(Ave.cantidadAves())+"\nReptiles : "+str(Reptil.cantidadReptiles())+"\nPeces : "+str(Pez.cantidadPeces())+"\nAnfibios : "+str(Anfibio.cantidadAnfibios())

    def movimiento():
        return "despazarse"

    def toString(self):
        if self._zona[0] != None:
            k = "Mi nombre es "+self._nombre+" , tengo una edad de "+str(self._edad)+" , habito en "+self._habitat+" y mi genero es " + \
                self._genero+",la zona en la que me ubico es " + \
                self._zona[0].getNombre()+" en el " + \
                self._zona[0].getZoo().getNombre()
        else:
            k = "Mi nombre es "+self._nombre+", tengo una edad de "+str(self._edad) + \
                ", habito en "+self._habitat+" y mi genero es "+self._genero
        return k

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero
