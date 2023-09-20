from zooAnimales.animal import Animal
class Pez (Animal):
    listado = []
    salmones = 0
    bacalaos = 0
    def __init__ (self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.listado.append(self)
    @classmethod
    def cantidadPeces (cls):
        return len(cls.listado)
    def movimiento (self):
        return "nadar"
    @classmethod 
    def crearSalmon (cls, nombre, edad, genero):
        cls.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)
    @classmethod 
    def crearBacalao (cls, nombre, edad, genero):
        cls.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "blanco", 6)
    @classmethod 
    def getListado (cls):
        return cls.listado
    @classmethod 
    def setListado (cls, listado):
        cls.listado = listado
    @classmethod 
    def getSalmones (cls):
        return cls.salmones
    @classmethod 
    def setSalmones (cls, salmones):
        cls.salmones = salmones
    @classmethod 
    def getBacalaos (cls):
        return cls.bacalaos
    @classmethod 
    def setBacalaos (cls, bacalaos):
        cls.bacalaos = bacalaos
    def getColorEscamas (self):
        return self._colorEscamas
    def setColorEscamas (self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getCantidadAletas (self):
        return self._cantidadAletas
    def setCantidadAletas (self, cantidadAletas):
        self._cantidadAletas = cantidadAletas