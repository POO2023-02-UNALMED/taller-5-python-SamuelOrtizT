from zooAnimales.animal import Animal
class Anfibio (Animal):
    listado = []
    ranas = 0
    salamandras = 0
    def __init__ (self, nombre, edad, habitat, genero, colorPiel, Venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._Venenoso = Venenoso
        Anfibio.listado.append(self)
    @classmethod
    def cantidadAnfibios (cls):
        return len(cls.listado)
    def movimiento (self):
        return "saltar"
    @classmethod 
    def crearRana (cls, nombre, edad, genero):
        cls.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)
    @classmethod 
    def crearSalamandra (cls, nombre, edad, genero):
        cls.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
    @classmethod 
    def getListado (cls):
        return cls.listado
    @classmethod 
    def setListado (cls, listado):
        cls.listado = listado
    @classmethod 
    def getRanas (cls):
        return cls.ranas
    @classmethod 
    def setRanas (cls, ranas):
        cls.ranas = ranas
    @classmethod 
    def getSalamandras (cls):
        return cls.salamandras
    @classmethod 
    def setSalamandras (cls, salamandras):
        cls.salamandras = salamandras
    def getColorPiel (self):
        return self._colorPiel
    def setColorPiel (self, colorPiel):
        self._colorPiel = colorPiel
    def isVenenoso (self):
        return self._Venenoso
    def setVenenoso (self, Venenoso):
        self._Venenoso = Venenoso