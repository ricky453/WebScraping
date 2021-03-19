from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait #para que cargue la pagina
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


#para usar navegador chrome
driverBrowser = webdriver.Chrome('C:/Users/Administrador/Downloads/chromedriver_win32/chromedriver')
delay = 4 #seconds

#variables donde almacenaremos productos, precios y calificacion
products = []
prices = []
ratings = []

#abrir url de la pagina
driverBrowser.get('https://www.cinepolis.com.sv/cartelera')


#extraccion de datos
content = driverBrowser.page_source
soup = BeautifulSoup(content, 'html.parser')


#nos dirigimos a cartelera

#btnAudio = soup.find('div img', attrs={'id': 'audioImg'})
#btnAudio.click()
try:
    element = WebDriverWait(driverBrowser, 10).until(
            EC.element_to_be_clickable((By.ID, 'main')))

    price = soup.find("/html/body/main/div/div/div[5]/section[4]/div/h1", attrs={"class" : "billboard-page_content_title"})
    #prices.append(price)
    print(price)

except TimeoutException:
    print("Tardo mucho tiempo!")




##exportando datos a csv
df = pd.DataFrame({'Precio Name': prices})
df.to_csv('products.csv', index  = False, encoding = 'utf-8')