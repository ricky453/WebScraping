# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from ComprobarElementoWeb import Comprobar

comprobar = Comprobar()
driver_path = 'temp/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get('https://www.cinepolis.com.sv/peliculas/godzilla-vs-kong')
wait=WebDriverWait(driver, 10)
cont=1
while cont<=5:
    print('prueba #'+str(cont)+'#######################')
    comprobar.compDia(driver)
    wait_path=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="date"]/div/div[1]/div/label/div[2]')))
    wait_path.location_once_scrolled_into_view
    time.sleep(0.5)
    wait_path.click()
    time.sleep(3)
    comprobar.compCine(driver)
    comprobar.compHoraFuncion(driver,'//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li/div[2]/div/div[2]/div[1]')
    driver.refresh()    
    cont+