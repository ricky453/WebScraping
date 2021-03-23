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

    def getFuncion(self, id):
        sql = "SELECT * FROM FUNCIONES WHERE IDFUNCION = {}".format(id)
        try:
            self.miCursor.execute(sql)
            lista = self.miCursor.fetchone()
            
            print(lista)
        except Exception as e:
            raise

    def insertCartelera(self, idFuncion, pelicula, cine, departamento, fechaFuncion, fechaActual):
        sql = "INSERT INTO FUNCIONES(IDFUNCION, PELICULA, CINE, DEPARTAMENTO, FECHAFUNCION, FECHAACTUAL) VALUES({}, '{}', '{}','{}', '{}', '{}')".format(idFuncion, pelicula, cine, departamento, fechaFuncion, fechaActual)

        try:
            self.miCursor.execute(sql)
            self.miConnection.commit()
        except Exception as e:
            raise



database = OperationCinepolis()
database.listCartelera()
database.getFuncion(1)
#database.insertCartelera(2, "CABALLEROS DEL ZODIACO", "CINEPLIS METROCENTRO", "SANTA ANA", datetime.datetime.now() , date.today())