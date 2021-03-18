from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


#para usar navegador chrome
driver = webdriver.Chrome('C:/Users/Administrador/Downloads/chromedriver_win32/chromedriver')

#variables donde almacenaremos productos, precios y calificacion
products = []
prices = []
ratings = []

#abrir url de la pagina
driver.get('https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2')


#extraccion de datos
content = driver.page_source
soup = BeautifulSoup(content)

price = soup.find('div', attrs= {'class': '_30jeq3'})
prices.append(price.text)


##exportando datos a csv
df = pd.DataFrame({'Precio Name': prices})
df.to_csv('products.csv', index  = False, encoding = 'utf-8')
