from Model.Empresa import Empresa
from Conection.Conection import Conection
from mysql.connector import Error

class GestorEmpresa:
    def __init__ (self):
        self.conecttion = Conection()
    
    def createEmpresa(self, nombre, direccion, numEmp, convenio):
        empresa = self.getEmpresa(nombre)
        if empresa is None:
            try:
                con = self.conecttion.conection()
                cursor = con.cursor()
                cursor.callproc('createEmpresa', [nombre, direccion, numEmp, convenio])
                con.commit()
                self.conecttion.desconection()
                return True
            except Error as e:
                print(e)
        return False
    
    def getEmpresa(self, idEmpresa):
        try:
            con = self.conecttion.conection()
            cursor = con.cursor()
            cursor.callproc('getEmpresa', [idEmpresa])
            for result in cursor.stored_results():
                for (nombre, direccion, numEmp, convenio) in result:
                    empresa = Empresa(nombre, direccion, numEmp, convenio)
                    return empresa
            self.conecttion.desconection()
        except Error as e:
            print(e)
            return None
    
    def allEmpresas(self):
        try:
            con = self.conecttion.conection()
            cursor = con.cursor()
            cursor.callproc('allEmpresas')
            empresas = []
            for result in cursor.stored_results():
                for (nombre, direccion, numEmp, convenio) in result:
                    empresa = Empresa(nombre, direccion, numEmp, convenio)
                    print(empresa)
                    print("\n")
                    empresas.append(empresa)
            self.conecttion.desconection()
            return empresas
        except Error as e:
            print(e)
            return None
    
    def deleteEmpresa(self, nombre):
        empresa = self.getEmpresa(nombre)
        if empresa is not None:
            try:
                con = self.conecttion.conection()
                cursor = con.cursor()
                cursor.callproc('deleteEmpresa', [nombre])
                con.commit()
                self.conecttion.desconection()
                return True
            except Error as e:
                print(e)
        return False
    
    def updateEmpresa(self, nombreAnt,nombreNu, direccion, numEmp, convenio):
        empresa = self.getEmpresa(nombreAnt)
        if empresa is not None:
            try:
                con = self.conecttion.conection()
                cursor = con.cursor()
                cursor.callproc('updateEmpresa', [nombreAnt, nombreNu, direccion, numEmp, convenio])
                con.commit()
                self.conecttion.desconection()
                return True
            except Error as e:
                print(e)
        return False