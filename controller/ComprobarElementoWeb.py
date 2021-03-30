# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
class Comprobar:
    def compPelicula(self, driver,text_path):
        ejecucion=True
        while ejecucion==True:
            try:
                wait_p=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,text_path)))
                prueba=driver.find_elements_by_xpath(text_path)
                ejecucion=False
                print('Elementos Localizados en metodo compPelicula')
            except Exception as e:
                ejecucion==True
                driver.refresh()
                time.sleep(3)
                prunc('no cargo peliculas')

    def compDia(self, driver):
        ejecucion=True
        while ejecucion==True:
            try:
                wait_p=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="date"]/div/div[1]/div/label/div[2]')))
                prueba=driver.find_elements_by_xpath('//*[@id="date"]/div/div[1]/div/label/div[2]')
                wait_p.location_once_scrolled_into_view
                time.sleep(0.3)
                ejecucion=False
                print('Elementos Localizados en metodo compDia')
            except Exception as e:
                ejecucion==True
                driver.refresh()
                time.sleep(3)
                prunc('no cargo dia')
                
    def compCine(self, driver):
        ejecucion=True
        while ejecucion==True:
            try:
                prueba=driver.find_elements_by_xpath('//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[1]/div[1]')
                prueba=driver.find_elements_by_xpath('//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[2]/div[1]')
                ejecucion=False
                print('Elementos Localizados en metodo compCine')
            except Exception as e:
                ejecucion==True
                driver.refresh()
                time.sleep(2)
                wait_p=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="date"]/div/div[1]/div/label/div[2]')))
                wait_p.location_once_scrolled_into_view
                time.sleep(0.5)
                wait_path.click()
                time.sleep(4)
                print('no cargo cines')

    def compHoraFuncion(self,driver, text_path):
        ejecucion=True
        while ejecucion==True:
            try:
                prueba=driver.find_elements_by_xpath('//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[1]/div[1]')
                prueba=driver.find_elements_by_xpath('//*[@id="main-app"]/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[2]/div[1]')
                
                wait_p=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,text_path)))
                prueba=driver.find_element_by_xpath(text_path)
                wait_p.location_once_scrolled_into_view
                time.sleep(0.5)
                wait_p.click()
                ejecucion=False
                print('Elementos Localizados en metodo compHoraFuncion')
            except Exception as e:
                ejecucion==True
                driver.refresh()
                time.sleep(2)
                wait_p=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="date"]/div/div[1]/div/label/div[2]')))
                wait_p.location_once_scrolled_into_view
                time.sleep(0.5)
                wait_p.click()
                time.sleep(4)
                print('no cargo hora')

    def compDatosFuncion(self, driver):
        ejecucion=True
        while ejecucion==True:
            try:
                wait_p=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/main/div/div/div[5]/div/div[2]/div/div/div/div[2]')))
                prueba=driver.find_elements_by_xpath('/html/body/main/div/div/div[5]/div/div[2]/div/div/div/div[2]')
                ejecucion=False
                print('Elementos Localizados en metodo compDatosFuncion')
            except Exception as e:
                ejecucion==True
                driver.refresh()
                time.sleep(3)
                prunc('no cargo datos de la funcion')

    def compAsientos(self, driver):
        ejecucion=True
        while ejecucion==True:
            try:
                wait_p=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="roomContainer"]/div/div[4]/div/div/div')))
                prueba=driver.find_elements_by_xpath('//*[@id="roomContainer"]/div/div[4]/div/div/div')
                ejecucion=False
                print('Elementos Localizados en metodo compAsientos')
            except Exception as e:
                ejecucion==True
                driver.refresh()
                time.sleep(5)
                prunc('no cargo Asientos')
