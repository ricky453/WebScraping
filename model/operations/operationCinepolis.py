import sys
sys.path.insert(1,'model/conexion/') 
from conexion import DataBase


class OperationCinepolis:

    db = DataBase()
    miCursor = db.getCursor()

    def __init__(self):
        sql = "vacio"
    
    def listProductos(self):
        sql = "SELECT * FROM PRODUCTOS"

        try:
            self.miCursor.execute(sql)
            lista = self.miCursor.fetchall()
            for item in lista:
                print(item)
        except Exception as e:
            raise

    def getProducto(self, id):
        sql = "SELECT * FROM PRODUCTOS WHERE CÓDIGOARTÍCULO = '{}'".format(id)
        try:
            self.miCursor.execute(sql)
            lista = self.miCursor.fetchone()
            
            print(lista)
        except Exception as e:
            raise

    def insertProducto(self, codArticulo, seccion, nomArticulo, precio, fecha, importado, paisOrigen):
        sql = "INSERT INTO PRODUCTOS(CÓDIGOARTÍCULO, SECCIÓN, NOMBREARTÍCULO, PRECIO, FECHA, IMPORTADO, PAÍSDEORIGEN) VALUES('{}', '{}', '{}',{}, '{}', '{}', '{}')".format(codArticulo, seccion, nomArticulo, precio, fecha, importado, paisOrigen )

        try:
            self.miCursor.execute(sql)
            self.miCursor.commit()
        except Exception as e:
            raise



database = OperationCinepolis()
database.listProductos()
database.getProducto('AR06')
#database.insertProducto('AR43', 'MEMES', 'DAMA', 700, '12/01/2021', 'VERDADERO', 'BAGDAK')