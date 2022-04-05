class Socio:
    def __init__(self,id,nombre, direccion, tel, cargo, empresa):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel
        self.cargo = cargo
        self.empresa = empresa
    # getters and setters
    def getId(self):
        return self.id
    def setId(self,id):
        self.id = id
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre = nombre
    def getDireccion(self):
        return self.direccion
    def setDireccion(self,direccion):
        self.direccion = direccion
    def getTel(self):
        return self.tel
    def setTel(self,tel):
        self.tel = tel
    def getCargo(self):
        return self.cargo
    def setCargo(self,cargo):
        self.cargo = cargo
    def getEmpresa(self):
        return self.empresa
    def setEmpresa(self,empresa):
        self.empresa = empresa
    def __str__(self):
        return "id: " + str(self.id) + " nombre: " + self.nombre + " direccion: " + self.direccion + " tel: " + self.tel + " cargo: " + self.cargo + " empresa: " + self.empresa