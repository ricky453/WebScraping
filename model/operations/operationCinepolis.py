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
    
    def funcionesPorDia(self, fechaFuncion):
        nuevalista = []
        sql = "SELECT * FROM FUNCIONES WHERE FECHAFUNCION = '{}' ORDER BY HORAFUNCION ASC".format(fechaFuncion)

        try:
            self.miCursor.execute(sql)
            lista = self.miCursor.fetchall()
            for item in lista:
                nuevalista.append(item)
            return nuevaLista
        except Exception as e:
            return nuevalista
            raise
        
        


    def getFuncion(self, idPelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion):
        sql = "SELECT * FROM FUNCIONES WHERE IDPELICULA = '{}' AND DEPARTAMENTO = '{}' AND CINE = '{}' AND TIPO_DOBLAJE = '{}' AND FECHAFUNCION = '{}' AND HORAFUNCION = '{}'".format(idPelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion)
        try:
            self.miCursor.execute(sql)
            lista = self.miCursor.fetchone()
            
            print(sql)
        except Exception as e:
            raise

    def insertFunsiones(self, idPelicula, pelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion, sala):
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

    def getCupo(self, idPelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion):
        lista = None
        sql = "SELECT ASIENTOSOCUPADOS FROM FUNCIONES WHERE IDPELICULA = '{}' AND DEPARTAMENTO = '{}' AND CINE = '{}' AND TIPO_DOBLAJE = '{}' AND FECHAFUNCION = '{}' AND HORAFUNCION = '{}'".format(idPelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion)
        try:
            self.miCursor.execute(sql)
            lista = self.miCursor.fetchone()
            return lista[0]
        except Exception as e:
            return lista
            raise
# falta consulta para saber si el registro existe:
# select count(*) from FUNCIONES WHERE IDPELICULA = '{}' AND DEPARTAMENTO = '{}' AND CINE = '{}' AND TIPO_DOBLAJE = '{}' AND FECHAFUNCION = '{}' AND HORAFUNCION = '{}'

#database.insertCartelera(idPelicula, pelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion, sala)