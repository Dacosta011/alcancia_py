from Model.Prestamo import Prestamo
from Conection.Conection import Conection
from mysql.connector import Error

class GestorPrestamo:
    def __init__(self):
        self.conecttion = Conection()
    
    def createPrestamo(self, modalidad, socio, prestamo, fechaInicio, valor, cuota):
        prestamo = self.getPrestamo(modalidad, socio, prestamo)
        if prestamo is None:
            print('entreeee')
            try:
                con = self.conecttion.conection()
                cursor = con.cursor()
                cursor.callproc('createPrestamo', [modalidad, socio, prestamo, fechaInicio, valor, cuota])
                con.commit()
                self.conecttion.desconection()
                return True
            except Error as e:
                print(e)
        return False

    def getPrestamo(self, modalidad, socio, prestamo):
        try:
            con = self.conecttion.conection()
            cursor = con.cursor()
            cursor.callproc('getPrestamo', [modalidad, socio, prestamo])
            for result in cursor.stored_results():
                for (modalidad, socio, prestamo, fechaInicio, valor, cuota) in result:
                    prestamo = Prestamo(modalidad, socio, prestamo, fechaInicio, valor, cuota)
                    return prestamo
            self.conecttion.desconection()
        except Error as e:
            print(e)
            return None

    def allPrestamos(self):
        try:
            con = self.conecttion.conection()
            cursor = con.cursor()
            cursor.callproc('allPrestamos')
            prestamos = []
            for result in cursor.stored_results():
                for (modalidad, socio, prestamo, fechaInicio, valor, cuota) in result:
                    prestamo = Prestamo(modalidad, socio, prestamo, fechaInicio, valor, cuota)
                    print(prestamo)
                    print("\n")
                    prestamos.append(prestamo)
            self.conecttion.desconection()
            return prestamos
        except Error as e:
            print(e)
            return None
    
    def deletePrestamo(self, modalidad, socio, prestamo):
        prestamo = self.getPrestamo(modalidad, socio, prestamo)
        if prestamo is not None:
            try:
                con = self.conecttion.conection()
                cursor = con.cursor()
                cursor.callproc('deletePrestamo', [modalidad, socio, prestamo])
                con.commit()
                self.conecttion.desconection()
                return True
            except Error as e:
                print(e)
        return False
    
    def updatePrestamo(self, modalidadAnt, socioAnt, prestamoAnt,modalidadNu, socioNu, prestamoNu, fechaInicio, valor, cuota):
        prestamo = self.getPrestamo(modalidadAnt, socioAnt, prestamoAnt)
        if prestamo is not None:
            try:
                con = self.conecttion.conection()
                cursor = con.cursor()
                cursor.callproc('updatePrestamo', [modalidadAnt, socioAnt, prestamoAnt, modalidadNu, socioNu, prestamoNu, fechaInicio, valor, cuota])
                con.commit()
                self.conecttion.desconection()
                return True
            except Error as e:
                print(e)
        return False


