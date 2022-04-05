class Prestamo:
    def __init__(self,modalidad, socio, idPrestamo, fechaInicio, valor, cuota):
        self.modalidad = modalidad
        self.socio = socio
        self.idPrestamo = idPrestamo
        self.fechaInicio = fechaInicio
        self.valor = valor
        self.cuota = cuota
    # getters and setters
    def getModalidad(self):
        return self.modalidad
    def setModalidad(self,modalidad):
        self.modalidad = modalidad
    def getSocio(self):
        return self.socio
    def setSocio(self,socio):
        self.socio = socio
    def getIdPrestamo(self):
        return self.idPrestamo
    def setIdPrestamo(self,idPrestamo):
        self.idPrestamo = idPrestamo
    def getFechaInicio(self):
        return self.fechaInicio
    def setFechaInicio(self,fechaInicio):
        self.fechaInicio = fechaInicio
    def getValor(self):
        return self.valor
    def setValor(self,valor):
        self.valor = valor
    def getCuota(self):
        return self.cuota
    def setCuota(self,cuota):
        self.cuota = cuota
    def __str__(self):
        return "idPrestamo: " + str(self.idPrestamo) + " fechaInicio: " + self.fechaInicio + " valor: " + str(self.valor) + " cuota: " + str(self.cuota)