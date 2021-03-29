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

    def getCines(self, fechaBuscar):
        sql = "SELECT DISTINCT CINE FROM FUNCIONES WHERE FECHAFUNCION = '{}'".format(fechaBuscar)
        try:
            self.miCursor.execute(sql)
            lista = self.miCursor.fetchall()

            return lista
        except Exception as e:
            raise
    
    def getPeliculasFunciones(self, cine, fechaBuscar):
        sql = "SELECT DISTINCT PELICULA FROM FUNCIONES WHERE CINE = '{}' AND FECHAFUNCION = '{}'".format(cine, fechaBuscar)
        try:
            self.miCursor.execute(sql)
            lista = self.miCursor.fetchall()

            return lista
        except Exception as e:
            raise
    

    def getPeliculasPorCine(self, cine, fechaBuscar):
        sql = "SELECT DISTINCT HORAFUNCION, PELICULA FROM FUNCIONES WHERE CINE = '{}' AND FECHAFUNCION = '{}'".format(cine, fechaBuscar)
        try:
            self.miCursor.execute(sql)
            lista = self.miCursor.fetchall()

            return lista
        except Exception as e:
            raise
    
    def comprobarExistenciaFuncion(self, idPelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion):
        nuevalista = []
        sql = "SELECT COUNT(*) FROM FUNCIONES WHERE IDPELICULA = '{}' AND DEPARTAMENTO = '{}' AND CINE = '{}' AND TIPO_DOBLAJE = '{}' AND FECHAFUNCION = '{}' AND HORAFUNCION = '{}'".format(idPelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion)
        
        count=0
        try:
            self.miCursor.execute(sql)
            count = self.miCursor.fetchone()
            
            return count[0]
        except Exception as e:
            return count
            raise

    def deleteFuncitions(self, fechaFuncion):
        sql = "SELECT * FROM FUNCIONES WHERE FECHAFUNCION = '{}'".format(fechaFuncion)
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

    def getCupoPelicula(self, idPelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion, sala):
        lista = None
        sql = "SELECT ASIENTOSOCUPADOS, PELICULA FROM FUNCIONES WHERE IDPELICULA = '{}' AND DEPARTAMENTO = '{}' AND CINE = '{}' AND TIPO_DOBLAJE = '{}' AND FECHAFUNCION = '{}' AND HORAFUNCION = '{}' AND SALA = '{}'".format(idPelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion, sala)
        try:
            self.miCursor.execute(sql)
            lista = self.miCursor.fetchall()
            return lista[0]
        except Exception as e:
            return lista
            raise
# falta consulta para saber si el registro existe:
# 

#database.insertCartelera(idPelicula, pelicula, departamento, cine, tipo_doblaje, fechaFuncion, horaFuncion, sala)