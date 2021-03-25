import sys
sys.path.insert(1,'model/conexion/') 
from conexion import DataBase
import datetime
from datetime import date


class OperationCinepolis:

    db = DataBase()
    miCursor = db.getCursor()
    miConnection = db.getConnection()

    def __init__(self):
        sql = "vacio"
    
    def listCartelera(self):
        sql = "SELECT * FROM FUNCIONES"

        try:
            self.miCursor.execute(sql)
            lista = self.miCursor.fetchall()
            for item in lista:
                print(item)
        except Exception as e:
            raise

    def getFuncion(self, idPelicula, pelicula, departamento, sala, fechaFuncion, horaFuncion):
        sql = "SELECT * FROM FUNCIONES WHERE IDPELICULA = '{}' AND PELICULA = '{}' AND DEPARTAMENTO = '{}' AND SALA = '{}' AND FECHAFUNCION = '{}' AND HORAFUNCION = '{}'".format(idPelicula, pelicula, departamento, sala, fechaFuncion, horaFuncion)
        try:
            self.miCursor.execute(sql)
            lista = self.miCursor.fetchone()
            
            print(lista)
        except Exception as e:
            raise

    def insertCartelera(self, idPelicula, pelicula, cine, departamento, sala, fechaFuncion, horaFuncion):
        sql = "INSERT INTO FUNCIONES(IDPELICULA, PELICULA, CINE, DEPARTAMENTO, SALA, FECHAFUNCION, HORAFUNCION) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(idPelicula, pelicula, cine, departamento, sala,fechaFuncion, horaFuncion)
        print(sql)
        try:
            self.miCursor.execute(sql)
            self.miConnection.commit()
        except Exception as e:
            raise



database = OperationCinepolis() 
database.listCartelera()
database.getFuncion('get_ticket1499', 'EL CAMPEOM', 'METAPAN','1', datetime.date(2021, 3, 24), '19:45')
#database.insertCartelera("get_ticket1499", "EL CAMPEOM", "CINEPOLIS SANTA ANA", "METAPAN", "1", date.today(), '19:45')