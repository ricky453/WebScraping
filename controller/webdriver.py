# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
#import pandas as pd
#

driver_path = 'C:\\Users\\ivanp\\Desktop\\TrabajoFinal\\chromedriver.exe'

driver = webdriver.Chrome(driver_path)
driver.maximize_window()
# Inicializamos el navegador
driver.get('https://www.cinepolis.com.sv/cartelera/')

#selecciona san salvador
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        'input#cityBillboardSearch.el-input__inner')))\
            .click()

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, 
    '/html/body/div[2]/div[1]/div[1]/ul/li[1]')))\
        .click()

#selecciona todos los cines
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        'input#cinemaBillboardSearch.el-input__inner')))\
            .click()

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, 
    '/html/body/div[3]/div[1]/div[1]/ul/li[1]')))\
        .click()

#seleccionar la tercer pelicula 
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, 
    '/html/body/main/div/div/div[5]/section[5]/div/div/div[3]/div[1]/img')))\
        .click()
#seleccionar dia
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, 
    '/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div/label/div[2]')))\
        .click()
#seleccionar hora
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, 
    '/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[2]/div/div[2]/div/label')))\
        .click()
#selecciona botton "comprar boletos"
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, 
    '/html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[5]/button')))\
        .click()

#path de la tabla donde estan los asientos
# /html/body/main/div/div/div[5]/div/div[4]/div/div/div[4]/div/div        

#path del dia
# 
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div/label/div[2]
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div/label/div[2]

#path de la hora 
# 
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[2]/div[1]/div[2]/div[1]/label  doblada
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[2]/div[1]/div[2]/div[2]/label  doblada
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[1]/div[2]/div[2]/div[2]/div   /label     sub

# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[2]/div[2]/div   /div[2]/div[1]/label     dob
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[2]/div[2]/div   /div[2]/div[2]/label     dob
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[2]/div[2]/div   /div[2]/div[3]/label     dob

# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[3]/div[2]/div   /div[2]/div[1]/label     dob
# /html/body/main/div/div/div[5]/div/div[2]/section/div[2]/div[2]/div[1]/div/div[4]/ul/li[3]/div[2]/div   /div[2]/div[2]/label     dob
#                                                                                     /cines       /dob o sub
#                                                                                                                /hora

#path de pelicula

# /html/body/main/div/div/div[5]/section[5]/div/div/div[1]/div[2]/button
# /html/body/main/div/div/div[5]/section[5]/div/div/div[2]/div[2]/button
# /html/body/main/div/div/div[5]/section[5]/div/div/div[9]/div[2]/button
# /html/body/main/div/div/div[5]/section[5]/div/div/div[1]/div[1]/img
