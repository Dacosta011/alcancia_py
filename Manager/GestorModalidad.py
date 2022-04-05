from Model.Modalidad import Modalidad
from Conection.Conection import Conection
from mysql.connector import Error


class GestorModalidad:
    def __init__(self):
        self.conecttion = Conection()

    def createModalidad(self, id, nombre, plazo, tasa):
        modalidad = self.getModalidad(id)
        if modalidad is None:
            try:
                con = self.conecttion.conection()
                cursor = con.cursor()
                cursor.callproc('createModalidad', [id, nombre, plazo, tasa])
                con.commit()
                self.conecttion.desconection()
                return True
            except Error as e:
                print(e)
        return False

    def getModalidad(self, id):
        try:
            con = self.conecttion.conection()
            cursor = con.cursor()
            cursor.callproc('getModalidad', [id])
            for result in cursor.stored_results():
                for (id, nombre, plazo, tasa) in result:
                    modalidad = Modalidad(id, nombre, plazo, tasa)
                    return modalidad
            self.conecttion.desconection()
        except Error as e:
            print(e)
            return None

    def allModalidades(self):
        try:
            con = self.conecttion.conection()
            cursor = con.cursor()
            cursor.callproc('allModalidades')
            modalidades = []
            for result in cursor.stored_results():
                for (id, nombre, plazo, tasa) in result:
                    modalidad = Modalidad(id, nombre, plazo, tasa)
                    print(modalidad)
                    print("\n")
                    modalidades.append(modalidad)
            self.conecttion.desconection()
            return modalidades
        except Error as e:
            print(e)
            return None
    
    def deleteModalidad(self, id):
        modalidad = self.getModalidad(id)
        if modalidad is not None:
            try:
                con = self.conecttion.conection()
                cursor = con.cursor()
                cursor.callproc('deleteModalidad', [id])
                con.commit()
                self.conecttion.desconection()
                return True
            except Error as e:
                print(e)
        return False
    
    def updateModalidad(self, idAnt,idNu, nombre, plazo, tasa):
        modalidad = self.getModalidad(idAnt)
        if modalidad is not None:
            try:
                con = self.conecttion.conection()
                cursor = con.cursor()
                cursor.callproc('updateModalidad', [idAnt, idNu, nombre, plazo, tasa])
                con.commit()
                self.conecttion.desconection()
                return True
            except Error as e:
                print(e)
        return False
    
    