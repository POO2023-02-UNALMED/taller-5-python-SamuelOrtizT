from zooAnimales.animal import Animal
class Reptil (Animal):
    listado = []
    iguanas = 0
    serpientes = 0
    def __init__ (self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado.append(self)
    @classmethod
    def cantidadReptiles (cls):
        return len(cls.listado)
    def movimiento (self):
        return "reptar"
    @classmethod 
    def crearIguana (cls, nombre, edad, genero):
        cls.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @classmethod 
    def crearSerpiente (cls, nombre, edad, genero):
        cls.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)
    @classmethod 
    def getListado (cls):
        return cls.listado
    @classmethod 
    def setListado (cls, listado):
        cls.listado = listado
    @classmethod 
    def getIguanas (cls):
        return cls.iguanas
    @classmethod 
    def setIguanas (cls, iguanas):
        cls.iguanas = iguanas
    @classmethod 
    def getSerpientes (cls):
        return cls.serpientes
    @classmethod 
    def setSerpientes (cls, serpientes):
        cls.serpientes = serpientes
    def getColorEscamas (self):
        return self._colorEscamas
    def setColorEscamas (self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getLargoCola (self):
        return self._largoCola
    def setLargoCola (self, largoCola):
        self._largoCola = largoCola