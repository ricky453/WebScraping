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

class Buscar_Peli:
    def contarAsientos(self, buscar_id_peli, buscar_dept, buscar_nombre_cine, buscar_tipo_doblaje, fecha, buscar_hora):
        
        src_ocupado = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADQAAAAtCAYAAADhoUi4AAAABHNCSVQICAgIfAhkiAAAAi9JREFUaEPtmktOwzAQhmfcx5Y62ZQVFReAHoEDIMQFgBugHgAJblBuUJbsegOKxBIhVmzhArW7pm0GTZRUTkhLQy0cwCNFlRJnPL/n87TyFKHAtNYtADgnojMA6BSNcXRviIjXUsrRsvkx/0BrvU9EdwDAoippRNQPw7BXFFxGEGeGiF6rLCYVgYg9KWU/LyojaDweDxDxNB1Ur9dBCFGJLBERzGYz4M/EJkEQyJWClFKcnXjPNBoNQPxEpHNx0+l0IQoRD/L7KROxUmohv9lsOg++KADOUhRF8SMiugrD8NIcFwtKqtoeES2qR61Wi8dxlqqAHaPG13w+N7EbIeIAAO6llG9xvFrrTlLVlpZnFsUIujLOCGdmhU2SIjFApdQQAI6+CtZVgeCs8L5Zw1hUlwVNAGCLX8ijlaY5fcaiftrM7DAp+UJlxshFggUtLQTm6rBYF4J4z/C1bFHNIuEF+QxZ2HAeOV8ULGBUxoVHziNXhhcLYz1yHjkLGJVx4ZHzyJXhxcJYj5xHzgJGZVx45DxyZXixMPZbyPHRkHEIbiEMNy7iUx+tNf0FMckSHmbO5dysq71Z+Tg4I6iqLZRVknPdiJtfL8jsFxGRF2QPeEue/leGqtqGXJXMogxxr2LtVnfVGsnmdygiXnCVewKAriWkXbqJEHGXfynwny1eAGDbZTQbzv0uhDhptVq3i7a+1noHAI4LHD9vOJm114UQ7SiK2qZDInoMguAhvfcBcs3yY6nLfpsAAAAASUVORK5CYII="

        #fecha de hoy
        fechaActual= fecha
        dia=fechaActual.day
        finalizado=False
        driver_path = 'temp/chromedriver/chromedriver.exe'

        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()
        # Inicializamos el navegador
        driver.get('https://www.cinepolis.com.sv/cartelera/')
        wait=WebDriverWait(driver, 60)

        count_localted_cine=3
        count_dept=1
        if buscar_dept== 'San Salvador':
            count_dept=1
            count_localted_cine=3
        elif buscar_dept== 'Santa Ana':
            count_dept=2
            count_localted_cine=2

        #selecciona buscador de departamento
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
            'input#cityBillboardSearch.el-input__inner')))\
                .click()
        #selecciona san salvador o santa ana
        wait.until(EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div[2]/div[1]/div[1]/ul/li['+str(count_dept)+']')))\
                .click()
        time.sleep(2)
        #selecciona buscador de cine
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
            'input#cinemaBillboardSearch.el-input__inner')))\
                .click()
        #selecciona todos los cines
        wait.until(EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div['+str(count_localted_cine)+']/div[1]/div[1]/ul/li[1]')))\
                .click()
                    
        time.sleep(2)
        #seleccionar pelicula a buscar  
        print('selecciona el cine por id')
        wait_path=wait.until(EC.presence_of_element_located((By.ID,buscar_id_peli)))
        wait_path.location_once_scrolled_into_view

        time.sleep(0.3)
        wait_path.click()
        time.sleep(4)
        #localiza el dia
        wait_path=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="date"]/div/div[1]/div/label/div[2]')))
        wait_path.location_once_scrolled_into_view
        time.sleep(0.5)

        numero_dia = driver.find_element_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div/label/div[2]/div/div/div[2]/span')
        #saber si la fecha actual es igual al dia seleccionado en la pagina
        print(str(dia)+'##dias##'+numero_dia.text)
        if(dia==int(numero_dia.text)): 
            wait_path.click() 
            time.sleep(4)
            #SELECCIONAR HORAS
            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul')))
            #cantidad de cines y recorrer cada uno
            count_li_cines = len(driver.find_elements_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li')) 
            
            count_cine=1
            while count_cine<=count_li_cines:

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
                            wait_path=wait.until(EC.presence_of_element_located((By.XPATH,text_path)))
                            wait_path.location_once_scrolled_into_view
                            time.sleep(0.5)
                            #recolectar el tipo de doblaje cuando se recorre bucle de las horas
                            tipo_doblaje1 = driver.find_element_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li['+str(count_cine)+']/div[2]/div['+str(count_tipocine)+']/div[1]/span').text
                            tipo_doblaje2 = driver.find_element_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li['+str(count_cine)+']/div[2]/div['+str(count_tipocine)+']/div[1]/h5').text
                            tipo_doblaje=tipo_doblaje1+tipo_doblaje2 
                            print('#'+tipo_doblaje+'#')                   
                            if(buscar_tipo_doblaje==tipo_doblaje):
                                hora_peli=driver.find_element_by_xpath(text_path).text
                                if(buscar_hora==hora_peli):
                                    wait_path.click()
                                    time.sleep(0.3)
                                    #seleccionar el botton
                                    wait_path=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buyTickets"]')))
                                    wait_path.location_once_scrolled_into_view
                                    time.sleep(0.5)
                                    wait_path.click()
                                    time.sleep(5)
                                    #Contar asientos ocupados/vendidos
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
                                            if e == src_ocupado:
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
                    if(finalizado): 
                        break
                #termina if(buscar_nombre_cine==nombre_cine)  
                count_cine+=1
        driver.quit()            

