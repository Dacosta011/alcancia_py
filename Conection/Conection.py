from mysql import connector
from mysql.connector import Error

class Conection:
    def conection(self):
        try:
            self.connection = connector.connect(host='localhost',
                                                database='alcancia',
                                                user='root',
                                                password='root')
            if self.connection.is_connected():
                return self.connection
        except Error as e:
            print(e)
    
    def desconection(self):
        self.connection.close()