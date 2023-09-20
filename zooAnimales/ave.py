from zooAnimales.animal import Animal
class Ave (Animal):
    listado = []
    halcones = 0
    aguilas = 0
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)
    @classmethod
    def cantidadAves(cls):
        return len(cls.listado)
    def movimiento (self):
        return "volar"
    @classmethod
    def crearHalcon (cls, nombre, edad, genero):
        cls.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")
    @classmethod
    def crearAguila (cls, nombre, edad, genero):
        cls.aguilas +=1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
    @classmethod
    def getListado (cls):
        return cls.listado
    @classmethod
    def setListado (cls, listado):
        cls.listado = listado
    @classmethod
    def getHalcones (cls):
        return cls.halcones
    @classmethod
    def setHalcones (cls, halcones):
        cls.halcones = halcones
    @classmethod
    def getAguilas (cls):
        return cls.aguilas
    @classmethod
    def setAguilas (cls, aguilas):
        cls.aguilas = aguilas
    def getColorPlumas (self):
        return self._colorPlumas
    def setColorPlumas (self, colorPlumas):
        self._colorPlumas = colorPlumas