from zooAnimales.animal import Animal
class Mamifero (Animal):
    listado = []
    caballos = 0
    leones = 0
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls.listado)
    @classmethod
    def crearCaballo (cls, nombre, edad, genero):
        cls.caballos += 1
        return cls(nombre, edad, "pradera", genero, True, 4)
    @classmethod
    def crearLeon (cls, nombre, edad, genero):
        cls.leones += 1
        return cls(nombre, edad, "selva", genero, True, 4)
    @classmethod
    def getListado (cls):
        return cls.listado
    @classmethod
    def setListado (cls, listado):
        cls.listado = listado
    @classmethod
    def getCaballos (cls):
        return cls.caballos
    @classmethod
    def setCaballos (cls, caballos):
        cls.caballos = caballos
    @classmethod
    def getLeones (cls):
        return cls.leones
    @classmethod
    def setLeones (cls, leones):
        cls.leones = leones
    def isPelaje (self):
        return self._pelaje
    def setPelaje (self, pelaje):
        self._pelaje = pelaje
    def getPatas (self):
        return self._patas
    def setPatas (self, patas):
        self._patas = patas