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

    def getFuncion(self, idPelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion):
        sql = "SELECT * FROM FUNCIONES WHERE IDPELICULA = '{}' AND DEPARTAMENTO = '{}' AND CINE = '{}' AND TIPO_DOBLAJE = '{}' AND FECHAFUNCION = '{}' AND HORAFUNCION = '{}'".format(idPelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion)
        try:
            self.miCursor.execute(sql)
            lista = self.miCursor.fetchone()
            
            print(sql)
        except Exception as e:
            raise

    def insertCartelera(self, idPelicula, pelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion, sala):
        sql = "INSERT INTO FUNCIONES(IDPELICULA, PELICULA, DEPARTAMENTO, CINE, TIPO_DOBLAJE, FECHAFUNCION, HORAFUNCION, SALA) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(idPelicula, pelicula, departamento, cine, tipo_doblaje,fechaFuncion, horaFuncion, sala)
        print(sql)
        try:
            self.miCursor.execute(sql)
            self.miConnection.commit()
        except Exception as e:
            raise

    def updateAsientosOcupados(self, idPelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion, asientosOcupados):
        sql = "UPDATE FUNCIONES  SET ASIENTOSOCUPADOS='{}' WHERE IDPELICULA = '{}' AND DEPARTAMENTO = '{}' AND CINE = '{}' AND TIPO_DOBLAJE = '{}' AND FECHAFUNCION = '{}' AND HORAFUNCION = '{}'".format(asientosOcupados, idPelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion)
        print(sql)
        try:
            self.miCursor.execute(sql)
            self.miConnection.commit()
        except Exception as e:
            raise


database = OperationCinepolis() 
database.listCartelera()
# falta consulta para saber si el registro existe:
# select count(*) from FUNCIONES WHERE IDPELICULA = '{}' AND DEPARTAMENTO = '{}' AND CINE = '{}' AND TIPO_DOBLAJE = '{}' AND FECHAFUNCION = '{}' AND HORAFUNCION = '{}'
#falta consulta de toda la tabla por fecha
#database.getFuncion(idPelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion)
#database.insertCartelera(idPelicula, pelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion, sala)