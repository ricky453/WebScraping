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
from operationCinepolis import OperationCinepolis

#fecha de hoy
fechaActual= datetime.now()
fechaActual= fechaActual.date()
dia=fechaActual.day

driver_path = 'C:\\Users\\ivanp\\Desktop\\TrabajoFinal\\chromedriver.exe'

driver = webdriver.Chrome(driver_path)
driver.maximize_window()
# Inicializamos el navegador
driver.get('https://www.cinepolis.com.sv/cartelera/')
wait=WebDriverWait(driver, 60)

count_localted_cine=3
count_dept=1
while count_dept<=2:
    #selecciona buscador de departamento
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        'input#cityBillboardSearch.el-input__inner')))\
            .click()
    dept=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li['+str(count_dept)+']').text
    #selecciona san salvador
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
    #SELECCIONAR PELICUAL

    #cantidad de peliculas y recorrer en bucle
    count_divs_peliculas = len(driver.find_elements_by_xpath("/html/body/main/div/div/div[5]/section[5]/div/div/div")) 
    count_pelicula=1    
    while count_pelicula<=count_divs_peliculas:

        text_path='/html/body/main/div/div/div[5]/section[5]/div/div/div['+str(count_pelicula)+']'
        wait_path=wait.until(EC.presence_of_element_located((By.XPATH,text_path)))
        wait_path.location_once_scrolled_into_view

        id_peli=driver.find_element_by_xpath(text_path).get_property("id")

        time.sleep(0.3)
        wait_path.click()
        time.sleep(4)
        #localiza el dia
        wait_path=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="date"]/div/div[1]/div/label/div[2]')))
        wait_path.location_once_scrolled_into_view
        time.sleep(0.5)

        numero_dia = driver.find_element_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div/label/div[2]/div/div/div[2]/span')

        if(dia==int(numero_dia.text)): #saber si la fecha actual es igual al dia seleccionado en la pagina
            wait_path.click() 
            time.sleep(4)
            #SELECCIONAR HORAS
            #cantidad de cines y recorrer cada uno
            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul')))
            count_li_cines = len(driver.find_elements_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li')) 
            count_cine=1
            while count_cine<=count_li_cines:
                #cantidad de tipos de doblaje que tiene la pelicula y recorrer cada uno
                count_divs_tiposcine=len(driver.find_elements_by_xpath('//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li['+str(count_cine)+']/div[2]/div'))
                count_tipocine=1
                while count_tipocine<=count_divs_tiposcine:
                    #cantidad de horarios que hay en un tipo de dobleje de una pelicula y recorrer cada uno
                    count_divs_hora=len(driver.find_elements_by_xpath('//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li['+str(count_cine)+']/div[2]/div['+str(count_tipocine)+']/div[2]/div'))
                    
                    count_hora=1
                    while count_hora<=count_divs_hora:
                        
                        text_path='//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li['+str(count_cine)+']/div[2]/div['+str(count_tipocine)+']/div[2]/div['+str(count_hora)+']'
                        wait_path=wait.until(EC.presence_of_element_located((By.XPATH,text_path)))
                        wait_path.location_once_scrolled_into_view
                        time.sleep(0.5)
                        tipo_doblaje1 = driver.find_element_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li['+str(count_cine)+']/div[2]/div['+str(count_tipocine)+']/div[1]/span').text
                        tipo_doblaje2 = driver.find_element_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li['+str(count_cine)+']/div[2]/div['+str(count_tipocine)+']/div[1]/h5').text
                    
                        wait_path.click()
                        time.sleep(0.3)
                        
                        #seleccionar el botton
                        wait_path=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buyTickets"]')))
                        wait_path.location_once_scrolled_into_view
                        time.sleep(0.5)
                        wait_path.click()
                        time.sleep(2)

                        ###recolectar datos### 
                        nombre_peli=driver.find_element_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/div/div/div/div[2]/div[1]').text
                        nombre_cine=driver.find_element_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/div/div/div/div[2]/div[2]').text
                        hora_sala=driver.find_element_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/div/div/div/div[2]/div[4]').text
                        lista_hora_sala_string = hora_sala.split(' ')
                        tipo_doblaje= tipo_doblaje1+tipo_doblaje2
                        
                        database = OperationCinepolis() 
                        database.insertFunsiones(id_peli,nombre_peli,dept,nombre_cine,tipo_doblaje,fechaActual,lista_hora_sala_string[0],lista_hora_sala_string[2])
                        print('success insert')
                        driver.back()
                        time.sleep(3)
                        #localizar y seleccionar dia
                        wait_path=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="date"]/div/div[1]/div/label/div[2]')))
                        wait_path.location_once_scrolled_into_view
                        time.sleep(0.5)
                        wait_path.click()
                        time.sleep(3)
                        count_hora+=1
                    count_tipocine+=1
                count_cine+=1
        
        driver.back()
        time.sleep(1)
        count_pelicula+=1
    count_dept+=1
    count_localted_cine-=1
driver.quit()

