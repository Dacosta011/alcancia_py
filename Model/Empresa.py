class Empresa:
    def __init__(self,nombre, direccion, numEmp, convenio):
        self.nombre = nombre
        self.direccion = direccion
        self.numEmp = numEmp
        self.convenio = convenio
    # getters and setters
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre = nombre
    def getDireccion(self):
        return self.direccion
    def setDireccion(self,direccion):
        self.direccion = direccion
    def getNumEmp(self):
        return self.numEmp
    def setNumEmp(self,numEmp):
        self.numEmp = numEmp
    def getConvenio(self):
        return self.convenio
    def setConvenio(self,convenio):
        self.convenio = convenio
    def __str__(self):
        return "nombre: " + self.nombre + " direccion: " + self.direccion + " numEmp: " + str(self.numEmp) + " convenio: " + self.convenio