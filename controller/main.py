import schedule
import time
from datetime import datetime


def job(hora, nombre):
    print("Leyendo tiempo... "+hora+" - "+nombre)


def coding():
    print("Codigo...")


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


# Time
horarios = [["09:11", "Ivan"], ["09:11", "Kike"], [
    "09:12", "Ricardo"], ["09:13", "Pedro"], ["09:14", "Nadie"]]

for i in range(len(horarios)):
    newHora = restar_hora(horarios[i][0], "00:02")
    print(newHora)
    # print(horarios[i][0])
    schedule.every().day.at(newHora).do(job, horarios[i][0], horarios[i][1])

schedule.every(10).seconds.do(coding)

while True:
    schedule.run_pending()
    time.sleep(1)
