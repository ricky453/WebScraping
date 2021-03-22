import pymysql

#creando clase conexion
class DataBase:

    #credenciales
    servidor = "localhost"
    usuario = "root"
    contra = "" #vacio
    bd = "pruebas"

    #creando conexion
    def __init__(self):
        self.connection = pymysql.connect(
            host = self.servidor,
            user = self.usuario,
            password = self.contra,
            db = self.bd
        )

        self.cursor = self.connection.cursor()
        print("Codigo se ejecuto con exito")

    def getCursor(self):
        return self.cursor

    
