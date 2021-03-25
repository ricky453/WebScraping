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

    def getFuncion(self, idFuncion, idPelicula, pelicula, departamento, sala, fechaFuncion, horaFuncion):
        sql = "SELECT * FROM FUNCIONES WHERE IDFUNCION = {} AND IDPELICULA = '{}' AND PELICULA = '{}' AND DEPARTAMENTO = '{}' AND SALA = '{}' AND FECHAFUNCION = '{}' AND HORAFUNCION = '{}'".format(idFuncion, idPelicula, pelicula, departamento, sala, fechaFuncion, horaFuncion)
        try:
            self.miCursor.execute(sql)
            lista = self.miCursor.fetchone()
            
            print(lista)
        except Exception as e:
            raise

    def insertCartelera(self, idFuncion, idPelicula, pelicula, cine, departamento, tipoDoblaje, sala, fechaFuncion, horaFuncion):
        sql = "INSERT INTO FUNCIONES(IDFUNCION, IDPELICULA, PELICULA, CINE, DEPARTAMENTO, TIPO_DOBLAJE, SALA, FECHAFUNCION, HORAFUNCION) VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(idFuncion, idPelicula, pelicula, cine, departamento, tipoDoblaje, sala,fechaFuncion, horaFuncion)
        print(sql)
        try:
            self.miCursor.execute(sql)
            self.miConnection.commit()
        except Exception as e:
            raise



database = OperationCinepolis() 
database.listCartelera()
database.getFuncion(1, 'get_ticket123', 'ATAQUE A LOS TITANES', 'SAN SALVADOR', '1', datetime.date(2021, 3, 22), '17:05')
#database.insertCartelera(3, "get_ticket145", "EL PEPE", "CINEPOLIS SANTA ANA", "SANTA ANA", "TRADICIONAL", "2", date.today(), '19:45')