class Animal ():
    totalAnimales = 0
    def __init__ (self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal.totalAnimales += 1
    def movimiento (self):
        return "desplazarse"
    @classmethod
    def totalPorTipo (cls):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return "Mamiferos :" + str(Mamifero.cantidadMamiferos()) + "\nAves :" + str(Ave.cantidadAves()) + "\nReptiles :" + str(Reptil.cantidadReptiles()) + "\nPeces :" + str(Pez.cantidadPeces()) + "\nAnfibios :" + str(Anfibio.cantidadAnfibios())
    def toString (self):
        from gestion.zoologico import Zoologico
        if self._zona == None:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona.getNombre() + ", en el " + self._zona.getZoo().getNombre()
    @classmethod
    def getTotalAnimales (cls):
        return cls.totalAnimales
    @classmethod
    def setTotalAnimales (cls, totalAnimales):
        Animal.totalAnimales = totalAnimales
    def getNombre (self):
        return self._nombre
    def setNombre (self, nombre):
        self._nombre = nombre
    def getEdad (self):
        return self._edad
    def setEdad (self, edad):
        self._edad = edad
    def getHabitat (self):
        return self._habitat
    def setHabitat (self, habitat):
        self._habitat = habitat
    def getGenero (self):
        return self._genero
    def setGenero (self, genero):
        self._genero = genero
    def getZona (self):
        return self._zona
    def setZona (self, zona):
        self._zona = zona