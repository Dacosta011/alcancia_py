class Modalidad:
    def __init__ (self, id, nombre, plazo, tasa):
        self.id = id
        self.nombre = nombre
        self.plazo = plazo
        self.tasa = tasa
    # getters and setters
    def getId(self):
        return self.id
    def setId(self,id):
        self.id = id
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre = nombre
    def getPlazo(self):
        return self.plazo
    def setPlazo(self,plazo):
        self.plazo = plazo
    def getTasa(self):
        return self.tasa
    def setTasa(self,tasa):
        self.tasa = tasa
    def __str__(self):
        return "id: " + str(self.id) + " nombre: " + self.nombre + " plazo: " + str(self.plazo) + " tasa: " + str(self.tasa)