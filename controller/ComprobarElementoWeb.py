# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

def ComprobarCine():
    ejecucion=True
    while ejecucion==True:
        try:
            prueba=driver.find_elements_by_xpath('//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[1]/div[1]')
            prueba=driver.find_elements_by_xpath('//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[2]/div[1]')
            ejecucion=False
        except Exception as e:
            ejecucion==True
            driver.refresh()
            wait_path=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="date"]/div/div[1]/div/label/div[2]')))
            wait_path.location_once_scrolled_into_view
            time.sleep(0.5)
            wait_path.click()
            time.sleep(3)

def ComprobarHora(count_cine,count_tiposcine,count_hora):
    ejecucion=True
    while ejecucion==True:
        try:
            prueba=driver.find_elements_by_xpath('//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[1]/div[1]')
            prueba=driver.find_elements_by_xpath('//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[2]/div[1]')
            prueba=driver.find_element_by_xpath('//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li['+str(count_cine)+']/div[2]/div['+str(count_tipocine)+']/div[2]/div['+str(count_hora)+']')
            ejecucion=False
        except Exception as e:
            ejecucion==True
            driver.refresh()
            wait_path=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="date"]/div/div[1]/div/label/div[2]')))
            wait_path.location_once_scrolled_into_view
            time.sleep(0.5)
            wait_path.click()
            time.sleep(3)