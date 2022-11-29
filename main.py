import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',   ##Si el servidor no es local, se ponde la IP
            user='root',
            password='password',
            db='quiz_db'
        )

        self.cursor = self.connection.cursor()

        print ("Conexión establecida")


    def insertSubject():
        
