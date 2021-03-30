import schedule
import time
from datetime import datetime
from datetime import date
from BuscarPeli import Buscar_Peli

import sys
sys.path.insert(1, 'model/operations/')
from operationCinepolis import OperationCinepolis

metodo = Buscar_Peli()

def saludar():
    print("hola")

def obtenerDatos():
    
    import ObtenerDatos        
    obtenerCupo()

def restar_hora(hora1, hora2):
    formato = "%H:%M"
    h1 = datetime.strptime(hora1, formato)
    h2 = datetime.strptime(hora2, formato)
    comparar = datetime.strptime("10:00", formato)
    comparar2 = datetime.strptime("00:00", formato)
    resultado = h1 - h2
    resultado2 = comparar - comparar2
    if resultado < resultado2:
        return ("0"+str(resultado))
    else:
        return str(resultado)

def mandarInfo(buscar_id_peli, buscar_dept, buscar_nombre_cine, buscar_tipo_doblaje, fecha, buscar_hora):
    metodo.contarAsientos(buscar_id_peli, buscar_dept, buscar_nombre_cine, buscar_tipo_doblaje, fecha, buscar_hora)
    database = OperationCinepolis()
    metodo.contarAsientos(buscar_id_peli, buscar_dept, buscar_nombre_cine, buscar_tipo_doblaje, fecha, buscar_hora)
    
    

def obtenerCupo():
    database = OperationCinepolis()
    horarios = database.funcionesPorDia(date.today())
    if(len(horarios)>0):
        for i in range(len(horarios)):
            newHora = restar_hora(horarios[i][9], "00:02")
            schedule.every().day.at(newHora).do(mandarInfo, horarios[i][0], horarios[i][3], horarios[i][2], horarios[i][4], horarios[i][8], horarios[i][9])
    else:
        obtenerDatos()


# Time
schedule.every().day.at("07:00").do(obtenerDatos)
#obtenerDatos()
obtenerCupo()

while True:
    schedule.run_pending()
    time.sleep(1)
