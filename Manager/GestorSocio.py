from Model.Socio import Socio
from Conection.Conection import Conection
from mysql.connector import Error


class GestorSocio:
    def __init__(self):
        self.conecttion = Conection()
    
    def createSocio(self, id, nombre, direccion, tel, cargo, empresa):
        socio = self.getSocio(id)
        if socio is None:
            try:
                con = self.conecttion.conection()
                cursor = con.cursor()
                cursor.callproc('createSocio', [id, nombre, direccion, tel, cargo, empresa])
                con.commit()
                self.conecttion.desconection()
                return True
            except Error as e:
                print(e)
        return False

    def getSocio(self, id):
        try:
            con = self.conecttion.conection()
            cursor = con.cursor()
            cursor.callproc('getSocio', [id])
            for result in cursor.stored_results():
                for (id, nombre, direccion, tel, cargo, empresa) in result:
                    socio = Socio(id, nombre, direccion, tel, cargo, empresa)
            self.conecttion.desconection()
            return socio
        except Error as e:
            print(e)
            return None
    
    def allSocios(self):
        try:
            con = self.conecttion.conection()
            cursor = con.cursor()
            cursor.callproc('allSocios')
            socios = []
            for result in cursor.stored_results():
                for (id, nombre, direccion, tel, cargo, empresa) in result:
                    socio = Socio(id, nombre, direccion, tel, cargo, empresa)
                    print(socio)
                    print("\n")
                    socios.append(socio)
            self.conecttion.desconection()
            return socios
        except Error as e:
            print(e)
            return None
    
    def deleteSocio(self, id):
        socio = self.getSocio(id)
        if socio is not None:
            try:
                con = self.conecttion.conection()
                cursor = con.cursor()
                cursor.callproc('deleteSocio', [id])
                con.commit()
                self.conecttion.desconection()
                return True
            except Error as e:
                print(e)
        return False
    
    def updateSocio(self, idAnt,idNu, nombre, direccion, tel, cargo, empresa):
        socio = self.getSocio(idAnt)
        if socio is not None:
            try:
                con = self.conecttion.conection()
                cursor = con.cursor()
                cursor.callproc('updateSocio', [idAnt, idNu, nombre, direccion, tel, cargo, empresa])
                con.commit()
                self.conecttion.desconection()
                return True
            except Error as e:
                print(e)
        return False
    
    