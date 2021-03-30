# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
from datetime import datetime
#Para que la bd
import sys
sys.path.insert(1, 'model/operations/')
sys.path.insert(1, 'temp/chromedriver/')
from operationCinepolis import OperationCinepolis

from ComprobarElementoWeb import Comprobar
#metodos de comprobar si se encuentra elemento en la pagina
comprobar = Comprobar()

class Buscar_Peli:
    def contarAsientos(self, buscar_id_peli, buscar_dept, buscar_nombre_cine, buscar_tipo_doblaje, fecha, buscar_hora):
        
        src_ocupado =  "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADQAAAAtCAYAAADhoUi4AAAABHNCSVQICAgIfAhkiAAAAi9JREFUaEPtmktOwzAQhmfcx5Y62ZQVFReAHoEDIMQFgBugHgAJblBuUJbsegOKxBIhVmzhArW7pm0GTZRUTkhLQy0cwCNFlRJnPL/n87TyFKHAtNYtADgnojMA6BSNcXRviIjXUsrRsvkx/0BrvU9EdwDAoippRNQPw7BXFFxGEGeGiF6rLCYVgYg9KWU/LyojaDweDxDxNB1Ur9dBCFGJLBERzGYz4M/EJkEQyJWClFKcnXjPNBoNQPxEpHNx0+l0IQoRD/L7KROxUmohv9lsOg++KADOUhRF8SMiugrD8NIcFwtKqtoeES2qR61Wi8dxlqqAHaPG13w+N7EbIeIAAO6llG9xvFrrTlLVlpZnFsUIujLOCGdmhU2SIjFApdQQAI6+CtZVgeCs8L5Zw1hUlwVNAGCLX8ijlaY5fcaiftrM7DAp+UJlxshFggUtLQTm6rBYF4J4z/C1bFHNIuEF+QxZ2HAeOV8ULGBUxoVHziNXhhcLYz1yHjkLGJVx4ZHzyJXhxcJYj5xHzgJGZVx45DxyZXixMPZbyPHRkHEIbiEMNy7iUx+tNf0FMckSHmbO5dysq71Z+Tg4I6iqLZRVknPdiJtfL8jsFxGRF2QPeEue/leGqtqGXJXMogxxr2LtVnfVGsnmdygiXnCVewKAriWkXbqJEHGXfynwny1eAGDbZTQbzv0uhDhptVq3i7a+1noHAI4LHD9vOJm114UQ7SiK2qZDInoMguAhvfcBcs3yY6nLfpsAAAAASUVORK5CYII="
        src_ocupado2 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAABFCAYAAAAM7WX1AAAABHNCSVQICAgIfAhkiAAAA0ZJREFUaEPtW71uFDEQntn8FDTE6wcg1DRJR4MET0CQkCgT3iA8QcgbQElF0tAh4AkIHR2hoc4DsHYoaPLjQd+yPjl3mzsvd7dJxFhane5udjzfzGd7Z+xl6ti895siskVEDzveOk78SEQOiqLYNcYcddHLucLe+xUR+TBjw4e7/8XM28aYvVy7sgE45z5H44uioIWFhdw+suTOzs5IRGpZZn5kjDnIuTELgPd+S0TeQuHS0hI6yNHdWeb09DSCOCzLcj1HQZYlzrmPRPQYhgPAvBoiABBNFNaNMYeT+soF4IloBdRZXFycpHOq/09OTiKAJ8YYOG5sywVQk3Oe9IlWRhqJyK619qUCgAeccxqBSVRQCo3zkFIolz9E9TqA9UBnodRpSiGl0OUe0EeJDuzIEtVZqM1NOgtlkeevkFJIKdSBLm2iSiGlkFJI84FRDuhK3GFc/L/TKOr/IYQdZl4jIlyHzIza5L6IoDbae2mxKIqDEMJmY9NKY9N+WjOtExrv/ZqIoP4PoeGGHZPVKwDwlZnvt7FPRPastc/xH3vvV0XkG4xH+RwVaHyGEGJ5Y6Cj5+JubQfswYUGm3Chichra+02V1W1x8wIU106Tzcv0nr9FUSg3gUaLuefn58Trtr7zHfZOQeK3IFgRJqGDVs/EXXfEVheXm7dDYozFTO/AICxlWcYDxB9RwD9AUBbi05F9W4igJRGfUZAAcTQaQQ6PEZANNlq1TEQF4zB3q0O4gw6KYWGnaSzUAZtUhGlkFKoI2WGxZVCN55CeP5HxhPPr03JiJncjiwxZoxQ2JoPICO7boa3oU/z4wsJzUxc1bOSSwHE5H5epxO74gSd02OZTUKPXH0XZRVJ+d7HE2dXAFE+LTDgtzoCVVVJ9HQfpxL/1fh4XzzV2Hx/M0jq+6o6TAsgXehCCF8uALisjDFtp7O8P6XRCIDrzP/ohJEIVFX1m5lvQeCmjQFm3gGF6nPREeF1jkLqfdR6mdliGsV7AT+JaHCe/iasA0T0qSzLjXp/4Pj4+FkI4R1YNMsBN0ddP8qyvFcvaLET59wDoCIiM8eOp1YtIu+ttU+jopEjZ83LDhvN2xq3p+5xNgq+N+/YvBp+x+YPL3CXlc6wULgAAAAASUVORK5CYII="
        src_ocupado3 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFYAAAAuCAYAAACyJ+5bAAAABHNCSVQICAgIfAhkiAAABA9JREFUaEPtm71OG0EQx2eWDwOJlJzdpSFI6UOeAPIAkUKVMqROAbwBfQqgSE3o0gWeICClDzxAFFcRRex1Cj7Ex070v3jtZWVzd75zdPbdSshG3tvb++1/Z3dm55iGVLTWT4loyRizzMz4vkhEj4d0u7jN1omoLiLHSqljIjoIgqAV9+Ik9ThJ5ai6WmuAeysi60QEmKNQDpn5U9aQMwELoMaYLWZ+3U+VzJncKvVAiUi/NlrMvE1EO1moOPXTaq3XRGTTBwqQExMThM+8QLVEAff29pbw2QN0nZnfBUFwmGYUBwYLlYrIFyJadjuglKLJyck0ffrv197c3JAx5s59RWS7VqttDNqZgcBqrRfbUDt2dBSB+tCur699BR8z88tBTENisG2oX+3UxzSHQvM23QdVGkwDADtlILiJwPaCOjU1Negz5PY6wIV5cOxvYrixwbZtKpSK/Wio0HGE6o62Zxr2q9XqSlw1xAbbaDR2mXm1KFDxnL5ZYOaNIAiwJYssscBqrZdFBGoNy/T0dGTD41LBg4u97osgCODB3VtigW02mz+tJ4XpPy4LVRQc+7u7HRORvVqtFs7c+0okWK31qojsFskE9ALm2ltmXohSbQes1npdRJacbdQ+Ee2JyHer1iKZAB+uaxKgWqXUpjFmjZnDxVxE6kqpwyAI9kIR+qu926CI/GLmJ0VXq2Xi7RL+ENGjHuoOdw/caDS2mXktymYU0bb6TFxbi3WmX0AHsQZuNptY4ebhks7MzIQLEy64vLy84z8X2QxYwJ45CD1OMENBrOHi4sJWPQDYMI6GSJSthP+vrq46rl0RnIGoGWt/BxdbMItdwZ2dndmfjmKBHYcAS1xwUfVcO5saLCQPuGWhMIZgQ4zgUqlUOlgSK7YE25VUCXZI08tdwErFZgi5BJshTLep0hSMAthyu9UdpUy3WyXYIYEtPa8uWOt5YRGD15XK80KzZRDmXzwAi5eN9mG7lRpsaQ4ojJ24Ea3ULq2dCEWOcPXINwhncWrFAm6RVesdzYTKzQIs4mEPimprPbWeENFzyyKtYj8S0XtrtMc9UcP3LdwYLHILRGQrE7BIDEP2nR2pIpkE1wSIyI5Sat/mWKQ2BQBrU8ztAVoR4Hq7gBNmRsoqMi3D5JVYYO00vyfjeUje93g0C6EhmbmdzNI9mhmPx8vNUxzh+FtsylAe09pzgyqiI27aPTP/6BwmAurc3NyoPEfu+gmw5+fntl+/O2BhI2ZnZ3PX4VHqkHOY2CrBZjhyPlhtE+GQtIG/siQn4B7ZGGOOuNVqvTHGfE7eVHlFHwLYDCyEaZztFM4PRDRaL2jlb2zxXu6rarX67U7isdZ6nohWlFKnxpjT/PU7fz1i5mci8tB/N+EvQxEHlfctFG4AAAAASUVORK5CYII="
        src_ocupado4 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFcAAAA8CAYAAAAT+yb1AAAABHNCSVQICAgIfAhkiAAABNBJREFUeF7tnEtuHEcMQMnRx0u70AsD3sQGso91gMDOAQLLBwgsnyC5geVlVtYNbCEXkOADWEIOEHlvwPImQBbdNdrq0wzY6pLoRvcMq6Y/WrCBgYQZklX1ivVho4oIiY/3/kVZltuI+BwAHiea6VI7QsQDADh0zp12CXnvudxXRMR14E+fzykRHc1ms33n3FGKYYxV8t4/JaJ3AzSmrSpzRNxzzr1t/ui9f0NEu7H1T5Tnzn69qKPb7EbBrcF+AoAHwRgiAn/6eoioMhX+1v9/yLLsdSgjz/P3iLgzVB1C+bIOAMAd/Ytz7kTbVjUV7/0DIvoawDLQjY0NbTnRctywi4uLGz0ieptl2W6e53uI+Dv/wHVYX1/vtXObFeU6CMiniLjlnJtrGqSGm+f5B0R8xUZns1nVqDGe8/NzWczPAPB3ADtk58pCLy8voSzLMKKqTta0XQW39lo/dqPC8BQe/AUAfuTvGWyf09EyWNKDEdFpvFcLd4eI3k/RKC5TNIzdZzb0lNQGWk5TiPjSOce7mYWPCm6e57uI+IYtbW5uLrPZ++9yWI49LcnGhCkqzP/LGqqCWxQF99KLKeGy54SFZcw5fwy4vIl+ZnCvF9e+PdfgAsDK04L3nsNI3smfhQ1zURRJcPtaza+uroLHVH/Z7tra2rIpr/P3RnCgttMGlwMrALjPRpxzx9JYNedyjF6HtNuNkuZExPvbrSmnBXXrBxYMcMuy/BMR79VR4k20Whd/UIfKc2xGXh3144ikMjLFbmFgZmrzwnP/Q8SHCxQ5VH6CzchLDmWOSppDyODeImVWvHMJD7MSkdw+FkXBr/R+aNveNON789zbULzrvYYIeE4YbvUaiheItkWiuYE3z7320669tuRlcNUz7u1WzOBGQNOKyjd05rlaako5g6sElSJmcFOoKXUMrhJUipjBTaGm1DG4SlApYgY3hZpSx+AqQaWIGdwUakodg6sElSJmcFOoKXUMrhJUipjBTaGm1DG4SlApYgY3hZpSx+AqQaWIGdwUakodg6sElSJmcFOoKXUMrhJUipjBTaGm1DG4SlApYqPAlQeRF1Uy9TRhsBmuYTXL6/peCyz29GUob3C4XNCq0LQQpNxU5cqOlu3u9dzC1I1L6ZAhdXqFKyvKhlc5fBzTaD571TZSwkG4GFupsm116A3u1Jc9Ghf9KkZjHwjU3iiKPojHx+bDIjB2oxiktmGpnqnVG2RBuwtwpx493AGDwA2npacYjsFzDa52fEXKhQXlrlzy4+r3tqCZ5157g00LkaMiRtzgxtCKlB0Eru0WBpwW7gJcOe9PfWs9ZkHj25H3uyocsnRMuVKL4XgJAFX+l7GDmUaumyqoaksDIwKeb3xV6iaXQjNvDXuL8BhOw+K4YWPF9dyhXFnxHIa8D/zd0MmDQrmNdwv/AsCj4L3yBmXYk9d6h3z3l/OE/bNkbv8GAL8BwMdwQztyLVhZnIj2syzbkddpVzYab+AMAH4FgL/41uki9eruLwt477f5dnoHuM+IuM0Jy+qO2As32OPrlqRxRkR7MiNSnRbmj5E7+phvqQsOzOunlhad1byOvkvDUudakPLztiRldZq/vlMMtpLvSvXHt+0BgHMdjPGctmXDq3MtfJcSQNb3f2AbLhVOh2x8AAAAAElFTkSuQmCC"
        #fecha de hoy
        fechaActual= fecha
        dia=fechaActual.day
        finalizado=False

        driver_path = 'temp/chromedriver/chromedriver.exe'
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()
        # Inicializamos el navegador
        driver.get('https://www.cinepolis.com.sv/cartelera/')
        wait=WebDriverWait(driver, 20)


        #selecciona buscador de departamento
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
            'input#cityBillboardSearch.el-input__inner')))\
                .click()
        #seleccionar dept
        if(buscar_dept=='San Salvador'):
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="238"]'))).click()
        elif (buscar_dept=='Santa Ana'):
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="239"]'))).click()
        time.sleep(2)
        #selecciona buscador de cine
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
            'input#cinemaBillboardSearch.el-input__inner')))\
                .click()
        #selecciona todos los cines
        wait.until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="-1"]')))\
                .click()
                    
        time.sleep(2)
        
        ###seleccionar pelicula a buscar###
        comprobar.compPelicula(driver, '//*[@id="main-app"]/div/div[5]/section[5]/div/div/div[1]')
        wait_path=wait.until(EC.presence_of_element_located((By.ID,buscar_id_peli)))
        wait_path.location_once_scrolled_into_view

        time.sleep(0.3)
        wait_path.click()
        time.sleep(4)
        ###localiza el dia###
        comprobar.compDia(driver)
        wait_path=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="date"]/div/div[1]/div/label/div[2]')))
        wait_path.location_once_scrolled_into_view
        time.sleep(0.5)

        numero_dia = driver.find_element_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div/label/div[2]/div/div/div[2]/span')
        #saber si la fecha actual es igual al dia seleccionado en la pagina
        if(dia==int(numero_dia.text)): 
            wait_path.click() 
            time.sleep(5)

            ###SELECCIONAR HORAS###
            comprobar.compCine(driver)
            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]')))
            #cantidad de cines y recorrer cada uno
            count_li_cines = len(driver.find_elements_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li')) 
            count_cine=1
            while count_cine<=count_li_cines:
                encontrado=False 
                nombre_cine=driver.find_element_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li['+str(count_cine)+']/div[1]/div[1]/h3').text
                if(buscar_nombre_cine==nombre_cine):
                    #cantidad de tipos de doblaje que tiene la pelicula y recorrer cada uno
                    count_divs_tiposcine=len(driver.find_elements_by_xpath('//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li['+str(count_cine)+']/div[2]/div'))
                    count_tipocine=1
                    while count_tipocine<=count_divs_tiposcine:
                        #cantidad de horarios que hay en un tipo de dobleje de una pelicula y recorrer cada uno
                        count_divs_hora=len(driver.find_elements_by_xpath('//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li['+str(count_cine)+']/div[2]/div['+str(count_tipocine)+']/div[2]/div'))
                        count_hora=1
                        while count_hora<=count_divs_hora:
                            #seleccionar cada hora
                            text_path='//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li['+str(count_cine)+']/div[2]/div['+str(count_tipocine)+']/div[2]/div['+str(count_hora)+']'
                            comprobar.compHoraFuncion(driver, text_path)

                            wait_path=wait.until(EC.presence_of_element_located((By.XPATH,text_path)))
                            
                            #recolectar el tipo de doblaje cuando se recorre bucle de las horas
                            tipo_doblaje1 = driver.find_element_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li['+str(count_cine)+']/div[2]/div['+str(count_tipocine)+']/div[1]/span').text
                            tipo_doblaje2 = driver.find_element_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li['+str(count_cine)+']/div[2]/div['+str(count_tipocine)+']/div[1]/h5').text
                            tipo_doblaje=tipo_doblaje1+tipo_doblaje2 
                                            
                            if(buscar_tipo_doblaje==tipo_doblaje):
                                hora_peli=driver.find_element_by_xpath(text_path).text
                                if(buscar_hora==hora_peli):
                                    wait_path.location_once_scrolled_into_view
                                    time.sleep(0.5)
                                    wait_path.click()
                                    time.sleep(0.3)
                                    encontrado=True
                                    #seleccionar el botton
                                    wait_path=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buyTickets"]')))
                                    wait_path.location_once_scrolled_into_view
                                    time.sleep(0.5)
                                    wait_path.click()
                                    time.sleep(4)
                                    
                                    #Contar asientos ocupados/vendidos
                                    comprobar.compAsientos(driver)
                                    newText_path = '//*[@id="roomContainer"]/div/div[4]/div/div/div'
                                    e = driver.find_elements_by_xpath(newText_path)
                                    count = 0
                                    for a in range(len(e)):
                                        f = '//*[@id="roomContainer"]/div/div[4]/div/div/div['+str(
                                            a)+']/div/div/img'
                                        p = driver.find_elements_by_xpath(f)
                                        if(len(p) > 0):
                                            e = driver.find_element_by_xpath(
                                                f).get_attribute('src')
                                            if e == src_ocupado or e == src_ocupado2 or e == src_ocupado3 or e == src_ocupado4:
                                                count = count + 1
                                    print('Asientos ocupados: '+str(count))
                                    database = OperationCinepolis()
                                    database.updateAsientosOcupados(buscar_id_peli, buscar_dept, buscar_nombre_cine, buscar_tipo_doblaje, fecha, buscar_hora, count)
                                    
                                    finalizado=True
                                    break     
                            else:
                                break
                            #termina if del tipo de doblaje
                            count_hora+=1
                        if(finalizado): 
                            break
                        count_tipocine+=1
                    if(encontrado==False):
                        print('no existe la funcion que se desea buscar en la pagina')
                    if(finalizado): 
                        break
                #termina if(buscar_nombre_cine==nombre_cine)  
                count_cine+=1
        driver.quit()  